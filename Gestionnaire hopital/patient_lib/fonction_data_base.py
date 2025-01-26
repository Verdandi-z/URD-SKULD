import sqlite3
import pathlib
import re
import datetime as dt
import pandas as pd


dir_files = pathlib.Path(__file__).parent
dir_datafiles = dir_files/'Data_and_sauvegarde'
dir_patient_db = dir_datafiles/'patients.db'
dir_archive = dir_datafiles/'archive_des_sauvegardes.txt'


try :
    conn = sqlite3.connect(dir_patient_db)
    cursor = conn.cursor()
    cursor.execute('CREATE INDEX IF NOT EXISTS index_nom ON patients (NOM)')
    cursor.execute('CREATE INDEX IF NOT EXISTS index_age ON patients (AGE)')
    cursor.execute('CREATE INDEX IF NOT EXISTS index_motif ON patients (MOTIF)')
    conn.commit()
except sqlite3.Error as e:
    print(f'Erreur : {e}')

def addSQL_patient() :
    while True :
        print("Ajouter patient")
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
                continue
        except ValueError :
            print("veuillez ecrire un nombre")
            continue
        motif_entrer = input("motif d'hopitaliation : ").lower().strip()
        pattern_verication_motif = r"^(?=.*[A-Za-zÀ-ÖØ-öø-ÿ].*[A-Za-zÀ-ÖØ-öø-ÿ].*[A-Za-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ\s'\-]+$"
        motif_verif = re.match(pattern_verication_motif, motif_entrer)
        if not motif_verif :
            print("veuillez entrer un motif correct")
        motif = motif_verif.group()
        try :
            cursor.execute('INSERT INTO patients (NOM, AGE, MOTIF) VALUES (?,?,?)',(nom,age,motif))
            conn.commit()
        except sqlite3.Error as e :
            print(f'Erreur : {e}')
        print("nouveau patient ajouté à la base de donnée")
        repeate = input('voulez vous recommencer ? oui/non : ')
        if repeate != 'oui' :
            break

def print_all_db() :
    try :
        cursor.execute("SELECT * FROM patients")
    except sqlite3.Error as e :
        print(f'Erreur : {e}')
    print_all = cursor.fetchall()
    for patient in print_all :
        print(f"ID : patient {patient[0]} \n  nom : {patient[1]}\n  age : {patient[2]}\n  motif :{patient[3]}")

def affiche_patient(patient) :
    print(f"ID : patient {patient[0]} \n  nom : {patient[1]}\n  age : {patient[2]}\n  motif :{patient[3]}")

def selection_patient () :
    while True :
        try :
            cursor.execute('SELECT * FROM patients')
        except sqlite3.Error as e :
            print(f'Erreur : {e}')
        patient_db = cursor.fetchall()
        try :
            selection_ID = int(input("selectionnez le patient par son ID ? \n"))
        except ValueError :
            print("Veuillez entrer un nombre.")

        flag_patient = False

        for patient in patient_db:
            if selection_ID == patient[0] :
                print(f"vous avez selectionné :")
                affiche_patient(patient)
                flag_patient = True

                cursor.execute('SELECT NOM, AGE, MOTIF FROM patients WHERE id = ?', (selection_ID,))
                print("quelle par paramètre souhaitez-vous faire  ? \n1. Modifier le nom \n2. Modifier l'âge \n3. Modifier le motif d'hospitalisation \n4. Supprimer le patient de la database")
                try :
                    modif = int(input(""))
                except ValueError :
                    print("Choissez un nombre entre 1 et 4")


                if modif == 1 :
                    element = 'NOM'
                    nom_entrer = input("entrez le nouveau nom : ").lower().strip()
                    pattern_verication = r'^(?=.{3,}$)[A-Za-zÀ-ÖØ-öø-ÿ]+(?:-[A-Za-zÀ-ÖØ-öø-ÿ]+)*$'
                    nom_verification = re.match(pattern_verication, nom_entrer)
                    if not nom_verification:
                        print("veuillez écrire un nom")
                        continue
                    nom = nom_verification.group()
                    modifitation(selection_ID, element, nom)
                    break

                if modif == 2 :
                    element = 'AGE'
                    try:
                        age = int(input("nouvel age : "))
                        if age <= 0 or age >= 130:
                            print("age invalide")
                    except ValueError:
                        print("veuillez ecrire un nombre")
                        continue
                    modifitation(selection_ID,element,age)
                    break

                if modif == 3 :
                    element ='MOTIF'
                    motif_entrer = input("nouveau motif d'hopitaliation : ").lower().strip()
                    pattern_verication_motif = r"^(?=.*[A-Za-zÀ-ÖØ-öø-ÿ].*[A-Za-zÀ-ÖØ-öø-ÿ].*[A-Za-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ\s'\-]+$"
                    motif_verif = re.match(pattern_verication_motif, motif_entrer)
                    if not motif_verif:
                        print("veuillez entrer un motif correct")
                    motif = motif_verif.group()
                    modifitation(selection_ID, element, motif)
                    break

                if modif == 4 :
                    verif = input("êtes-vous sur de vouloir supprimer le patient ? oui/non \n")
                    if verif != 'oui' :
                        continue
                    else :
                        cursor.execute('DELETE FROM patients WHERE id = ?', (selection_ID,))
                        conn.commit()
                        print("patient supprimé. ")
                        break

        if not flag_patient:
            print("aucun patient retrouvé")

