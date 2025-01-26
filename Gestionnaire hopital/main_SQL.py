from patient_lib import fonction_data_base as fdb
from  patient_lib import  fonction_analyse_data as fad

while True :
    print("Selectionnez une action par le chiffre correspondant : \n 1. Ajouter patient \n 2. Recherche de patient \n 3. Voir tous les patients \n 4. Gestion de la database \n 5. Exporter la liste des patients \n 6. Supprimer des données "
          "\n 7. Analyse statistique \n 8. Quitter ")
    try :
        choix_menu = int(input(""))
    except ValueError :
        print("veuillez choisir par le chiffre correspondant")
        continue
    if choix_menu == 1 :
        fdb.addSQL_patient()
    if choix_menu == 2 :
        fdb.tri_opti()
    if choix_menu == 3 :
        nb_lign_print = int(input("Combien de patient voulez-vous afficher par pages ? (ecrivez uniquement le nombre): "))
        fdb.pagination_activation(nb_lign_print)
    if choix_menu == 4 :
        fdb.selection_patient()
    if choix_menu == 5 :
        fdb.select_export()
    if choix_menu == 6 :
        fdb.clear()
    if choix_menu == 7 :
        print('''Selectionnez une action : 
1. Afficher moyenne, médiane, motif d'hospistalisation le plus fréquent
2. Afficher les graphiques (répartition age et repartition des motifs d'hospitalisation)
3. Afficher les 5 motifs d'hospitalisations les plus fréquents et les 5 patients les plus jeunes
4. Afficher les statistiques par catégorie d'âge''')
        try :
            choix = int(input(''))
        except ValueError as e :
            print(f'Erreur : {e}')
        if choix == 1 :
            fad.print_stat()
        if choix == 2 :
            fad.affiche_graph()
        if choix == 3 :
            print("\nles 5 motifs d'hospitalisation les plus fréquent : ")
            fad.print_top5_motif()
            print('\nLes 5 patients les plus jeunes : ')
            fad.print_top5_bas_age()
            print("\n")
        if choix == 4 :
            fad.print_par_categorie_age()
        if choix not in [1,2,3,4] :
            print("Sélectionner une action par son nombre ")
    if choix_menu == 8 :
        print ("Fermé")
        fdb.conn.close()
        break
    if choix_menu not in [1,2,3,4,5,6,7,8] :
        print("Veuillez choisir un chiffre entre 1 et 8")
