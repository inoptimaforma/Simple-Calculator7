from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout

if __name__ == "__main__":
    application = QApplication([])
    window = CalculatorWindow()
    window.show()
    app.exec_()