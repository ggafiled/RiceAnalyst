import ControlActivity
import os
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    RiceAnalyst = QtWidgets.QMainWindow()
    ui = ControlActivity.Ui_RiceAnalyst()
    ui.setupUi(RiceAnalyst)
    root = os.path.dirname(os.path.realpath(__file__))
    RiceAnalyst.setWindowIcon(QtGui.QIcon(root + os.path.sep + "img/icons/32x32.ico"))
    RiceAnalyst.show()
    sys.exit(app.exec_())
