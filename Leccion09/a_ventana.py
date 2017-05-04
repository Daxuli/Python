import sys
from PyQt4.QtGui import *

a = QApplication(sys.argv)
w = QWidget()
btn = QPushButton("Button", w)
btn.move(100, 100)
btn.setToolTip("cierra el programa")
# btn.clicked.connect(lambda: print("a"))
w2 = QWidget()

w.resize(320, 240)
w2.resize(600, 400)

btn.clicked.connect(w2.show)
w.setWindowTitle("Titulo")

w.show()
# w2.show()
sys.exit(a.exec_())
