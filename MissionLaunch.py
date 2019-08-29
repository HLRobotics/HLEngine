#@Author:Akhil P Jacob
#HLRobotics-Automation

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(604, 72)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Graphics/dev.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(39, 39, 39);"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(140, 20, 331, 29))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(39, 39, 39);\n"
"color: rgb(255, 255, 255);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(480, 20, 95, 27))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(39, 39, 39);\n"
"color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 26, 111, 21))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))


        self.pushButton.clicked.connect(self.launchMission)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "HLEngine_MissionLaunch", None))
        self.pushButton.setText(_translate("Dialog", "Generate", None))
        self.label.setText(_translate("Dialog", "Path & Name", None))

    def launchMission(self):
        path=self.lineEdit.text()
        from xml.dom import minidom
        mydoc = minidom.parse('payload.xml')
        payload = mydoc.getElementsByTagName('payload')
        file = open(path, "a")
        for elem in payload:
            print(elem.firstChild.data)
            framework = elem.firstChild.data
            file.write(str(framework + "\n"))

        file.close()
        Dialog.close()



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

