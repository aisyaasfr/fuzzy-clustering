"""Application entry point for the Fuzzy C-Means desktop interface."""

import sys

from PyQt6.QtWidgets import QApplication

from src.pages.main import MainWindow
from src.utils.font import Fonts


def main() -> int:
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    Fonts().load_fonts()

    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
