import subprocess
import sys
import platform
from threading import Thread
from PySide6.QtCore import Signal, QObject

class RavenizerLogic(QObject):
    update_progress = Signal(int)
    update_message = Signal(str)
    update_status = Signal(str)
    update_complete = Signal(bool)
    
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.running = False
        
        # Conectar sinais
        self.update_progress.connect(self.ui.progress_bar.setValue)
        self.update_message.connect(self.append_log)
        self.update_status.connect(self.ui.status_label.setText)
        self.update_complete.connect(self.on_update_complete)
        
        # Conectar botão
        self.ui.update_button.clicked.connect(self.start_update)
    
    def append_log(self, message):
        self.ui.output_log.append(message)
    
    def on_update_complete(self, success):
        self.running = False
        self.ui.update_button.setEnabled(True)
        status = "Atualização concluída com sucesso!" if success else "Atualização concluída com erros."
        self.update_status.emit(status)
    
    def start_update(self):
        if self.running:
            return
            
        self.running = True
        self.ui.update_button.setEnabled(False)
        self.ui.output_log.clear()
        
        # Iniciar thread de atualização
        self.update_thread = Thread(target=self.run_updates)
        self.update_thread.start()
    
    def run_updates(self):
        try:
            self.update_status.emit("Iniciando atualizações...")
            self.update_progress.emit(0)
            
            if platform.system() == "Windows":
                self.update_windows()
            else:
                self.update_message.emit("Sistema não suportado. Apenas Windows é compatível.")
            
            self.update_complete.emit(True)
        except Exception as e:
            self.update_message.emit(f"Erro: {str(e)}")
            self.update_complete.emit(False)
    
    def update_windows(self):
        """Executa todas as atualizações para Windows"""
        self.update_message.emit("\n=== Atualizando Sistema via winget ===")
        try:
            subprocess.run(['winget', 'upgrade', '--all'], check=True)
            self.update_message.emit("winget concluído com sucesso.")
            self.update_progress.emit(50)
        except Exception as e:
            self.update_message.emit(f"Erro no winget: {e}")
        
        self.update_message.emit("\n=== Atualizando Programas via Chocolatey ===")
        try:
            subprocess.run(['choco', 'upgrade', 'all', '-y'], check=True)
            self.update_message.emit("Chocolatey concluído com sucesso.")
            self.update_progress.emit(100)
        except Exception as e:
            self.update_message.emit(f"Erro no Chocolatey: {e}")