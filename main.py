import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont

def on_button_click():
    label.setText("Button clicked!")

app = QApplication(sys.argv)

# Create a window
window = QWidget()
window.setWindowTitle('EDesign Software: By NV Makoala - 22919732')
window.setGeometry(500, 100, 800, 800)

# Create layout
layout = QVBoxLayout()

# Create a label and a button

#Font of the label
font = QFont("Times", 60)

label = QLabel('Hello World!')
label.setFont(font)
label.setGeometry(100, 100, 100, 100)
# button = QPushButton('Click me')

# Connect button click event to function
# button.clicked.connect(on_button_click)

# Add widgets to layout
layout.addWidget(label)
# layout.addWidget(button)

# Set layout for the window
window.setLayout(layout)

# Show the window
window.show()

# Start the application event loop
sys.exit(app.exec_())
