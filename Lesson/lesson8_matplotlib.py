import pandas as pd
import sqlite3

import matplotlib.pyplot as plt

conn = sqlite3.connect('PATIENT_test.db')
cur = conn.cursor()

df = pd.read_sql_query('SELECT * FROM PATIENTS', conn)

def print_stat () :
    print(f"moyenne d'age de : {df['AGE'].mean()} ans ")
    print(f"médiane d'age de : {df['AGE'].median()} ans ")
    print(f"motif d'hospitaliation le plus fréquent : {df['MOTIF'].mode().values[0]} avec {df['MOTIF'].value_counts().max()} patients")

'''
x = df['AGE']
y = df['MOTIF'].value_counts()
plt.figure()
plt.hist(x, bins = 25)
plt.title('repartition des âges')
plt.xlabel('âge')
plt.ylabel('nombre de patient')
plt.show()
'''

value_counts = df['MOTIF'].value_counts()
motifs = value_counts.index.tolist()
comptages = value_counts.values.tolist()

value_counts = df['AGE'].value_counts()
x = value_counts.index.tolist()
y = value_counts.values.tolist()
print(x)
print(y)

'''
plt.figure()
plt.bar(motifs, comptages)
plt.xticks(rotation = 45)
plt.show()
'''

plt.figure()
plt.bar(x,y)
plt.show()
