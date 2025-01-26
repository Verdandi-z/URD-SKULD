def calculatrice():
    while True :
        operation = str(input("quelle opération souhaitez vous effectuer ?")).lower()
        
        if operation in ["addition","soustraction","multiplication","division","modulo","exponentiation"] :
            while True :
                try :
                    nombre_1 = float(input("choisissez votre 1er nombre :"))
                    nombre_2 = float(input("choisissez votre 2eme nombre :"))
                except ValueError : 
                    print("veuillez choisir un nombre")

                if operation == "addition":
                    print('le resultat est', nombre_1 + nombre_2)
                elif operation == "soustraction":
                    print('le resultat est', nombre_1 - nombre_2)
                elif operation == "multiplication":
                    print('le resultat est', nombre_1 * nombre_2)
                elif operation == "division":
                    if nombre_2 == 0 :
                        print("cette opération est impossible")
                    else :
                        print('le resultat est', nombre_1 / nombre_2)
                
                elif operation == "modulo":
                    if nombre_2 == 0 : print("cette opération est impossible")
                    else : print('le resultat est', nombre_1 % nombre_2)

                elif operation == "exponentiation" : 
                    print('le resultat est', nombre_1 ** nombre_2) 
            
                recommencer = str(input("voulez vous recommencer ?")).lower()
                if recommencer != "oui":
                    print("aurevoir")
                    break
            
            else:
                print("je ne comprends pas, veuillez choisir entre addition, multiplication, soustraction, multiplication, division, exponentiation, modulo")
                
calculatrice()
