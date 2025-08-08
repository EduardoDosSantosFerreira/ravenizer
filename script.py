import subprocess
import sys
import platform
from threading import Thread, Event
from PySide6.QtCore import Signal, QObject


class RavenizerLogic(QObject):
    update_message = Signal(str)
    update_status = Signal(str)
    update_complete = Signal(bool)

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.running = False
        self.paused = False
        self.pause_event = Event()
        self.current_process = None

        # Conectar sinais
        self.update_message.connect(self.append_log)
        self.update_status.connect(self.ui.status_label.setText)
        self.update_complete.connect(self.on_update_complete)

        # Conectar botões
        self.ui.update_button.clicked.connect(self.start_update)
        self.ui.pause_button.clicked.connect(self.toggle_pause)
        self.ui.pause_button.setEnabled(False)  # Inicialmente desabilitado

    def append_log(self, message):
        self.ui.output_log.append(message)

    def on_update_complete(self, success):
        self.running = False
        self.ui.update_button.setEnabled(True)
        self.ui.pause_button.setEnabled(False)
        status = (
            "Atualização concluída com sucesso!"
            if success
            else "Atualização concluída com erros."
        )
        self.update_status.emit(status)

    def start_update(self):
        if self.running:
            return

        self.running = True
        self.paused = False
        self.pause_event.clear()
        self.ui.update_button.setEnabled(False)
        self.ui.pause_button.setEnabled(True)
        self.ui.pause_button.setText("Pausar")
        self.ui.output_log.clear()

        # Obter a escolha do usuário
        use_winget = self.ui.winget_checkbox.isChecked()
        use_choco = self.ui.choco_checkbox.isChecked()
        use_scoop = self.ui.scoop_checkbox.isChecked()
        use_npackd = self.ui.npackd_checkbox.isChecked()

        # Iniciar thread de atualização
        self.update_thread = Thread(
            target=self.run_updates, args=(use_winget, use_choco, use_scoop, use_npackd)
        )
        self.update_thread.start()

    def toggle_pause(self):
        if not self.running:
            return

        self.paused = not self.paused

        if self.paused:
            self.pause_event.set()
            self.ui.pause_button.setText("Continuar")
            self.update_status.emit("Atualização pausada")
            self.update_message.emit("\n=== Atualização pausada pelo usuário ===")
            if self.current_process:
                self.current_process.terminate()  # Encerra o processo atual
        else:
            self.pause_event.clear()
            self.ui.pause_button.setText("Pausar")
            self.update_status.emit("Atualização em andamento...")
            self.update_message.emit("\n=== Atualização continuada pelo usuário ===")
            # Reinicia a thread de atualização
            use_winget = self.ui.winget_checkbox.isChecked()
            use_choco = self.ui.choco_checkbox.isChecked()
            use_scoop = self.ui.scoop_checkbox.isChecked()
            use_npackd = self.ui.npackd_checkbox.isChecked()
            self.update_thread = Thread(
                target=self.run_updates, args=(use_winget, use_choco, use_scoop, use_npackd)
            )
            self.update_thread.start()

    def run_updates(self, use_winget, use_choco, use_scoop, use_npackd):
        try:
            self.update_status.emit("Iniciando atualizações...")

            if platform.system() == "Windows":
                self.update_windows(use_winget, use_choco, use_scoop, use_npackd)
            else:
                self.update_message.emit(
                    "Sistema não suportado. Apenas Windows é compatível."
                )

            self.update_complete.emit(True)
        except Exception as e:
            self.update_message.emit(f"Erro: {str(e)}")
            self.update_complete.emit(False)

    def run_command(self, command, process_name):
        """Executa um comando e emite o output em tempo real"""
        self.update_message.emit(f"\n=== Executando {process_name} ===")

        try:
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="replace",
                shell=True,
            )
            self.current_process = process

            while True:
                if self.pause_event.is_set():
                    return False

                output = process.stdout.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    self.update_message.emit(output.strip())

            return process.poll() == 0
        except Exception as e:
            self.update_message.emit(f"Erro ao executar {process_name}: {e}")
            return False
        finally:
            self.current_process = None

    def update_windows(self, use_winget, use_choco, use_scoop, use_npackd):
        """Executa as atualizações para Windows conforme selecionado pelo usuário"""
        total_steps = sum([use_winget, use_choco, use_scoop, use_npackd])
        current_step = 0

        if total_steps == 0:
            self.update_message.emit("Nenhuma opção de atualização selecionada.")
            return

        if use_winget:
            if self.pause_event.is_set():
                return
            success = self.run_command("winget upgrade --all", "winget")
            current_step += 1
            if not success:
                self.update_message.emit("winget encontrou erros.")

        if use_choco:
            if self.pause_event.is_set():
                return
            success = self.run_command("choco upgrade all -y", "Chocolatey")
            current_step += 1
            if not success:
                self.update_message.emit("Chocolatey encontrou erros.")

        if use_scoop:
            if self.pause_event.is_set():
                return
            # Atualizar scoop e depois os pacotes
            success = self.run_command("scoop update", "Scoop (auto-atualização)")
            if success:
                success = self.run_command("scoop update *", "Scoop (pacotes)")
            current_step += 1
            if not success:
                self.update_message.emit("Scoop encontrou erros.")

        if use_npackd:
            if self.pause_event.is_set():
                return
            # Npackd CLI (npckd) - assumindo que está no PATH
            success = self.run_command("npckd upgrade -all", "Npackd")
            current_step += 1
            if not success:
                self.update_message.emit("Npackd encontrou erros.")