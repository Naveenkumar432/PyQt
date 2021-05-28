import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc # for signals/slots
from PyQt5 import QtGui as qtg # For changing font color etc

from login_form import Ui_Login_Form

class MainWindow(qtw.QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.ui = Ui_Login_Form()
		self.ui.setupUi(self)

		self.show()

if __name__ == "__main__":
	# Create application object first
	app = qtw.QApplication(sys.argv)
	w = MainWindow()
	sys.exit(app.exec_())


# Widget is an any item you see on the screen i.e., button, label, text input
# menu are all widgets.
# QWidget is jst blank panel/window.
# windowTitle is a property of the widget .
# w = qtw.QWidget(windowTitle='hello world')

# # Show method of the widget.
# w.show()


