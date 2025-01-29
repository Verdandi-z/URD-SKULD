import sys
from PyQt5.QtWidgets import *


class Window(QWidget) :
    def __init__(self, wind):
        super().__init__()
        self.wind = wind

    def build(self):
        self.wind.setWindowTitle('Fenètre de connexion')
        self.wind.setGeometry(100,200,400,400)

        label = QLabel('entrez votre mail', self.wind)
        label2 = QLabel('entrez votre mot de passe', self.wind)

        input_mail = QLineEdit(self.wind)
        input_mdp = QLineEdit(self.wind)
        input_mdp.setEchoMode(QLineEdit.Password)

        bouton_connexion = QPushButton('connexion', self.wind)


        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(input_mail)
        layout.addWidget(label2)
        layout.addWidget(input_mdp)
        layout.addWidget(bouton_connexion)

        self.wind.setLayout(layout)




app = QApplication(sys.argv)
wind1 = QWidget()
w1 = Window(wind1)
w1.build()

wind1.show()

sys.exit(app.exec_())

## 1/ étudier les class en python
## 2/ choisir les élements à integrer sur le menu de base
## 3/ creer fonction permmetant de définir  par défaut  le choix d'export du type de fichier pour que sur le menu le bouton mène direct à l'export.


### 1- fenetre + inputmail + inputmdp + bouton connect
###
###
###