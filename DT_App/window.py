import sys
from PyQt5.QtWidgets import *
from parse import fit_to_ascii
from datab import insert_to_db
from select_2 import *


class Window(QWidget):
    def __init__(self):

        super().__init__()
        self.setWindowTitle("Battery statistics")
        self.resize(336, 164)

        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.addTab(self.second_Tab_UI(), "Statisztikák")
        tabs.addTab(self.first_Tab_UI(), "File feltöltése")
        layout.addWidget(tabs)

    def first_Tab_UI(self):
        """CREATE FIRST TAB"""
        elsoTab = QWidget()
        layout = QVBoxLayout()

        button = QPushButton(elsoTab)
        button.setText("Fájl kiválasztása")
        button.clicked.connect(first_Tab_button_clicked)

        text = QLabel(elsoTab)
        text.setText("Kiválaszthat egy fájlt, amit fel szretne tölteni az adatbázisba")

        layout.addWidget(text)
        layout.addWidget(button)

        elsoTab.setLayout(layout)

        return elsoTab

    def second_Tab_UI(self):
        """CREATE SECOND TAB"""

        secondTab = QWidget()
        layout = QVBoxLayout()

        self.label = QLabel(secondTab)
        self.label.setText("Különböző modellek átlagos fogyasztásai")

        self.text = QLabel(secondTab)
        self.text.setText("Válasszon egy modellt!")

        self.pageCombo = QComboBox()
        self.items = select_models()
        self.pageCombo.addItem("Típusok")
        self.pageCombo.addItems(self.items)
        self.pageCombo.activated.connect(self.switchPage)

        self.stackedLayout = QStackedLayout()

        layout.addWidget(self.label)
        layout.addWidget(self.pageCombo)
        layout.addWidget(self.text)
        layout.addLayout(self.stackedLayout)

        secondTab.setLayout(layout)

        return secondTab

    def switchPage(self):
        index = self.pageCombo.currentIndex()
        self.stackedLayout.setCurrentIndex(self.pageCombo.currentIndex())
        if index != 0:
            self.text.setText(
                "A(z) {} átlag fogyasztása: {} \nHr off: {}\nGPS off: {}\nHr + GPS off: {}\nHr + GPS on: {}".format(
                    self.items[index - 1],
                    specific_AVG(
                        self.items[index - 1],
                    ),
                    specific_HR_GPS(self.items[index - 1], 0, 1),
                    specific_HR_GPS(self.items[index - 1], 1, 0),
                    specific_HR_GPS(self.items[index - 1], 0, 0),
                    specific_HR_GPS(self.items[index - 1], 1, 1),
                )
            )
        else:
            self.text.setText("Válasszon egy modellt!")


def first_Tab_button_clicked():
    # akku_stat()
    # fit_to_ascii()
    insert_to_db()
    # print("passzolok")
    # pass


def createWindow():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    createWindow()
