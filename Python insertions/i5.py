#charger le module psycopg2
import psycopg2 
#connexion sur la BD 
conn = psycopg2.connect("dbname = 'dbnf18a042' user= 'nf18a042' host = 'tuxa.sme.utc' password = 'aKlQ6ckN'")
#ouvir un curseur
cur = conn.cursor() 
nom = input("Entrez le nom du medicament: ")
description = input("Entrez la description: ")
#ecrire le code sql
sql = "INSERT INTO medicament(nom, description)\
     VALUES ('%s', '%s') ;\
    "%(nom, description)
cur.execute(sql)
conn.commit()
conn.close()
