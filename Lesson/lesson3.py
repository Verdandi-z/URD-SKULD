import os 

def lire_fichier() :
    if os.path.exists("patients.txt") : 
        with open("patients.txt", "r") as fichier :
            print(fichier.readlines())
    else : 
        print("fichier introuvable")

def ajouter_patient() :
    print('ajouter un patient avec la forme "nom, age, pathologie" ')
    nouveau_patient = input("")
    with open("patients.txt","a") as fichier : 
        fichier.write(f"\n{nouveau_patient}")
        print("patient ajouté")
        return

def afficher_patients() :
    if os.path.exists("patients.txt") : 
        with open("patients.txt") as fichier :
            for patient in fichier.readlines() :
                print(patient.strip())
    else : 
        print("fichier introuvable")

def triage_data() :
    if os.path.exists("patients.txt") : 
        with open("patients.txt", "r") as fichier : 
            for patient in fichier.readlines() :
                patient_data = patient.strip().split(",")
                diagnostic_data = f"{patient_data[2]}"
                age_data = f"{patient_data[1]}"
                with open("files_data_diagnostic.txt", "a") as fichier_data :
                    fichier_data.write(f"{diagnostic_data} \n")
                with open ("age_data.txt", "a") as fichier_data : 
                    fichier_data.write(f"{age_data} \n")
    else : 
        print("fichier introuvable")

def recherche_patient () : 
    print("donnez le nom du patient :")
    try :
        patient_recherche = input("").lower()
    except ValueError : 
        print("Ecrivez un nom")
    if os.path.exists("patients.txt") :
        patient_trouve = False
        with open("patients.txt","r") as fichier : 
            for patient in fichier.readlines() :
                patient_data = patient.strip().split(",")
                name_data = patient_data[0].strip().lower()
                if name_data == f"{patient_recherche}" :
                    print("patient trouvé", patient.strip())
                    patient_trouve = True
                    return
        if not patient_trouve :
            print("patient introuvable")        
    else : 
        print("dossier introuvable")

#MENU
fichiers = { "1" : "patients.txt",
           "2" :"age_data.txt",
           "3": "files_data_diagnostic.txt"}

while True : 
    print(""" selectionnez votre action avec le chiffre correspondant : \n
        1.afficher les patients \n
        2.ajouter un patient\n
        3.triez les données\n
        4.Rechercher un patient\n
        5.Nettoyez données \n
        6.Quitter \n """)
    try :
        choix_menu = int(input(""))
    except ValueError :
        print("veuillez donner un chiffre")
    if choix_menu not in [1,2,3,4,5,6] :
        print("cette action n'existe pas")
    elif choix_menu == 1 :
        afficher_patients()
    elif choix_menu == 2 :
        ajouter_patient()
    elif choix_menu == 3 :
        triage_data()
        print("triage fait")
        if os.path.exists("files_data_diagnostic.txt") : 
            with open("files_data_diagnostic.txt") as fichier :
                for data in fichier.readlines() :
                    print(data.strip())
        else : 
            print("fichier introuvable")
    elif choix_menu == 4 :
        recherche_patient()
    elif choix_menu ==5 :
        print("quel fichier voulez vous nettoyez ? \n 1.fichier patient \n 2.fichier age \n 1.fichier diagnostic")
        try : 
            choix_nettoyage = input("entrez le numéro du fichier :").strip()
        except Exception as e :
            print(f"Une erreur s'est produite : {e}")
        if choix_nettoyage in fichiers :
            fichier_choisi = fichiers[choix_nettoyage]
            with open(f"{fichier_choisi}","w") as fichier :
                print("nettoyage fait.",)
                pass
        else : 
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
            
    elif choix_menu == 6 : 
        print("à bientôt...")
        break


