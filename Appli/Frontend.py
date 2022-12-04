#charger le module psycopg2
import psycopg2, time
from fonctions import *
print("-----------------------------------------------------------\n")
print("Bienvenue Dans l'application de Gestion pour vétérinaire \n")
print("-----------------------------------------------------------\n \n")


choixaction=0
while choixaction!='q':
    print("Entrez q pour quitter l'application \n")
    print("1) Insérer des données \n2) Consulter des données \n")
    choixaction=input("Que souhaitez vous faire ? ")
    if choixaction=='1':
        choix=0
        while choix!='m':
            print("\nMaintenant, souhaitez-vous...\n")
            print("1) Insérer un membre du personnel\n")
            print("2) Insérer un client\n")
            print("3) Insérer une information de propriétaire pour un animal\n")
            print("4) Insérer un médicament\n")
            print("5) Insérer un membre du personnel\n")
            print("6) Insérer une entrée dans un dossier médical\n")
            print("Pour revenir au menu principal, entrez m\n")
            choix=input("Choix ?  ")
            if choix=='1' :
                i1()
            elif choix=='2' :
                i2()
            elif choix=='3' :
                i3()
            elif choix=='4' :
                i4()
            elif choix=='5' :
                i5()
            elif choix=='6' :
                i6()
            elif choix=='m' :
                print("Retour au menu principal\n")
            else:
                print("Choix invalide, veuillez réessayer\n")
    elif choixaction=='2' :
        choix=0
        while choix!='m':
            print("\nMaintenant, souhaitez-vous...\n")
            print("1) Lister les quantités de médicaments consommés pour une période donnée\n")
            print("2) Lister le nombre de traitements prescrits au cours d'une période donnée\n")
            print("3) Lister les procédures effectuées sur un animal donné, avec et triées par date.\n")
            print("4) Compter le nombre d'animaux traités groupés par espèce. \n")
            print("5) Lister les animaux ayant appartenus à un client donné. \n")
            print("6) Lister les animaux appartenant actuellement à un client donné. \n")
            print("7) Lister les animaux ayant appartenus mais n'appartenant plus à un client donné. \n")
            print("8) Lister l'évolution de croissance taille et poids d'un animal donné, par ordre chronologique. \n")
            print("9) Lister les traitements subis par un animal donné  \n")
            print("10) Lister les traitements en cours pour un animal donné,  \n")
            print("11) Lister les membres de personnel spécialisés dans les reptiles \n")
            print("12) Afficher la liste des animaux ayant été suivis par un vétérinaire donné au cours du dernier mois \n")
            print("13) Afficher la liste des vétérinaires ayant suivi un animal donné \n")
            print("Pour revenir au menu principal, entrez m\n")
            choix=input("Choix ?  ")
            if choix=='1' :
                s1()
            elif choix=='2' :
                s2()
            elif choix=='3' :
                s3()
            elif choix=='4' :
                s4()
            elif choix=='5' :
                s5()
            elif choix=='6' :
                s6()
            elif choix=='7' :
                s7()
            elif choix=='8' :
                s8()
            elif choix=='9' :
                s9()
            elif choix=='10' :
                s10()
            elif choix=='11':
                s11()
            elif choix=='12':
                s12()
            elif choix=='13':
                s13()
            print("\nNow sleeping for 3s (pour lire les infos)\n")
            time.sleep(3)
    elif choixaction=='q' :
         print("Fermeture de l'application")
    else :
        print("Choix invalide, veuillez réessayer\n")

    
