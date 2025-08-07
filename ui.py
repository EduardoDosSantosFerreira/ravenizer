from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QProgressBar,
    QTextEdit,
    QGroupBox,
    QFrame,
    QScrollArea,
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
        header_layout = QVBoxLayout(header_frame)

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
        scroll_content = QWidget()
        body_layout = QVBoxLayout(scroll_content)
        scroll_area.setWidget(scroll_content)

        # Descrição simplificada
        self.desc_label = QLabel(
            "Este software irá atualizar automaticamente seu sistema Windows utilizando:\n\n"
            "• winget: Para atualização de aplicativos e sistema\n"
            "• Chocolatey: Para atualização de programas instalados"
        )
        self.desc_label.setWordWrap(True)
        self.desc_label.setAlignment(Qt.AlignCenter)
        body_layout.addWidget(self.wrap_in_frame(self.desc_label))

        # Seção de progresso (simplificada)
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setFormat("%p% - Atualizando...")

        progress_group = QGroupBox("Progresso da Atualização")
        progress_layout = QVBoxLayout(progress_group)
        progress_layout.addWidget(self.progress_bar)
        body_layout.addWidget(progress_group)

        # Área de log
        self.output_log = QTextEdit()
        self.output_log.setReadOnly(True)
        self.output_log.setPlaceholderText("O log de atualização aparecerá aqui...")
        self.output_log.setFont(QFont("Consolas", 10))

        log_group = QGroupBox("Log de Atualização")
        log_layout = QVBoxLayout(log_group)
        log_layout.addWidget(self.output_log)
        body_layout.addWidget(log_group)

        self.main_layout.addWidget(scroll_area)

    def setup_footer(self):
        footer_frame = QFrame()
        footer_layout = QHBoxLayout(footer_frame)

        self.status_label = QLabel("Pronto para atualizar")
        self.status_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.update_button = QPushButton("INICIAR ATUALIZAÇÃO COMPLETA")
        self.update_button.setFixedHeight(50)
        self.update_button.setMinimumWidth(200)

        footer_layout.addWidget(self.status_label)
        footer_layout.addStretch()
        footer_layout.addWidget(self.update_button)
        self.main_layout.addWidget(footer_frame)

    def wrap_in_frame(self, widget):
        frame = QFrame()
        layout = QVBoxLayout(frame)
        layout.addWidget(widget)
        return frame

    def apply_style(self):
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #1e1e1e;
                color: #e0e0e0;
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

            QProgressBar {
                border: 1px solid #3a3a3a;
                border-radius: 5px;
                text-align: center;
                height: 24px;
                font-size: 12px;
                color: white;
                background-color: #2d2d2d;
            }

            QProgressBar::chunk {
                background-color: #0078d7;
                border-radius: 4px;
                margin: 1px;
            }
        """
        )
