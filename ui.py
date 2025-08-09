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
    QProgressBar,
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QIcon, QPixmap


class RavenizerUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ravenizer - Atualizador Windows")
        self.setGeometry(100, 100, 1000, 700)
        self.setMinimumSize(800, 600)

        # Usando ícone padrão do sistema
        self.setWindowIcon(QIcon.fromTheme("system-software-update"))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

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
        header_layout.setContentsMargins(20, 20, 20, 20)
        header_layout.setSpacing(15)

        # Logo e título
        title_container = QHBoxLayout()
        title_container.setContentsMargins(0, 0, 0, 0)
        title_container.setSpacing(15)

        # Usando ícone padrão do sistema
        logo_label = QLabel()
        logo_icon = QIcon.fromTheme("system-software-update")
        if not logo_icon.isNull():
            logo_pixmap = logo_icon.pixmap(40, 40)
            logo_label.setPixmap(logo_pixmap)
            title_container.addWidget(logo_label)

        title_text = QVBoxLayout()
        title_text.setContentsMargins(0, 0, 0, 0)
        title_text.setSpacing(5)

        self.title_label = QLabel("Ravenizer Updater")
        self.title_label.setFont(QFont("Segoe UI", 18, QFont.Bold))

        self.subtitle_label = QLabel("Analisando seus aplicativos")
        self.subtitle_label.setFont(QFont("Segoe UI", 10))

        title_text.addWidget(self.title_label)
        title_text.addWidget(self.subtitle_label)
        title_container.addLayout(title_text)
        title_container.addStretch()

        header_layout.addLayout(title_container)

        # Checkboxes dos gerenciadores de pacotes
        self.manager_checkboxes = QHBoxLayout()
        self.manager_checkboxes.setContentsMargins(0, 0, 0, 0)
        self.manager_checkboxes.setSpacing(15)

        # Todos os ícones das checkboxes serão iguais ao da checkbox do Scoop ("utilities-terminal")
        scoop_icon_name = "utilities-terminal"
        self.winget_checkbox = self.create_manager_checkbox("Winget", scoop_icon_name)
        self.choco_checkbox = self.create_manager_checkbox(
            "Chocolatey", scoop_icon_name
        )
        self.scoop_checkbox = self.create_manager_checkbox("Scoop", scoop_icon_name)
        self.npackd_checkbox = self.create_manager_checkbox("Npackd", scoop_icon_name)

        self.manager_checkboxes.addWidget(self.winget_checkbox)
        self.manager_checkboxes.addWidget(self.choco_checkbox)
        self.manager_checkboxes.addWidget(self.scoop_checkbox)
        self.manager_checkboxes.addWidget(self.npackd_checkbox)
        self.manager_checkboxes.addStretch()

        header_layout.addLayout(self.manager_checkboxes)
        self.main_layout.addWidget(header_frame)

    def create_manager_checkbox(self, text, icon_name):
        checkbox = QCheckBox(text)
        checkbox.setChecked(True)
        checkbox.setFont(QFont("Segoe UI", 9))

        # Todos os ícones das checkboxes serão iguais ao da checkbox do Scoop ("utilities-terminal")
        icon = QIcon.fromTheme("utilities-terminal")
        if icon.isNull():
            # Fallback para ícone genérico se o tema não tiver o ícone específico
            icon = QIcon.fromTheme("package-x-generic")

        checkbox.setIcon(icon)
        checkbox.setIconSize(QSize(20, 20))

        # Estilo adicional para os checkboxes
        checkbox.setStyleSheet(
            """
            QCheckBox {
                spacing: 8px;
                padding: 8px 12px;
                background-color: #2a2a2a;
                border-radius: 6px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
            }
            QCheckBox:hover {
                background-color: #333333;
            }
            QCheckBox::indicator:checked {
                background-color: #4CAF50;
            }
            QCheckBox::indicator:unchecked {
                background-color: #555555;
            }
        """
        )

        return checkbox

    def setup_body(self):
        body_frame = QFrame()
        body_frame.setObjectName("bodyFrame")
        body_layout = QVBoxLayout(body_frame)
        body_layout.setContentsMargins(20, 20, 20, 20)
        body_layout.setSpacing(20)

        # Seção de progresso
        progress_group = QGroupBox("Progresso da Atualização")
        progress_layout = QVBoxLayout(progress_group)
        progress_layout.setContentsMargins(15, 15, 15, 15)
        progress_layout.setSpacing(15)

        self.progress_label = QLabel("Preparando para atualização automática")
        self.progress_label.setFont(QFont("Segoe UI", 10))

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setFixedHeight(10)

        self.status_label = QLabel("0/0 apps")
        self.status_label.setFont(QFont("Segoe UI", 9))
        self.status_label.setAlignment(Qt.AlignRight)

        progress_layout.addWidget(self.progress_label)
        progress_layout.addWidget(self.progress_bar)
        progress_layout.addWidget(self.status_label)
        body_layout.addWidget(progress_group)

        # Área de log
        log_group = QGroupBox("Detalhes da Atualização")
        log_layout = QVBoxLayout(log_group)
        log_layout.setContentsMargins(10, 15, 10, 10)

        self.output_log = QTextEdit()
        self.output_log.setReadOnly(True)
        self.output_log.setPlaceholderText("O log de atualização aparecerá aqui...")
        self.output_log.setFont(QFont("Consolas", 9))

        log_layout.addWidget(self.output_log)
        body_layout.addWidget(log_group)

        # Espaço flexível no final
        body_layout.addItem(
            QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )
        self.main_layout.addWidget(body_frame)

    def setup_footer(self):
        footer_frame = QFrame()
        footer_frame.setObjectName("footerFrame")
        footer_layout = QHBoxLayout(footer_frame)
        footer_layout.setContentsMargins(20, 15, 20, 15)

        # Botão de pausar
        self.pause_button = QPushButton("PAUSAR")
        self.pause_button.setFixedHeight(50)
        self.pause_button.setMinimumWidth(150)
        self.pause_button.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.pause_button.setEnabled(False)  # Inicialmente desabilitado
        self.pause_button.setObjectName("pauseButton")  # Para estilização

        self.update_button = QPushButton("INICIAR ATUALIZAÇÃO")
        self.update_button.setFixedHeight(50)
        self.update_button.setMinimumWidth(250)
        self.update_button.setFont(QFont("Segoe UI", 12, QFont.Bold))

        # Adicionando ícones aos botões
        pause_icon = QIcon.fromTheme("media-playback-pause")
        if not pause_icon.isNull():
            self.pause_button.setIcon(pause_icon)
            self.pause_button.setIconSize(QSize(24, 24))

        update_icon = QIcon.fromTheme("system-software-update")
        if not update_icon.isNull():
            self.update_button.setIcon(update_icon)
            self.update_button.setIconSize(QSize(24, 24))

        footer_layout.addStretch()
        footer_layout.addWidget(self.pause_button)
        footer_layout.addWidget(self.update_button)
        self.main_layout.addWidget(footer_frame)

    def apply_style(self):
        self.setStyleSheet(
            """
            /* Main window */
            QMainWindow {
                background-color: #121212;
                color: #e0e0e0;
            }

            /* Header */
            #headerFrame {
                background-color: #1a1a1a;
                border-bottom: 1px solid #2a2a2a;
            }

            /* Body */
            #bodyFrame {
                background-color: #121212;
                border: none;
            }

            /* Footer */
            #footerFrame {
                background-color: #1a1a1a;
                border-top: 1px solid #2a2a2a;
            }

            /* Labels */
            QLabel {
                color: #e0e0e0;
            }

            /* Group boxes */
            QGroupBox {
                border: 1px solid #2a2a2a;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 15px;
                font-weight: bold;
                font-size: 12px;
                color: #4CAF50;
                background-color: #1a1a1a;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
                color: #4CAF50;
            }

            /* Text edit / log */
            QTextEdit {
                background-color: #1a1a1a;
                border: 1px solid #2a2a2a;
                border-radius: 6px;
                padding: 8px;
                color: #e0e0e0;
                min-height: 200px;
                font-family: Consolas;
            }

            /* Buttons */
            QPushButton {
                background-color: #2E7D32;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-size: 11px;
                font-weight: bold;
                min-width: 80px;
            }

            QPushButton:hover {
                background-color: #388E3C;
            }

            QPushButton:pressed {
                background-color: #1B5E20;
            }

            QPushButton:checked {
                background-color: #1B5E20;
                border: 1px solid #4CAF50;
            }

            QPushButton:disabled {
                background-color: #424242;
                color: #757575;
            }

            /* Main action button */
            QPushButton[text="INICIAR ATUALIZAÇÃO"] {
                background-color: #4CAF50;
                font-size: 14px;
                min-width: 200px;
            }

            QPushButton[text="INICIAR ATUALIZAÇÃO"]:hover {
                background-color: #66BB6A;
            }

            QPushButton[text="INICIAR ATUALIZAÇÃO"]:pressed {
                background-color: #388E3C;
            }

            /* Pause button style */
            QPushButton#pauseButton {
                background-color: #FF9800;
                color: white;
                min-width: 120px;
            }

            QPushButton#pauseButton:hover {
                background-color: #FB8C00;
            }

            QPushButton#pauseButton:pressed {
                background-color: #F57C00;
            }

            QPushButton#pauseButton:disabled {
                background-color: #424242;
                color: #757575;
            }

            /* Progress bar */
            QProgressBar {
                border: 1px solid #2a2a2a;
                border-radius: 5px;
                background-color: #1a1a1a;
                text-align: center;
            }

            QProgressBar::chunk {
                background-color: #4CAF50;
                border-radius: 4px;
            }

            /* Scroll area */
            QScrollArea {
                border: none;
            }

            QScrollBar:vertical {
                border: none;
                background: #1a1a1a;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }

            QScrollBar::handle:vertical {
                background: #424242;
                min-height: 20px;
                border-radius: 5px;
            }

            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """
        )


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = RavenizerUI()
    window.show()
    sys.exit(app.exec())