def modifitation(selection_ID ,element, new_data) :
    try :
        cursor.execute(f'UPDATE patients SET {element} = ? WHERE ID = ?', (new_data, selection_ID))
        conn.commit()
    except sqlite3.Error as e :
        print(f'Erreur : {e}')

    print("modification enregistré")
    return

def pagination(nb_lign_print, page) :
    nb_lign_ignorer = nb_lign_print * (page-1)
    try :
        cursor.execute('SELECT * FROM patients LIMIT ? OFFSET ?', (nb_lign_print, nb_lign_ignorer))
    except sqlite3.Error as e :
        print(f'Erreur : {e}')
    return cursor.fetchall()

def pagination_activation (nb_lign_print) :
    try :
        cursor.execute('SELECT COUNT (*) FROM patients')
    except sqlite3.Error as e :
        print(f'Erreur : {e}')
    pages_tot = int(cursor.fetchone()[0] // nb_lign_print) + 1
    while True :
        for page in range(1,pages_tot + 1) :
            data = pagination(nb_lign_print, page)

            for patient in data :
                affiche_patient(patient)
            print(f"\n                                       pages {page}")

            if page < pages_tot :
                print("\nvoir la suite (oui/non) :")
                suite = input("").lower().strip()
                if suite != 'oui' :
                    break
            else :
                print('fin page')
        break

def tri_opti() :
    print("entrez les paramatres qui vous interesse")
    name_select = input("nom : ").lower().strip()
    age_limit = None
    try:
        age_limit = int(input("age minimal : "))
    except ValueError:
        pass
    motif_select = input("motif : ").lower().strip()
    requete = 'SELECT * FROM patients WHERE 1=1 '
    parametre_tri = []

    if name_select :
        requete += ' AND NOM LIKE ?'
        parametre_tri.append(f'%{name_select}%')

    if age_limit :
        requete += ' AND AGE >= ?'
        parametre_tri.append(age_limit)

    if motif_select :
        requete += ' AND MOTIF LIKE ?'
        parametre_tri.append(f'%{motif_select}%')

    parametre_tri = tuple(parametre_tri)
    try :
        cursor.execute(f'{requete}', parametre_tri )
    except sqlite3.Error as e :
        print(f'Erreur : {e}')
        return
    patient_trier = cursor.fetchall()
    if patient_trier :
        for patient in patient_trier :
            affiche_patient(patient)
        return patient_trier, name_select, age_limit, motif_select
    else :
        print("aucun patient trouver")

def notif_sauvegarde (nom_fichier, action) :
    date_sauvegarde = dt.datetime.now()
    with open(dir_archive, "a+") as fichier_archiv:
        fichier_archiv.write(
            f"{action} {nom_fichier} faite le {date_sauvegarde.year}-{date_sauvegarde.month}-{date_sauvegarde.day} à {date_sauvegarde.hour} : {date_sauvegarde.strftime('%M')} \n")
    print(f'{action} {nom_fichier}')

def export_data_base(data_base, name_file) :
    print("Format d'exportation : \n1. Texte \n2. Excel \n3. CSV")
    dir_export = dir_datafiles/'export_files'/name_file
    try :
        choix = int(input("selectionnez par le chiffre associé :\n "))
    except ValueError as e :
        print("Erreur : {e} \nEntrez un nombre")
    action = 'export de la base de donnée vers '

    if choix == 1 :
        with open(f'{dir_export}.txt', 'w+') as data:
            for patient in data_base :
                data.write(f'ID : {patient[0]}')
                data.write(f'\nnom : {patient[1]}, age : {patient[2]}, motif : {patient[3]}\n')
            notif_sauvegarde(nom_fichier=f'{name_file}.txt', action=action)

    if choix in [2,3] :
        nom = []
        age = []
        motif = []
        for patient in data_base :
            nom.append(f'{patient[1]}')
            age.append(int(f'{patient[2]}'))
            motif.append(f'{patient[3]}')
        data = { 'NOM' : nom ,
                 'AGE' : age,
                 'MOTIF' : motif}
        df = pd.DataFrame(data)
        df.index = df.index + 1

        if choix == 2 :
            df.to_excel(f'{dir_export}.xlsx')
            notif_sauvegarde(nom_fichier=f'{name_file}.xlsx', action=action)

        if choix == 3 :
            df.to_csv(f'{dir_export}.csv')
            notif_sauvegarde(nom_fichier=f'{name_file}.csv', action=action)

    if choix not in [1, 2, 3] :
        print("veuillez choisir un nombre entre 1 et 3")

def select_export() :
    print("que souhaitz-vous exporter ? \n1. Toute la base de donnée \n2. Certain élements de la base de donnée")
    choix = int(input(''))
    time = dt.datetime.now()
    if choix == 1 :
        name_file = f'DataBase_patients_{time.date()}_{time.hour}h{time.strftime("%M")}'
        cursor.execute('SELECT * FROM patients')
        data_base = cursor.fetchall()
        export_data_base(data_base,name_file)
    if choix == 2 :
        patient_trier, name_select, age_limit, motif_select = tri_opti()
        name_file = 'Data_trier_'
        if name_select :
            name_file += f'nom({name_select}-)'
        if age_limit :
            name_file += f'age>{age_limit}ans-'
        if motif_select :
            name_file += f'motif({motif_select})'
        name_file += f'{time.date()}_{time.hour}h{time.strftime("%M")}'
        print("souhaitez-vous exporter cette liste? oui/non")
        choix_2 = input('').strip()
        if choix_2 != 'oui' :
            return
        else :
            data_base = patient_trier
            export_data_base(data_base, name_file)

def clear() :
    print('que voulez-vous supprimer : \n1. Toute la base de donnée \n2.Certain patients')
    choix = int(input(""))
    if choix == 1 :
        verif_choice = input("êtes vous sur de vouloir supprimer toute la base de donnée ? oui/non : ").lower().strip()
        if verif_choice != 'oui' :
            print('action annulé')
            pass
        else :

            cursor.execute('DROP TABLE IF EXISTS patients')
            cursor.execute('CREATE TABLE patients (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOM TEXTE, AGE INTEGER, MOTIF TEXTE)')
            conn.commit()
            print('toute la base de donnée est supprimé')

    if choix == 2 :
        verif_choice = input("êtes vous sur de vouloir supprimer des patients de la base de données ? oui/non : ").lower().strip()
        if verif_choice != 'oui':
            print('action annulé')
            pass
        else:
            tri_opti()
            print('Selectionner les patients à supprimer par ID de la forme \nexemple: ID1, ID2, ID3,...,ID10')
            patient4delete = input('').replace(' ', '').lower()
            list_ID = []
            for ID_select in patient4delete.split(',') :
                if ID_select.startswith('id') :
                    ID_select = re.sub(r'\D','', ID_select)
                    for ID in ID_select :
                        ID = int(ID)
                        list_ID.append(ID)
            for ID_for_delete in list_ID :
                cursor.execute('DELETE FROM patients WHERE ID = ?', (ID_for_delete,) )
                conn.commit()
            print("suppression effectué")


