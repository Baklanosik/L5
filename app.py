import sys

from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QHBoxLayout,
    QPushButton,
    QSpinBox,
    QWidget,
)


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("L5")
        self.setMinimumWidth(200)

        self.spin_box = QSpinBox()
        self.spin_box.setRange(10, 10000)
        self.spin_box.setReadOnly(True)
        self.spin_box.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spin_box.setStyleSheet("background-color: lightgray;")

        self.toggle_button = QPushButton("start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self.button_method)

        layout = QHBoxLayout(self)
        layout.addWidget(self.spin_box)
        layout.addWidget(self.toggle_button)

    def button_method(self, is_running: bool) -> None:
        self.toggle_button.setText("stop" if is_running else "start")


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
