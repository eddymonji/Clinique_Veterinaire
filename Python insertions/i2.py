#charger le module psycopg2
import psycopg2 
#connexion sur la BD 
conn = psycopg2.connect("dbname = 'dbnf18a042' user= 'nf18a042' host = 'tuxa.sme.utc' password = 'aKlQ6ckN'")
#ouvir un curseur
cur = conn.cursor() 
nom = input("Entrez le nom du client: ")
prenom = input("Entrez le prenom du personnel: ")
date_naissance = input("Entrez la date naissance format YYYY-MM-DD : ")
adresse = input("Entrez l'adresse : ")
telephone = input("Entrez le numéro de téléphone : ")
#ecrire le code sql
sql = "INSERT INTO Client(nom, prenom, date_naissance, adresse, telephone ) \
     VALUES ( '%s', '%s', '%s', '%s', %d) ;\
    "%(nom, prenom, date_naissance, adresse, telephone)
cur.execute(sql)
conn.commit()
conn.close()
