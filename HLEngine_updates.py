# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'content.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import git
import cv2

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

class HL_Updates(object):
    def updates(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(709, 53)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(52, 52, 52);"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(470, 10, 221, 27))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(49, 49, 49);\n"
"color: rgb(255, 255, 255);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 10, 451, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))

        self.pushButton.clicked.connect(self.update)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "HLEngine Updates", None))
        self.pushButton.setText(_translate("Dialog", "Update HL_Engine", None))

    def update(self):
        try:
            # git.Git("Updates/").clone("https://github.com/HLRobotics/QBee.git")
            # print("done downloading .....")
            git_dir = "../HL_Engine"
            self.progressBar.setProperty("value", 50)
            g = git.cmd.Git(git_dir)
            g.pull()
            self.progressBar.setProperty("value", 75)
            self.progressBar.setProperty("value", 100)
            print("HLEngine:done updating ......")
            img = cv2.imread('HLEngine.png')
            cv2.imshow('HLEngine updates', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        except:
            return ("HLEngine:cannot connect to cloud")


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = HL_Updates()
    ui.updates(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

