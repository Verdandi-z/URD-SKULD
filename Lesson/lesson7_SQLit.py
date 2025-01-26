import sqlite3
import json


conn = sqlite3.connect('PATIENT_test.db')
cur = conn.cursor()
cur.execute('DROP TABLE PATIENTS')

query =  'CREATE TABLE IF NOT EXISTS PATIENTS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOM TEXT, AGE INTEGER, MOTIF TEXT)'
cur.execute(query)

with open('liste_patient.json', 'r', encoding="utf-8") as db :
    source_db = json.load(db)
    for patient in source_db :
        cur.execute('''INSERT INTO PATIENTS (NOM, AGE, MOTIF) 
        VALUES (?,?,?)''',
                    (source_db[patient]['nom'],source_db[patient]['age'],source_db[patient]['motif']))

'''
with open('test_df1.csv','r') as source :
    source_db = csv.DictReader(source)
    for row in source_db :
        cur.execute(""""INSERT INTO PATIENTS (NOM, AGE, MOTIF) VALUES (?,?,?) """, (row['nom'], row['age'] , row['motif']) )
'''

query = 'abcd'
query += 'cyz'

print(query)





conn.commit()
conn.close()