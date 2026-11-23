import sys

from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSlider,
    QSizePolicy,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("L5")
        self.setMinimumWidth(200)

        self.counter = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_method)
        

        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 10000)
        self.spin_box.setReadOnly(True)
        self.spin_box.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spin_box.setStyleSheet("background-color: lightgray;")

        self.toggle_button = QPushButton("start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self.button_method)

        layout = QHBoxLayout(self)
        layout.addWidget(self.spin_box)
        layout.addWidget(self.toggle_button)

        right_layout = QVBoxLayout()
        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setRange(0, 255)
        self.slider.valueChanged.connect(self.slider_method)
        right_layout.addWidget(self.slider)

        self.secondary_spin_box = QSpinBox()
        self.secondary_spin_box.setRange(0, 255)
        self.secondary_spin_box.setReadOnly(True)
        self.secondary_spin_box.setButtonSymbols(
            QAbstractSpinBox.ButtonSymbols.NoButtons
        )
        self.secondary_spin_box.setStyleSheet("background-color: lightgray;")
        right_layout.addWidget(self.secondary_spin_box)
        layout.addLayout(right_layout)

        self.color_box = QLabel()
        self.color_box.setMinimumWidth(100)
        self.color_box.setSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        layout.addWidget(self.color_box)

        self.color_box.setStyleSheet('background-color: rgb(0, 0, 0)')

    def button_method(self, is_running: bool):
        self.toggle_button.setText("stop" if is_running else "start")
        if is_running:
            self.counter = 0
            self.timer.start(10)
        else:
            self.timer.stop()

    def timer_method(self):
        self.counter += 1
        self.spin_box.setValue(self.counter)
        if self.counter == 500:
            self.timer.stop()
            self.toggle_button.setChecked(False)

    def slider_method(self):
        value = self.slider.value()
        self.secondary_spin_box.setValue(value)
        self.color_box.setStyleSheet(f'background-color: rgb({value}, {value}, {value})')



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
