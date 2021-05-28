# https://github.com/alandmoore/PyQt-Videos-Examples/tree/master/QtResourceFiles
import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QMainWindow):
	def __init__(self):
		super().__init__()
		# Main code goes here
		self.textedit = qtw.QTextEdit()
		self.setCentralWidget(self.textedit)

		# Menubar
		menubar = self.menuBar() # QMenubar
		file_menu = menubar.addMenu('File') #QMenu
		file_menu.addAction('Open', self.open_file)
		save_action = file_menu.addAction('save') #QAction
		file_menu.addSeparator()
		file_menu.addAction("Quit", self.close)


		save_action.triggered.connect(self.save_file)
		self.statusBar().showMessage("Welcome to  my editor", 2000)
		
		# Adding images
		# copy_icon = qtg.QIcon(qtg.QPixMap('copy.svg'))

		#toolbar
		edit_toolbar = self.addToolBar('Edit') # QToolBar
		# edit_toolbar.addAction(copy_icon, 'Copy', self.textedit.copy)
		edit_toolbar.addAction('Copy', self.textedit.copy)
		edit_toolbar.addAction('Paste', self.textedit.paste)
		edit_toolbar.addAction('Cut', self.textedit.cut)
		edit_toolbar.addAction('Undo', self.textedit.undo)
		edit_toolbar.addAction('Redo', self.textedit.redo)
		# Find main ui code
		self.show()

	def save_file(self):
		text = self.textedit.toPlainText()
		file_name, _ = qtw.QFileDialog.getSaveFileName()
		if file_name:
			with open(file_name, 'w') as handle:
				handle.write(text)
				self.statusBar().showMessage('save to {file_name}')

	def open_file(self):
		file_name, _ = qtw.QFileDialog.getOpenFileName()
		print(file_name)
		if file_name:
			with open(file_name, 'r') as handle:
				text = handle.read()
			self.textedit.clear()
			self.textedit.insertPlainText(text)
			self.textedit.moveCursor(qtg.QTextCursor.Start)
			self.statusBar().showMessage(f'Editing {file_name}')

if __name__ == "__main__":
	app = qtw.QApplication(sys.argv)
	w = MainWindow()
	sys.exit(app.exec_())