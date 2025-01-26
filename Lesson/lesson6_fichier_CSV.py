import pandas as pd
import json

with open('/Users/hamdoune/Desktop/IAM/Gestionnaire hopital/liste_patient.json', 'r', encoding='utf-8' ) as f :
    data_base = json.load(f)
dataframe1 = pd.DataFrame.from_dict(data_base, orient= "index")
dataframe2 = pd.DataFrame.from_dict(data_base, orient="columns")

dataframe1 = dataframe1.reset_index().rename(columns = {'index' : 'patient'})
dataframe2 = dataframe2.reset_index().rename(columns = {'index' : 'patient'})


dataframe1.to_csv('test_df1.csv', sep=';', encoding='utf-8')
dataframe2.to_csv('test_df2.csv', sep=';', encoding='utf-8')
dataframe1.to_excel('test_excel.xlsx')