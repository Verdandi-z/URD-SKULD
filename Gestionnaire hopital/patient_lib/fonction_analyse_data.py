import pandas as pd
import sqlite3
import pathlib
import matplotlib.pyplot as plt

dir_files = pathlib.Path(__file__).parent
dir_datafiles = dir_files/'Data_and_sauvegarde'
dir_patient_db = dir_datafiles/'patients.db'

conn = sqlite3.connect(dir_patient_db)
cursor = conn.cursor()
df = pd.read_sql_query('SELECT * FROM patients', conn)

def print_stat () :
    print(f"moyenne d'age de : {df['AGE'].mean()} ans ")
    print(f"médiane d'age de : {df['AGE'].median()} ans ")
    print(f"écart-type d'age de : {df['AGE'].std()} ans ")
    print(f"motif d'hospitaliation le plus fréquent : {df['MOTIF'].mode().values[0]} avec {df['MOTIF'].value_counts().max()} patients")

def affiche_graph () :
    plt.figure()
    value_counts = df['AGE'].value_counts()
    x = value_counts.index.tolist()
    y = value_counts.values.tolist()


    plt.subplot(1,2, 1)
    plt.bar(x,y)
    plt.xlabel('age')
    plt.ylabel('nombre de patient')
    plt.title('répartition des ages patients')

    value_counts = df['MOTIF'].value_counts()
    x = value_counts.index.tolist()
    y = value_counts.values.tolist()

    plt.subplot(1,2, 2)
    plt.bar(x,y)
    plt.ylabel("nombre de patient")
    plt.xticks(rotation = 90)
    plt.title("répartition des motifs d'hospitalisation")

    plt.tight_layout()
    save_fig()
    plt.show()

def print_top5_bas_age () :
    df_tri = df.sort_values(by='AGE')
    print(df_tri.head())

def print_top5_motif () :
    cursor.execute('''SELECT MOTIF, COUNT(*) as frequence 
    FROM patients
    GROUP BY MOTIF 
    ORDER BY frequence DESC 
    LIMIT 5;
    ''')
    resultats = cursor.fetchall()
    for motif, recurrence in resultats :
        print(f'{motif} : {recurrence}')

def print_par_categorie_age():
    print('''Selectionné la catégorie âge à afficher :
    1. 0-20 ans
    2. 21-40 ans
    3. 41-60 ans
    4. 61-80 ans
    5. 81-130 ans
    ''')
    choix = int(input('choix : '))

    if choix == 1 :
        limit1 = 0
        limit2 = 20
        query = print4age(limit1, limit2)
        stat_spe(query)

    if choix == 2 :
        limit1 = 21
        limit2 = 40
        query = print4age(limit1, limit2)
        stat_spe(query)

    if choix == 3 :
        limit1 = 41
        limit2 = 60
        query = print4age(limit1, limit2)
        stat_spe(query)

    if choix == 4 :
        limit1 = 61
        limit2 = 80
        query = print4age(limit1, limit2)
        stat_spe(query)

    if choix == 5 :
        limit1 = 81
        limit2 = 130
        query = print4age(limit1, limit2)
        stat_spe(query)

    if choix not in [1,2,3,4,5] :
        print('veuillez choisir un chiffre valide')

def print4age (limit1, limit2) :

    query = f''' SELECT NOM, AGE, MOTIF
    FROM patients
    WHERE AGE >= {limit1} AND AGE <= {limit2}
    ORDER BY AGE
    '''

    cursor.execute(query)

    resultat = cursor.fetchall()

    print(f'catégorie age : {limit1}-{limit2}')
    for nom, age, motif in resultat :
        print(f'{nom}, {age} ans, {motif}')

    return query

def stat_spe (query) :
    df_spe = pd.read_sql_query(query, conn)
    print(f"\n\nmoyenne d'age de : {df_spe['AGE'].mean()} ans ")
    print(f"médiane d'age de : {df_spe['AGE'].median()} ans ")
    print(f"écart-type d'age de : {df_spe['AGE'].std()} ans ")
    print(f"motif d'hospitaliation le plus fréquent : {df_spe['MOTIF'].mode().values[0]} avec {df_spe['MOTIF'].value_counts().max()} patients\n\n")




def save_fig () :
    reponse = input("Voulez-vous enregistrer ce graphique oui/non : ").lower().strip()
    if reponse != 'oui':
        return
    else:
        titre = input("Choississez un titre aux graphiques : ")
        try :
            choix = int(input("Choississez un type de fichier \n1. PDF \n2. JPEG \n3. PNG \n"))
        except ValueError as e :
            print(f'Erreur : {e}')
        if  choix == 1 :
            type = 'pdf'
            plt.savefig(f'{titre}.{type}')
        if  choix == 2 :
            type = 'jpeg'
            plt.savefig(f'{titre}.{type}')
        if  choix == 3 :
            type = 'png'
            plt.savefig(f'{titre}.{type}')

