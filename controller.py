from shapes import area,perimeter
from PyQt5.QtWidgets import *
from view import *
import math

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        '''
        Sets up the initial GUI conditions
        '''
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(350, 600)
        self.setImage("CalcSymbol.png")
        self.input1Line.setVisible(False)
        self.input2Line.setVisible(False)
        self.input3Line.setVisible(False)
        self.input1Label.setVisible(False)
        self.input2Label.setVisible(False)
        self.input3Label.setVisible(False)
        self.circleButton.clicked.connect(lambda: self.setUI())
        self.rectangleButton.clicked.connect(lambda: self.setUI())
        self.squareButton.clicked.connect(lambda: self.setUI())
        self.triangleButton.clicked.connect(lambda: self.setUI())
        self.areaButton.clicked.connect(lambda: self.setUI())
        self.perimeterButton.clicked.connect(lambda: self.setUI())
        self.submitButton.clicked.connect(lambda: self.calculate())

    def setUI(self) -> None:
        '''
        Adjusts the UI depending on the which buttons are clicked
        :return: Does not return anything
        '''
        if self.areaButton.isChecked():
            if self.circleButton.isChecked():
                self.input1Line.setVisible(True)
                self.input1Label.setVisible(True)
                self.input1Label.setText("Radius:")
                self.input2Line.setVisible(False)
                self.input2Label.setVisible(False)
                self.input3Line.setVisible(False)
                self.input3Label.setVisible(False)
                self.setImage("circleSymbol.png")
            elif self.rectangleButton.isChecked():
                self.input1Line.setVisible(True)
                self.input1Label.setVisible(True)
                self.input1Label.setText("Length:")
                self.input2Line.setVisible(True)
                self.input2Label.setVisible(True)
                self.input2Label.setText("Width:")
                self.input3Line.setVisible(False)
                self.input3Label.setVisible(False)
                self.setImage("rectangleSymbol.png")
            elif self.squareButton.isChecked():
                self.input1Line.setVisible(True)
                self.input1Label.setVisible(True)
                self.input1Label.setText("Length:")
                self.input2Line.setVisible(False)
                self.input2Label.setVisible(False)
                self.input3Line.setVisible(False)
                self.input3Label.setVisible(False)
                self.setImage("squareSymbol.jpg")
            elif self.triangleButton.isChecked():
                self.input1Line.setVisible(True)
                self.input1Label.setVisible(True)
                self.input1Label.setText("Side 1:")
                self.input2Line.setVisible(True)
                self.input2Label.setVisible(True)
                self.input2Label.setText("Side 2:")
                self.input3Line.setVisible(False)
                self.input3Label.setVisible(False)
                self.setImage("triangleSymbol.jpg")
        elif self.perimeterButton.isChecked():
            if self.circleButton.isChecked():
                self.input1Line.setVisible(True)
                self.input1Label.setVisible(True)
                self.input1Label.setText("Radius:")
                self.input2Line.setVisible(False)
                self.input2Label.setVisible(False)
                self.input3Line.setVisible(False)
                self.input3Label.setVisible(False)
                self.setImage("circleSymbol.png")
            elif self.rectangleButton.isChecked():
                self.input1Line.setVisible(True)
                self.input1Label.setVisible(True)
                self.input1Label.setText("Length:")
                self.input2Line.setVisible(True)
                self.input2Label.setVisible(True)
                self.input2Label.setText("Width:")
                self.input3Line.setVisible(False)
                self.input3Label.setVisible(False)
                self.setImage("rectangleSymbol.png")
            elif self.squareButton.isChecked():
                self.input1Line.setVisible(True)
                self.input1Label.setVisible(True)
                self.input1Label.setText("Length:")
                self.input2Line.setVisible(False)
                self.input2Label.setVisible(False)
                self.input3Line.setVisible(False)
                self.input3Label.setVisible(False)
                self.setImage("squareSymbol.jpg")
            elif self.triangleButton.isChecked():
                self.input1Line.setVisible(True)
                self.input1Label.setVisible(True)
                self.input1Label.setText("Side 1:")
                self.input2Line.setVisible(True)
                self.input2Label.setVisible(True)
                self.input2Label.setText("Side 2:")
                self.input3Line.setVisible(True)
                self.input3Label.setVisible(True)
                self.input3Label.setText("Side 3:")
                self.setImage("triangleSymbol.jpg")

    def setImage(self, file: str) -> None:
        '''
        Accepts an image file and uses it to set the pixmap image in the GUI
        :param file: Image file for the pixmap to interpret
        :return: Does not return anything
        '''
        self.current_file = file
        pixmap = QtGui.QPixmap(self.current_file)
        pixmap = pixmap.scaled(self.imageLabel.width(), self.imageLabel.width())
        self.imageLabel.setPixmap(pixmap)

    def calculate(self) -> None:
        '''
        Determines which calculation to make (Area/Perimeter)
        :return: Does not return anything
        '''
        if self.areaButton.isChecked():
            self.calculateArea()
        elif self.perimeterButton.isChecked():
            self.calculatePerimeter()

    def calculateArea(self) -> None:
        '''
        Calculates the area of a given shape with given conditions
        :return: Does not return anything
        '''
        if self.circleButton.isChecked():
            radius = float(self.input1Line.text())
            if radius < 0:
                self.outputLabel.setText("Enter a positive number!")
            else:
                area = math.pi * radius ** 2
                self.outputLabel.setText(f'Circle area = {area:.2f}')
        elif self.rectangleButton.isChecked():
            length = float(self.input1Line.text())
            if length < 0:
                self.outputLabel.setText("Enter positive numbers!")
            else:
                width = float(self.input2Line.text())
                if width < 0:
                    self.outputLabel.setText("Enter positive numbers!")
                else:
                    area = length * width
                    self.outputLabel.setText(f'Rectangle area = {area:.2f}')
        elif self.squareButton.isChecked():
            length = float(self.input1Line.text())
            if length < 0:
                self.outputLabel.setText("Enter positive numbers!")
            else:
                area = length ** 2
                self.outputLabel.setText(f'Square area = {area:.2f}')
        elif self.triangleButton.isChecked():
            side1 = float(self.input1Line.text())
            if side1 < 0:
                self.outputLabel.setText("Enter positive numbers!")
            else:
                side2 = float(self.input2Line.text())
                if side2 < 0:
                    self.outputLabel.setText("Enter positive numbers!")
                else:
                    area = (side1 * side2) / 2
                    self.outputLabel.setText(f'Triangle area = {area:.2f}')

    def calculatePerimeter(self) -> None:
        '''
        Calculates the perimeter of a given shape with given conditions
        :return: Does not return anything
        '''
        if self.circleButton.isChecked():
            radius = float(self.input1Line.text())
            if radius < 0:
                self.outputLabel.setText("Enter a positive number!")
            else:
                perimeter = 2 * math.pi * radius
                self.outputLabel.setText(f'Circle perimeter = {perimeter:.2f}')
        elif self.rectangleButton.isChecked():
            length = float(self.input1Line.text())
            if length < 0:
                self.outputLabel.setText("Enter positive numbers!")
            else:
                width = float(self.input2Line.text())
                if width < 0:
                    self.outputLabel.setText("Enter positive numbers!")
                else:
                    perimeter = (2 *length) + (2 * width)
                    self.outputLabel.setText(f'Rectangle perimeter = {perimeter:.2f}')
        elif self.squareButton.isChecked():
            length = float(self.input1Line.text())
            if length < 0:
                self.outputLabel.setText("Enter positive numbers!")
            else:
                perimeter = length * 4
                self.outputLabel.setText(f'Square perimeter = {perimeter:.2f}')
        elif self.triangleButton.isChecked():
            side1 = float(self.input1Line.text())
            if side1 < 0:
                self.outputLabel.setText("Enter positive numbers!")
            else:
                side2 = float(self.input2Line.text())
                if side2 < 0:
                    self.outputLabel.setText("Enter positive numbers!")
                else:
                    side3 = float(self.input3Line.text())
                    if side3 < 0:
                        self.outputLabel.setText("Enter positive numbers!")
                    else:
                        perimeter = side1 + side2 + side3
                        self.outputLabel.setText(f'Triangle perimeter = {perimeter:.2f}')