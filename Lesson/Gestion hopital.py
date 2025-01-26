#Gestion hopital

import re 

def selection_chambre() : 
    while True :
        print("choisit la chambre qui t'interesse ? (1/2/3)")
        bed_room_number = re.sub(r'\D', '', input(""))
        bed_room_number = int(bed_room_number)
        if bed_room_number not in [1,2,3] :
            print ("selectionner parmis les chambres disponible")
        elif bed_room_number == 1 : 
            choix_menu1()
        elif bed_room_number == 2 : 
            choix_menu2()

def choix_menu1() : 
    while True :
        print ("Souhaitez vous faire au patient de la chambre 1 ? \n -ajouter  \n -modifier  \n -info) ")
        choix = input("").lower()
        if choix not in ["ajouter","modifier","info"]:
            print("selectionner parmi les choix")
            continue
        elif choix == "ajouter" : 
            print("Quel est le nom du patient de la chambre 1")
            nom_patient = input("").lower()
            print("Quel age à t-il ?")
            age_patient = int(input(""))
            print("quel pathologie à t-il ?")
            diagnostic = input("").lower()
            liste_patient["chambre_1"]["nom"]= nom_patient
            liste_patient["chambre_1"]["age"]= age_patient
            liste_patient["chambre_1"]["diagnostic"]= diagnostic
            print(liste_patient["chambre_1"].items())
        elif choix == "modifier" : 
            print(liste_patient["chambre_1"].items(), "\n quelle information souhaitez vous modifier? \n nom \n age \n diagnostic")
            modif = input("") 
            if modif not in ["nom", "age", "diagnostic"] : 
                print("choissisez parmis nom/age/diagnostic")
            elif modif == "nom" :
                print("Quel est le nom du patient de la chambre 1")
                nom_patient = input("").lower()
                liste_patient["chambre_1"]["nom"]= nom_patient
                print("nouveau nom est :", liste_patient["chambre_1"]["nom"])
            elif modif == "age" : 
                print("Quel age à t-il ?")
                age_patient = int(input(""))
                liste_patient["chambre_1"]["age"]= age_patient
                print("nouveau nom est :", liste_patient["chambre_1"]["age"])
            elif modif == "diagnostic" :
                print("quel pathologie à t-il ?")
                diagnostic = input("").lower()
                liste_patient["chambre_1"]["diagnostic"]= diagnostic
                print("nouveau nom est :", liste_patient["chambre_1"]["diagnostic"])
        elif choix == "info" : 
             print(liste_patient["chambre_1"].items())

def choix_menu2() : 
    while True :
        print ("Souhaitez vous faire au patient de la chambre 2 ? \n -ajouter  \n -modifier  \n -info) ")
        choix = input("").lower()
        if choix not in ["ajouter","modifier","info"]:
            print("selectionner parmi les choix")
            continue
        elif choix == "ajouter" : 
            print("Quel est le nom du patient de la chambre 2")
            nom_patient = input("").lower()
            print("Quel age à t-il ?")
            age_patient = int(input(""))
            print("quel pathologie à t-il ?")
            diagnostic = input("").lower()
            liste_patient["chambre_2"]["nom"]= nom_patient
            liste_patient["chambre_2"]["age"]= age_patient
            liste_patient["chambre_2"]["diagnostic"]= diagnostic
            print(liste_patient["chambre_2"].items())
        elif choix == "modifier" : 
            print(liste_patient["chambre_2"].items(), "\n quelle information souhaitez vous modifier? \n nom \n age \n diagnostic")
            modif = input("") 
            if modif not in ["nom", "age", "diagnostic"] : 
                print("choissisez parmis nom/age/diagnostic")
            elif modif == "nom" :
                print("Quel est le nom du patient de la chambre 2")
                nom_patient = input("").lower()
                liste_patient["chambre_2"]["nom"]= nom_patient
                print("nouveau nom est :", liste_patient["chambre_2"]["nom"])
            elif modif == "age" : 
                print("Quel age à t-il ?")
                age_patient = int(input(""))
                liste_patient["chambre_2"]["age"]= age_patient
                print("nouveau nom est :", liste_patient["chambre_2"]["age"])
            elif modif == "diagnostic" :
                print("quel pathologie à t-il ?")
                diagnostic = input("").lower()
                liste_patient["chambre_2"]["diagnostic"]= diagnostic
                print("nouveau nom est :", liste_patient["chambre_2"]["diagnostic"])
        elif choix == "info" : 
             print(liste_patient["chambre_2"].items())

def choix_menu3() : 
    while True :
        print ("Souhaitez vous faire au patient de la chambre 3 ? \n -ajouter  \n -modifier  \n -info) ")
        choix = input("").lower()
        if choix not in ["ajouter","modifier","info"]:
            print("selectionner parmi les choix")
            continue
        elif choix == "ajouter" : 
            print("Quel est le nom du patient de la chambre 2")
            nom_patient = input("").lower()
            print("Quel age à t-il ?")
            age_patient = int(input(""))
            print("quel pathologie à t-il ?")
            diagnostic = input("").lower()
            liste_patient["chambre_3"]["nom"]= nom_patient
            liste_patient["chambre_3"]["age"]= age_patient
            liste_patient["chambre_3"]["diagnostic"]= diagnostic
            print(liste_patient["chambre_3"].items())
        elif choix == "modifier" : 
            print(liste_patient["chambre_3"].items(), "\n quelle information souhaitez vous modifier? \n nom \n age \n diagnostic")
            modif = input("") 
            if modif not in ["nom", "age", "diagnostic"] : 
                print("choissisez parmis nom/age/diagnostic")
            elif modif == "nom" :
                print("Quel est le nom du patient de la chambre 2")
                nom_patient = input("").lower()
                liste_patient["chambre_3"]["nom"]= nom_patient
                print("nouveau nom est :", liste_patient["chambre_2"]["nom"])
            elif modif == "age" : 
                print("Quel age à t-il ?")
                age_patient = int(input(""))
                liste_patient["chambre_3"]["age"]= age_patient
                print("nouveau nom est :", liste_patient["chambre_3"]["age"])
            elif modif == "diagnostic" :
                print("quel pathologie à t-il ?")
                diagnostic = input("").lower()
                liste_patient["chambre_3"]["diagnostic"]= diagnostic
                print("nouveau nom est :", liste_patient["chambre_3"]["diagnostic"])
        elif choix == "info" : 
             print(liste_patient["chambre_3"].items())

nom_patient = "vide"
age_patient = "vide"
diagnostic = "vide"

liste_patient = { 
    "chambre_1" : { "nom" : nom_patient,
                "age" : age_patient,
                "diagnostic" : diagnostic },
                
    "chambre_2" : { "nom" : nom_patient,
                "age" : age_patient,
                "diagnostic" : diagnostic },     
    
    "chambre_3" : { "nom" : nom_patient,
                "age" : age_patient,
                "diagnostic" : diagnostic }        
                }


selection_chambre()

