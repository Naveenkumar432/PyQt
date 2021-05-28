import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# Creating widgets
		username_label = qtw.QLabel("Username")
		password_label = qtw.QLabel("Password")

		username_input = qtw.QLineEdit()
		password_input = qtw.QLineEdit()
		password_input.setEchoMode(qtw.QLineEdit.Password)

		cancel_button = qtw.QPushButton('Cancel')
		submit_button = qtw.QPushButton('Login')

		# One way to use
		# layout = qtw.QVBoxLayout()
		# username_layout = qtw.QHBoxLayout()
		# username_layout.addWidget(username_label)
		# username_layout.addWidget(username_input)
		# layout.addLayout(username_layout)
		
		# password_layout = qtw.QHBoxLayout()
		# password_layout.addWidget(password_label)
		# password_layout.addWidget(password_input)
		# layout.addLayout(password_layout)

		# Another way 
		# layout = qtw.QGridLayout()
		# layout.addWidget(username_label, 0, 0)
		# layout.addWidget(username_input, 0, 1)
		# layout.addWidget(password_label)
		# layout.addWidget(password_input)

		# Anotherway using QForm
		layout = qtw.QFormLayout()
		layout.addRow('Username', username_input)
		layout.addRow('Password', password_input)

		button_widget = qtw.QWidget()
		button_widget.setLayout(qtw.QHBoxLayout())
		button_widget.layout().addWidget(cancel_button)
		button_widget.layout().addWidget(submit_button)
		layout.addRow('', button_widget)

		self.setLayout(layout)
		
		self.show()

if __name__ == "__main__":
	# Create application object first
	app = qtw.QApplication(sys.argv)
	w = MainWindow()
	sys.exit(app.exec_())