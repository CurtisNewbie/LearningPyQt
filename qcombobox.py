from PyQt5.QtWidgets import *
import sys

# AppWithComboBox is an subclass of QDialog
class AppWithComboBox(QDialog):

    # constructor that accepts variable arguments of string
    def __init__(self, *names : str):
        super(AppWithComboBox, self).__init__()
        print("Creating AppWithCombox")

        # widgets
        self.label = QLabel("ComboBoxDemo")
        self.comboBox = QComboBox()
        self.comboBox.addItems(names)

        # layouts
        self.mainLayout = QGridLayout()
        self.hboxLayout = QHBoxLayout()

        # hboxLayout at row: 0, col: 0, with row span: 2, col span: 1
        self.mainLayout.addLayout(self.hboxLayout, 0, 0, 2, 1)

        # put widgets in hbox
        self.putIntoLayout(self.hboxLayout, self.label, self.comboBox)

        # set the layout to this dialog
        self.setLayout(self.mainLayout)

    # Add the widget to the layout
    def putIntoLayout(self, hbox : QHBoxLayout, label : QLabel, comboBox : QComboBox):
        hbox.addWidget(label)
        hbox.addWidget(comboBox)


# create QApplication
app = QApplication([])
# create QDialog with combo box
dialog = AppWithComboBox("apple", "banana", "2077")
# display the QDialog
dialog.show()
# let the QApplication to do its job
app.exec_()
