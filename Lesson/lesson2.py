'''
def operation() :
    while True :
        print("choix operation addition/soustraction")
        try : 
            choixoperation = str(input()).lower().strip()
        except : 
            print ("veulliez selectionner une opération proposé")
        

        if choixoperation in ['addition','soustraction'] :
            try : 
                a = float(input("veuillez choisir un premier nombre?"))
                b = float(input("veuillez choisir un deuxieme nombre?")) 
                if choixoperation == 'addition' :
                    return (a + b)
                if choixoperation == 'soustraction' : 
                    return(a - b)    
            except ValueError :
                print ("Selectionez un nombre")
        else :    
            print("veulliez choisir une opération cité")

while True :
    resultat = operation()
    print(resultat)
    print("voulez vous recommencer ? (oui/non)")
    reponse = str(input("")).strip().lower()
    if reponse == 'oui' :
        continue
    else :
        print("merci, aurevoir")
        break
'''
'''
print("donnez un nom de fruit")
liste_de_fruit = []
while len(liste_de_fruit) < 5 :
    nom_de_fruit = input("").lower()
    if not nom_de_fruit.isalpha():  # Vérifie si l'entrée est valide
        print("Veuillez entrer un nom valide.")
        continue
    liste_de_fruit.append(nom_de_fruit)
    print(liste_de_fruit)
liste_de_fruit.pop(2)
print(liste_de_fruit)
liste_de_fruit.sort()
print('la liste trié est :', liste_de_fruit)
'''

