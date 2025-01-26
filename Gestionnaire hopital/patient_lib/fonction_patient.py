
import re
import json
from json import JSONDecodeError
import os
import pathlib
from . import fonction_fichier as ff
from . import fonction_data_base as fdb

CURRENT_DIR = pathlib.Path(__file__).parent
DATA_DIR = CURRENT_DIR / "Data_and_sauvegarde"
JSON_FILE_PATH = DATA_DIR / "liste_patient.json"

if not os.path.exists(JSON_FILE_PATH) or os.stat(JSON_FILE_PATH).st_size == 0 :
    liste_patient = {}
else :
    try :
        with open(JSON_FILE_PATH, "r", encoding="utf-8") as fichier :
            liste_patient = json.load(fichier)
    except FileNotFoundError  :
        print("Erreur : Le fichier 'liste_patient.json' est introuvable ou corrompu. Initialisation d'une nouvelle liste.")
    except JSONDecodeError:
        print("erreur structure fichier")

def affiche_patient(patient) :
        print("")
        print (f"\n{patient} :")
        print(f"nom : {liste_patient[patient]['nom']}")
        print(f"age : {liste_patient[patient]['age']}")
        print(f"motif d'hospitalisation : {liste_patient[patient]['motif']} \n")

def ajouter_patient() :
    while True :
        print("ajouter patient")
        nom_entrer = input("nom :").lower().strip()
        pattern_verication = r'^(?=.{3,}$)[A-Za-zÀ-ÖØ-öø-ÿ]+(?:-[A-Za-zÀ-ÖØ-öø-ÿ]+)*$'
        nom_verification = re.match(pattern_verication, nom_entrer)
        if not nom_verification  :
            print("veuillez écrire un nom")
            continue
        nom = nom_verification.group()
        try :
            age = int(input("age :"))
            if age <= 0 or age >= 130 :
                print("age invalide")
        except ValueError :
            print("veuillez ecrire un nombre")
            continue
        motif_entrer = input("motif d'hopitaliation : ").lower().strip()
        pattern_verication_motif = r"^(?=.*[A-Za-zÀ-ÖØ-öø-ÿ].*[A-Za-zÀ-ÖØ-öø-ÿ].*[A-Za-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ\s'\-]+$"
        motif_verif = re.match(pattern_verication_motif, motif_entrer)
        if not motif_verif :
            print("veuillez entrer un motif correct")
        motif = motif_verif.group()
        fdb.addSQL_patient(nom, age, motif)
        index_liste = len(liste_patient)+1
        liste_patient[f"patient{index_liste}"] = {"nom": nom,
                                                  "age": age,
                                                  "motif" : motif}
        print("patient ajouté")
        with open(JSON_FILE_PATH, "w") as fichier :
            json.dump(liste_patient, fichier, indent=4)

            fichier_sauvegarde = 'liste_patient.json'
            data = liste_patient
            ff.sauvegarde(fichier_sauvegarde, data)


        repeat = input("voulez vous recommencer? oui/non : ")
        if repeat != "oui" :
            print("très bien")
            break
        else :
           continue

def voir_patients() :
    if not liste_patient :
        print("aucun patient")
        return
    for patient in liste_patient :
        affiche_patient(patient)

def tri_name_motif(choix):
    if choix == 1:
        recherche_enter = input("entrez le un nom :").lower().strip()
        recherche_caractere(recherche_enter)
    if choix == 3:
        recherche_enter = input("entrez un motif d'hospitalisation :").lower().strip()
        recherche_caractere(recherche_enter)

def recherche_caractere(recherche_enter):
    pattern_verication = r'^[^\d]+(?:[\s-][^\d]+)*$'
    recherche_verification = re.match(pattern_verication, recherche_enter)
    if not recherche_verification:
        print("Entrez une recherche correct.")
    recherche = recherche_verification.group()
    if not recherche:
        print("entrer une recherche correct")
    drapeau_patient = False
    for patient in liste_patient:
        if recherche in [liste_patient[patient]['nom'], liste_patient[patient]['motif']]:
            affiche_patient(patient)
            drapeau_patient = True
    if not drapeau_patient:
        print("aucun patient trouvé")

def tri_age(age_limit):
    drapeau_patient = False
    for patient in liste_patient:
        age_patient = liste_patient[patient]['age']
        if age_patient > age_limit:
            affiche_patient(patient)
            drapeau_patient = True

    if not drapeau_patient:
        print("aucun patient trouvé")

def aucun_patient() :
    print("aucun patient retrouvé")

def tri_multiple():
    print("entrez les paramatres qui vous interesse")
    name_select = input("nom : ").lower().strip()
    age_limit = input("age minimal : ")
    try :
        age_limit = age_limit.isdigit() if int(age_limit) else 0
    except ValueError :
        print(" Erreur : Entrez un nombre ")
    motif_select = input("motif : ").lower().strip()
    drapeau_patient = False

    for patient in liste_patient:
        if age_limit :
            if [name_select, motif_select] == [liste_patient[patient]['nom'], liste_patient[patient]['motif']] and \
                    liste_patient[patient]['age'] > age_limit:
                affiche_patient(patient)
                drapeau_patient = True
            if name_select == liste_patient[patient]['nom'] and liste_patient[patient][
                'age'] > age_limit and not motif_select:
                affiche_patient(patient)
                drapeau_patient = True

            if motif_select == liste_patient[patient]['motif'] and liste_patient[patient][
                'age'] > age_limit and not name_select:
                affiche_patient(patient)
                drapeau_patient = True

            if liste_patient[patient]['age'] > age_limit and not name_select and not motif_select:
                affiche_patient(patient)
                drapeau_patient = True

        if [name_select, motif_select] == [liste_patient[patient]['nom'],
                                           liste_patient[patient]['motif']] and not age_limit :
            affiche_patient(patient)
            drapeau_patient = True

        if name_select == liste_patient[patient]['nom'] and not age_limit  and not motif_select:
            affiche_patient(patient)
            drapeau_patient = True

        if motif_select == liste_patient[patient]['motif'] and not age_limit  and not name_select:
            affiche_patient(patient)
            drapeau_patient = True

    if not drapeau_patient :
        print("aucun patient retrouvé")

    if not name_select and not motif_select and not age_limit :
        print("veuillez rentrer un parametre de recherche")

def trier():
    while True:
        print(
            "selectionnez un parametre de recherche (entrez le chiffre du paramètre)\n1.nom \n2.age \n3.motif \n4.paramètre multiple :")
        try:
            choix = int(input(""))
        except ValueError as e:
            print(f" erreur lié à {e}, veuillez selectionner uniqumenet un chiffre")
            continue

        if choix == 2:
            print("à partir de quel âge souhaitez vous afficher les patients?")
            try:
                age_limit = int(input(""))
            except ValueError:
                print("veuillez choisir uniquement un nombre")
                continue
            tri_age(age_limit)

        elif choix in [1, 3]:
            tri_name_motif(choix)

        elif choix == 4:
            tri_multiple()

        else:
            print("veuillez choisir un chiffre entre 1 et 4")

        recommencer = input("désirez vous recommencer ? (oui/non) : ")
        if recommencer != 'oui':
            print('aurevoir')
            break

