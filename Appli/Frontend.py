#charger le module psycopg2
import psycopg2
from fonctions import *
print("-----------------------------------------------------------\n")
print("Bienvenue Dans l'application de Gestion pour vétérinaire \n")
print("-----------------------------------------------------------\n \n")

choixaction=0
while choixaction!='q':
    print("Entrez q pour quitter l'application \n")
    print("1) Insérer des données \n2) Consulter des données \n")
    choixaction=input("Que souhaitez vous faire ? \n")
    if choixaction=='1':
        choix=0
        while choix!='m':
            print("Souhaitez-vous...\n")
            print("1) Insérer un membre du personnel\n")
            print("2) Insérer un client\n")
            print("3) Insérer une information de propriétaire pour un animal\n")
            print("4) Insérer un médicament\n")
            print("5) Insérer un membre du personnel\n")
            print("6) Insérer une entrée dans un dossier médical\n")
            print("Pour revenir au menu principal, entrez m\n")
            choix=input("Choix ?")
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
            print("Souhaitez-vous...\n")
            print("Pour revenir au menu principal, entrez m\n")
            choix=input("Choix ?")
            #mettre les requêtes du prof

    elif choixaction=='q' :
         print("Fermeture de l'application")
    else :
        print("Choix invalide, veuillez réessayer\n")
