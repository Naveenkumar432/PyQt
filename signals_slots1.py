import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

class MyWidget(qtw.QWidget):
	def __init__(self):
		super().__init__()

		self.init_Ui()

	def init_Ui(self):
		self.lcd = qtw.QLCDNumber(self)
		self.sld = qtw.QSlider(qtc.Qt.Horizontal, self)

		vbox = qtw.QVBoxLayout()
		vbox.addWidget(self.lcd)
		vbox.addWidget(self.sld)

		self.setLayout(vbox)

		self.sld.valueChanged.connect(self.lcd.display)

		self.setGeometry(100, 100, 250, 150)
		self.setWindowTitle("Signal and Slot example")

		self.show()

def run():
	app = qtw.QApplication(sys.argv)
	w = MyWidget()
	sys.exit(app.exec_())

if __name__ == "__main__":
	run()
