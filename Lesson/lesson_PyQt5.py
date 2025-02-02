import sys
from PyQt5.QtWidgets import *


class Window(QWidget) :
    def __init__(self, wind):
        super().__init__()
        self.wind = wind
        self.wind.setWindowTitle('Fenètre de connexion')
        self.wind.setGeometry(100,200,400,200)


    def build(self):

        layout_principal = QVBoxLayout()

        layout_horizontal1 = QHBoxLayout()
        label_mail = QLabel('Email : ')
        input_mail = QLineEdit()
        layout_horizontal1.addWidget(label_mail)
        layout_horizontal1.addWidget(input_mail)

        layout_horizontal2 = QHBoxLayout()
        label_mdp = QLabel('Mot de passe : ')
        input_mdp = QLineEdit()
        input_mdp.setEchoMode(QLineEdit.Password)
        layout_horizontal2.addWidget(label_mdp)
        layout_horizontal2.addWidget(input_mdp)



        bouton_connexion = QPushButton('Connexion', self)
        bouton_connexion.clicked.connect(self.click_connexion)


        layout_principal.addLayout(layout_horizontal1)
        layout_principal.addLayout(layout_horizontal2)
        layout_principal.addWidget(bouton_connexion)


        self.wind.setLayout(layout_principal)

    def click_connexion (self) :
        print("connexion")




app = QApplication(sys.argv)
wind1 = QWidget()
wind2 = QWidget()
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