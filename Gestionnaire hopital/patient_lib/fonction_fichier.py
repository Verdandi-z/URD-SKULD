
import json
import os
from json import JSONDecodeError
import datetime as d
import pandas as pd
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
DATA_DIR = CURRENT_DIR / "Data_and_sauvegarde"
DATA_DIR.mkdir(exist_ok=True)
JSON_FILE_PATH = DATA_DIR / "liste_patient.json"
ARCHIVE_FILE_PATH = DATA_DIR / "archive_des_sauvegardes.txt"



if not os.path.exists(JSON_FILE_PATH) or os.stat(JSON_FILE_PATH).st_size == 0 :
    liste_patient = {}
else :
    try :
        with open(JSON_FILE_PATH, "r", encoding='utf-8') as fichier :
            liste_patient = json.load(fichier)
    except FileNotFoundError :
        print("Erreur : Le fichier 'liste_patient.json' est introuvable ou corrompu. Initialisation d'une nouvelle liste.")
        liste_patient = {}
    except JSONDecodeError :
        print("erreur structure fichier")

def clear():
    certitude = input("êtes vous sur de vouloir supprimer les informations du fichier ? oui/non : ")
    date_now = d.datetime.now()
    minute = date_now.strftime("%M")
    if certitude == 'oui' :
        fichier_sauvegarde = f"liste_patient_backup.{date_now.date()}.{date_now.hour}:{minute}.json"
        data = liste_patient
        sauvegarde(fichier_sauvegarde, data)
        
        with open(JSON_FILE_PATH, "w") as clear_files:
            json.dump({}, clear_files,indent=4)
            print("votre fichier principale est désormais vide")

    else :
        print('tentative de suppresion annulé') 
        return

def sauvegarde(fichier_sauvegarde, data) :
    with open(fichier_sauvegarde ,'w') as fichier  : 
        json.dump(data, fichier, indent=4)
        nom_fichier = fichier_sauvegarde
        action = 'sauvegarde faite dans le fichier :'
        notif_sauvegarde(nom_fichier, action)

def notif_sauvegarde (nom_fichier, action) :
    date_sauvegarde = d.datetime.now()
    with open(ARCHIVE_FILE_PATH, "a+") as fichier_archiv:
        fichier_archiv.write(
            f"{action} {nom_fichier} faite le {date_sauvegarde.year}-{date_sauvegarde.month}-{date_sauvegarde.day} à {date_sauvegarde.hour} : {date_sauvegarde.minute} \n")
    print(f'{action} {nom_fichier}')

def exporter() :
    print ("Selectionnez le numéro du type de fichier que vous souhaitez générer ? \n 1-Texte \n 2-Excel \n 3-CSV")
    action = 'données exportés dans le fichier :'
    try :
        reponse = int(input(""))
    except ValueError :
        print("selectionner le type de fichier le numéro correspondant")
    if reponse not in [1,2,3] :
        print("veillez choisir entre 1,2 ou 3 pour choisir le type de fichier à exporter")
    if reponse == 1 :
        nom_fichier = DATA_DIR /'patients_export.txt'
        with open(nom_fichier, 'a') as export_files :
            for patient in liste_patient :
                export_files.write(f"Patient ID : {patient} \n")
                export_files.write(f"   nom : {liste_patient[patient]['nom']} \n")
                export_files.write(f"   age : {liste_patient[patient]['age']} \n")
                export_files.write(f"   motif d'hospitalisation : {liste_patient[patient]['motif']} \n")
            notif_sauvegarde(nom_fichier, action)

    if reponse in [2,3] :

        dataframe_patient = pd.DataFrame.from_dict(liste_patient, orient='index')
        dataframe_patient = dataframe_patient.reset_index().rename(columns={'index': 'Patient ID'})

        if reponse == 2 :
            nom_fichier = DATA_DIR / 'data_patient.xlsx'
            dataframe_patient.to_excel(nom_fichier)
            notif_sauvegarde(nom_fichier, action)

        if reponse == 3 :
            nom_fichier = DATA_DIR / 'data_patient.csv'
            dataframe_patient.to_csv(nom_fichier, sep=';', encoding='utf-8')
            notif_sauvegarde(nom_fichier, action)