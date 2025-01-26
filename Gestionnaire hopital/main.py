from patient_lib import  fonction_patient as fp
from patient_lib import  fonction_fichier as ff


#MENU
while True :
    print("Selectionnez une action par le chiffre correspondant : \n 1. Ajouter patient \n 2. Recherche de patient \n 3. Voir tous les patients \n 4. Nettoyer fichier patient \n 5. Exporter la liste des patients \n 6. Quitter")
    try :
        choix_menu = int(input(""))
    except ValueError :
        print("veuillez choisir par le chiffre correspondant")
        continue
    if choix_menu == 1 :
        fp.ajouter_patient()
    if choix_menu == 2 :
        fp.trier()
    if choix_menu == 3 :
        fp.voir_patients()
    if choix_menu == 4 :
        ff.clear()
    if choix_menu == 5 :
        ff.exporter()
    if choix_menu == 6 :
        print ("Fermé")
        break
    else :
        print("Veuillez choisir un chiffre entre 1 et 6")

