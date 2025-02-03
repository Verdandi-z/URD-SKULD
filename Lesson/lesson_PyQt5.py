import sys
from PyQt5.QtWidgets import *


class w1(QWidget) :
    def __init__ (self) :
        super().__init__()
        self.setWindowTitle('connexion')
        self.setGeometry(100,200,400,200)
        self.build()

        self.w2 = None



    def build(self) :

        main_layout = QVBoxLayout()

        layout_h1 = QHBoxLayout()
        layout_h2 = QHBoxLayout()

        label_mail = QLabel('e-mail : ')
        self.input_mail = QLineEdit()

        layout_h1.addWidget(label_mail)
        layout_h1.addWidget(self.input_mail)

        label_mdp = QLabel('mot de passe : ')
        self.input_mdp = QLineEdit()
        self.input_mdp.setEchoMode(QLineEdit.Password)

        layout_h2.addWidget(label_mdp)
        layout_h2.addWidget(self.input_mdp)

        self.bouton_conn = QPushButton('Connexion')
        self.bouton_conn.clicked.connect(self.login)

        main_layout.addLayout(layout_h1)
        main_layout.addLayout(layout_h2)
        main_layout.addWidget(self.bouton_conn)

        self.setLayout(main_layout)

    def login (self) :
        email = self.input_mail.text()
        mdp = self.input_mdp.text()

        liste_inscrit = ['zak@gmail.com', 'mohamed@gmail.com', 'hajar@gmail.com']

        if email in liste_inscrit and mdp == '1234' :
            if self.w2 is None :
                self.close()
                self.w2 = w2()
                self.w2.show()
                print('connexion')
        else :
            print('erreur')


class w2 (QWidget) :
    def __init__(self):
        super().__init__()
        self.setWindowTitle('connecté')
        self.setGeometry(100,200,400,200)
        self.build()

    def build(self) :
        layout = QVBoxLayout()

        label_connect = QLabel('connecté')

        layout.addWidget(label_connect)

        self.setLayout(layout)




app = QApplication(sys.argv)
main_w = w1()
main_w.show()

sys.exit(app.exec_())