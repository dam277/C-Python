from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QToolButton, QLineEdit, QWidget
import random
import sys

from Button import Button

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QPushButton("Click me!")
        self.text = QLabel("Hello World",
                                     alignment=Qt.AlignCenter)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        newButton = Button()
        newButton.clicked.connect(lambda btn: print(f"Button clicked with {btn}"))
        self.layout.addWidget(newButton)

        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QApplication([])

    # widget = MyWidget()
    # widget.resize(800, 600)
    # widget.show()
    label = QLabel("Hello World", alignment=Qt.AlignCenter)
    label.resize(400, 300)
    label.show()

    button = QToolButton()
    line_edit = QLineEdit()

    button.setText("Clear")
    button.show()
    line_edit.show()
    connection = button.clicked.connect(lambda: (line_edit.clear(), print("Cleared!")))

    sys.exit(app.exec())