import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):
	# Custom signals
	authenticated = qtc.pyqtSignal(str)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# Creating widgets
		self.username_label = qtw.QLabel("Username")
		self.password_label = qtw.QLabel("Password")

		self.username_input = qtw.QLineEdit()
		self.password_input = qtw.QLineEdit()
		self.password_input.setEchoMode(qtw.QLineEdit.Password)

		self.cancel_button = qtw.QPushButton('Cancel')
		self.submit_button = qtw.QPushButton('Login')

		# Anotherway using QForm
		layout = qtw.QFormLayout()
		layout.addRow('Username', self.username_input)
		layout.addRow('Password', self.password_input)

		button_widget = qtw.QWidget()
		button_widget.setLayout(qtw.QHBoxLayout())
		button_widget.layout().addWidget(self.cancel_button)
		button_widget.layout().addWidget(self.submit_button)
		layout.addRow('', button_widget)

		self.setLayout(layout)

		self.cancel_button.clicked.connect(self.close)
		self.submit_button.clicked.connect(self.authentication)

		self.username_input.textChanged.connect(self.set_button_text)
		
		self.authenticated.connect(self.user_logged_in)

		self.setGeometry(100, 100, 250, 100)
		self.show()

	# @qtc.pyqtSlot(str)
	def set_button_text(self, text):
		if text:
			self.submit_button.setText(f"Log in {text}")
			self.submit_button.adjustSize()
		else:
			self.submit_button.setText("Log in")

	def authentication(self):
		username = self.username_input.text()
		password = self.password_input.text()

		if username == 'user' and password == 'pass':
			qtw.QMessageBox.information(self, "Success", "Your logged in")
			
			self.authenticated.emit(username)
		else:
			qtw.QMessageBox.critical(self, 'Failed', "Your not logged in")

	def user_logged_in(self, username):
		qtw.QMessageBox.information(self, "Logged in", f'{username} is logged in')

if __name__ == "__main__":
	# Create application object first
	app = qtw.QApplication(sys.argv)
	w = MainWindow()
	sys.exit(app.exec_())