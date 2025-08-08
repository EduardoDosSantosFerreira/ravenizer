import sys
from PySide6.QtWidgets import QApplication
from ui import RavenizerUI
from script import RavenizerLogic


def main():
    app = QApplication(sys.argv)

    # Configurar estilo
    app.setStyle("Fusion")

    # Criar e mostrar janela principal
    window = RavenizerUI()
    window.show()

    # Inicializar lógica
    logic = RavenizerLogic(window)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
