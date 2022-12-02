# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shapeFrame = QtWidgets.QFrame(self.centralwidget)
        self.shapeFrame.setGeometry(QtCore.QRect(25, 230, 300, 60))
        self.shapeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shapeFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.shapeFrame.setObjectName("shapeFrame")
        self.shapeLabel = QtWidgets.QLabel(self.shapeFrame)
        self.shapeLabel.setGeometry(QtCore.QRect(10, 10, 75, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shapeLabel.setFont(font)
        self.shapeLabel.setObjectName("shapeLabel")
        self.circleButton = QtWidgets.QRadioButton(self.shapeFrame)
        self.circleButton.setGeometry(QtCore.QRect(10, 30, 70, 20))
        self.circleButton.setObjectName("circleButton")
        self.rectangleButton = QtWidgets.QRadioButton(self.shapeFrame)
        self.rectangleButton.setGeometry(QtCore.QRect(70, 30, 70, 20))
        self.rectangleButton.setObjectName("rectangleButton")
        self.squareButton = QtWidgets.QRadioButton(self.shapeFrame)
        self.squareButton.setGeometry(QtCore.QRect(150, 30, 70, 20))
        self.squareButton.setObjectName("squareButton")
        self.triangleButton = QtWidgets.QRadioButton(self.shapeFrame)
        self.triangleButton.setGeometry(QtCore.QRect(220, 30, 70, 20))
        self.triangleButton.setObjectName("triangleButton")
        self.operationFrame = QtWidgets.QFrame(self.centralwidget)
        self.operationFrame.setGeometry(QtCore.QRect(25, 290, 300, 60))
        self.operationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.operationFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.operationFrame.setObjectName("operationFrame")
        self.operationLabel = QtWidgets.QLabel(self.operationFrame)
        self.operationLabel.setGeometry(QtCore.QRect(10, 10, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.operationLabel.setFont(font)
        self.operationLabel.setObjectName("operationLabel")
        self.areaButton = QtWidgets.QRadioButton(self.operationFrame)
        self.areaButton.setGeometry(QtCore.QRect(70, 30, 70, 20))
        self.areaButton.setObjectName("areaButton")
        self.perimeterButton = QtWidgets.QRadioButton(self.operationFrame)
        self.perimeterButton.setGeometry(QtCore.QRect(150, 30, 70, 20))
        self.perimeterButton.setObjectName("perimeterButton")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(75, 450, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.outputLabel.setText("")
        self.outputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(125, 520, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.imageLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(75, 10, 200, 200))
        self.imageLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.input1Line = QtWidgets.QLineEdit(self.centralwidget)
        self.input1Line.setGeometry(QtCore.QRect(125, 360, 200, 20))
        self.input1Line.setAlignment(QtCore.Qt.AlignCenter)
        self.input1Line.setObjectName("input1Line")
        self.input2Line = QtWidgets.QLineEdit(self.centralwidget)
        self.input2Line.setGeometry(QtCore.QRect(125, 390, 200, 20))
        self.input2Line.setAlignment(QtCore.Qt.AlignCenter)
        self.input2Line.setObjectName("input2Line")
        self.input1Label = QtWidgets.QLabel(self.centralwidget)
        self.input1Label.setGeometry(QtCore.QRect(25, 360, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input1Label.setFont(font)
        self.input1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.input1Label.setObjectName("input1Label")
        self.input2Label = QtWidgets.QLabel(self.centralwidget)
        self.input2Label.setGeometry(QtCore.QRect(25, 390, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input2Label.setFont(font)
        self.input2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.input2Label.setObjectName("input2Label")
        self.input3Label = QtWidgets.QLabel(self.centralwidget)
        self.input3Label.setGeometry(QtCore.QRect(25, 420, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input3Label.setFont(font)
        self.input3Label.setAlignment(QtCore.Qt.AlignCenter)
        self.input3Label.setObjectName("input3Label")
        self.input3Line = QtWidgets.QLineEdit(self.centralwidget)
        self.input3Line.setGeometry(QtCore.QRect(125, 420, 200, 20))
        self.input3Line.setAlignment(QtCore.Qt.AlignCenter)
        self.input3Line.setObjectName("input3Line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Area/Perimeter Calculator"))
        self.shapeLabel.setText(_translate("MainWindow", "Shapes:"))
        self.circleButton.setText(_translate("MainWindow", "Circle"))
        self.rectangleButton.setText(_translate("MainWindow", "Rectangle"))
        self.squareButton.setText(_translate("MainWindow", "Square"))
        self.triangleButton.setText(_translate("MainWindow", "Triangle"))
        self.operationLabel.setText(_translate("MainWindow", "Operation:"))
        self.areaButton.setText(_translate("MainWindow", "Area"))
        self.perimeterButton.setText(_translate("MainWindow", "Perimeter"))
        self.submitButton.setText(_translate("MainWindow", "Begin"))
        self.input1Label.setText(_translate("MainWindow", "TextLabel"))
        self.input2Label.setText(_translate("MainWindow", "TextLabel"))
        self.input3Label.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())