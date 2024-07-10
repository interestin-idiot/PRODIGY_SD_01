from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIntValidator
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QMessageBox, QWidget, QHBoxLayout, QVBoxLayout, QLabel,QLineEdit

class testwidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Temperature Converter")
        self.setGeometry(0,0,350,100)

        label = QLabel("Input :")
        
        self.line_edit = QLineEdit(self)

        FButton = QPushButton("Farenheit")
        FButton.clicked.connect(self.ftock)
        KButton = QPushButton("Celsius")
        KButton.clicked.connect(self.ktocf)
        CButton = QPushButton("Kelvin")
        CButton.clicked.connect(self.ctokf)

        inputype_label = QLabel("Select Input Type : ")


        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)


        h2_layout = QHBoxLayout()
        h2_layout.addWidget(FButton)
        h2_layout.addWidget(KButton)
        h2_layout.addWidget(CButton)

        self.output_textLabel = QLabel("")
        self.output_textLabel2 = QLabel("")

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(inputype_label)
        v_layout.addLayout(h2_layout)
        v_layout.addWidget(self.output_textLabel)
        v_layout.addWidget(self.output_textLabel2)
        self.setLayout(v_layout)
    

    def commonStub(self):
        print("Common PlaceHolder")


    def ftock(self): 
        try:
            fahrenheit = float(self.line_edit.text())
            celsius = (fahrenheit - 32) * 5.0/9.0
            kelvin = (fahrenheit - 32) * 5.0/9.0 + 273.15
            self.output_textLabel.setText(f"Celsius: {celsius:.2f}.C")
            self.output_textLabel2.setText(f"Kelvin : {kelvin:.2f}. K")
        except ValueError:
            QMessageBox.warning(self, "Conversion Error", "The input is not a valid number.")



    def ktocf(self):
        try:
            kelvin = float(self.line_edit.text())
            celsius = kelvin - 273.15
            farenheit = (kelvin - 273.15) * 9.0/5.0 + 32
            self.output_textLabel.setText(f"Celsius : {celsius:.2f}. C")
            self.output_textLabel2.setText(f"farenheit : {farenheit:.2f}. F")
        except ValueError:
            QMessageBox.warning(self, "Conversion Error", "The input is not a valid number.")



    def ctokf(self):
        try :
            celsius = float(self.line_edit.text())
            kelvin = celsius + 273.15
            fahrenheit = (celsius * 9.0/5.0) + 32
            self.output_textLabel.setText(f"Kelvin : {kelvin:.2f}. K")
            self.output_textLabel2.setText(f"Farenheit : {fahrenheit:.2f}. F")
        except ValueError:
            QMessageBox.warning(self, "Conversion Error", "The input is not a valid number.")
        




        



    