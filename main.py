import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore

class CustomWidget(qtw.QWidget):
	def __init__(self):
		super().__init__()
		self.init_Ui()

	def init_Ui(self):
		self.setGeometry(180, 180, 300, 300)
		self.setWindowTitle("Button and Events")

		self.label = qtw.QLabel(self)
		self.label.setText("Hello")
		self.label.move(10, 10)
		
		self.button = qtw.QPushButton(self)
		self.button.setText("Click Me")
		self.button.move(10, 50)

		self.button.clicked.connect(self.button_clicked)

		self.show()
		
	def button_clicked(self):
		self.label.setText("Button clicked")
		self.button.adjustSize()

def run():
	app = qtw.QApplication(sys.argv)
	w = CustomWidget()
	sys.exit(app.exec_())
	

if __name__ == "__main__":
	run()
