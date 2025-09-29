from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Button(QWidget):
    clicked = Signal(int)  # emit an int for the mouse button

    def __init__(self, text="Custom Button"):
        super().__init__()
        self.setFixedSize(100, 50)

        # ensure stylesheet background is used
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: lightblue; border: 1px solid black;")

        # use a layout so the label is positioned and centered
        self._label = QLabel(text)
        self._label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._label)

    def mousePressEvent(self, event):
        self.clicked.emit(int(event.button()))