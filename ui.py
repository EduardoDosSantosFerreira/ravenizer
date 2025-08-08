from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QGroupBox,
    QFrame,
    QScrollArea,
    QCheckBox,
    QSpacerItem,
    QSizePolicy,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon


class RavenizerUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ravenizer - Atualizador Windows")
        self.setGeometry(100, 100, 1000, 800)
        self.setMinimumSize(800, 600)

        try:
            self.setWindowIcon(QIcon("raven_icon.png"))
        except Exception:
            pass

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        self.setup_ui()

    def setup_ui(self):
        self.setup_header()
        self.setup_body()
        self.setup_footer()
        self.apply_style()

    def setup_header(self):
        header_frame = QFrame()
        header_frame.setObjectName("headerFrame")
        header_layout = QVBoxLayout(header_frame)
        header_layout.setContentsMargins(0, 10, 0, 20)

        self.title_label = QLabel("RAVENIZER WINDOWS UPDATER")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Segoe UI", 20, QFont.Bold))

        self.subtitle_label = QLabel("Atualização Automática via winget e Chocolatey")
        self.subtitle_label.setAlignment(Qt.AlignCenter)
        self.subtitle_label.setFont(QFont("Segoe UI", 12))

        header_layout.addWidget(self.title_label)
        header_layout.addWidget(self.subtitle_label)
        self.main_layout.addWidget(header_frame)

    def setup_body(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_content = QWidget()
        body_layout = QVBoxLayout(scroll_content)
        body_layout.setContentsMargins(15, 0, 15, 0)
        scroll_area.setWidget(scroll_content)

        # Seção de configuração
        config_group = QGroupBox("Configurações de Atualização")
        config_layout = QVBoxLayout(config_group)

        # Checkboxes para seleção de pacotes
        self.winget_checkbox = QCheckBox("Atualizar aplicativos via winget")
        self.winget_checkbox.setChecked(True)
        self.choco_checkbox = QCheckBox("Atualizar programas via Chocolatey")
        self.choco_checkbox.setChecked(True)

        config_layout.addWidget(self.winget_checkbox)
        config_layout.addWidget(self.choco_checkbox)
        body_layout.addWidget(config_group)

        # Área de log
        log_group = QGroupBox("Log de Atualização")
        log_layout = QVBoxLayout(log_group)

        self.output_log = QTextEdit()
        self.output_log.setReadOnly(True)
        self.output_log.setPlaceholderText("O log de atualização aparecerá aqui...")
        self.output_log.setFont(QFont("Consolas", 10))

        log_layout.addWidget(self.output_log)
        body_layout.addWidget(log_group)

        # Adiciona espaço flexível no final
        body_layout.addItem(
            QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        self.main_layout.addWidget(scroll_area)

    def setup_footer(self):
        footer_frame = QFrame()
        footer_frame.setObjectName("footerFrame")
        footer_layout = QHBoxLayout(footer_frame)
        footer_layout.setContentsMargins(20, 10, 20, 10)

        self.status_label = QLabel("Pronto para atualizar")
        self.status_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.status_label.setFont(QFont("Segoe UI", 10))

        # Container para os botões
        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(10)

        # Botão de pausa
        self.pause_button = QPushButton("PAUSAR")
        self.pause_button.setFixedHeight(50)
        self.pause_button.setMinimumWidth(150)
        self.pause_button.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.pause_button.setEnabled(False)  # Inicialmente desabilitado

        # Botão de atualização
        self.update_button = QPushButton("INICIAR ATUALIZAÇÃO")
        self.update_button.setFixedHeight(50)
        self.update_button.setMinimumWidth(200)
        self.update_button.setFont(QFont("Segoe UI", 12, QFont.Bold))

        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.update_button)

        footer_layout.addWidget(self.status_label)
        footer_layout.addStretch()
        footer_layout.addWidget(button_container)
        self.main_layout.addWidget(footer_frame)

    def wrap_in_frame(self, widget):
        frame = QFrame()
        frame.setFrameShape(QFrame.NoFrame)
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(widget)
        return frame

    def apply_style(self):
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #1e1e1e;
                color: #e0e0e0;
            }

            #headerFrame {
                background-color: #252525;
                border-bottom: 1px solid #3a3a3a;
            }

            #footerFrame {
                background-color: #252525;
                border-top: 1px solid #3a3a3a;
            }

            QLabel {
                color: #e0e0e0;
            }

            QGroupBox {
                border: 1px solid #3a3a3a;
                border-radius: 6px;
                margin-top: 10px;
                padding-top: 12px;
                font-weight: bold;
                font-size: 14px;
                color: #ffffff;
                background-color: #252525;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px;
                color: #bbbbbb;
            }

            QTextEdit {
                background-color: #252525;
                border: 1px solid #3a3a3a;
                border-radius: 4px;
                padding: 8px;
                color: #e0e0e0;
                min-height: 300px;
            }

            QPushButton {
                background-color: #0078d7;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 12px 24px;
                font-size: 14px;
                font-weight: bold;
                min-width: 120px;
            }

            QPushButton:hover {
                background-color: #106ebe;
            }

            QPushButton:pressed {
                background-color: #005a9e;
            }

            QPushButton:disabled {
                background-color: #555555;
                color: #aaaaaa;
            }

            QCheckBox {
                color: #e0e0e0;
                font-size: 13px;
                padding: 8px;
            }

            QCheckBox::indicator {
                width: 18px;
                height: 18px;
            }

            QScrollArea {
                border: none;
            }

            /* Estilo especial para o botão de pausa quando ativo */
            QPushButton#pauseButton {
                background-color: #d77e00;
            }
            
            QPushButton#pauseButton:hover {
                background-color: #be6e10;
            }
            
            QPushButton#pauseButton:pressed {
                background-color: #9e5a00;
            }
        """
        )
        # Adiciona um ID para o botão de pausa para estilização especial
        self.pause_button.setObjectName("pauseButton")