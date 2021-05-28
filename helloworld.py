print(len(locals()))
from PyQt5.QtWidgets import *
print(len(locals()))
# Create application object first
app = QApplication([])

# Widget is an any item you see on the screen i.e., button, label, text input
# menu are all widgets.
# QWidget is jst blank panel/window.
# windowTitle is a property of the widget .
w = QWidget(windowTitle='hello world')

# Show method of the widget.
w.show()

app.exec_()
