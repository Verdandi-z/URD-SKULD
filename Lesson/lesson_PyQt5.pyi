import sys
from PyQt5.QtWidgets import QApplication, QWidget

Interface = QApplication(sys.argv)
w = QWidget()
w.setGeometry(200,300,400,500)
w.setWindowTitle('TEST')
w.show()

sys.exit(Interface.exec_())
