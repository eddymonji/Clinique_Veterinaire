#charger le module psycopg2
import psycopg2 
#connexion sur la BD 
conn = psycopg2.connect("dbname = 'dbnf18a042' user= 'nf18a042' host = 'tuxa.sme.utc' password = 'aKlQ6ckN'")
#ouvir un curseur
cur = conn.cursor() 
print("Bonjour. Bienvenue à l'insertion de l'information de propriétaire pour un animal")

print("Voici le tableau de l'animal existant: ")
cur.execute("SELECT * FROM Animal")
result = cur.fetchall()
for x in result:
  print(x)

animal = input("Entrez l'id de l'animal ciblé: ")

print("\nVoici le tableau de client existant: ")
cur.execute("SELECT * FROM Client")
result = cur.fetchall()
for x in result:
  print(x)

client = input("Entrez l'id du personnel ciblé: ")

debut = input("Entrez la date de debut format YYYY-MM-DD : ")
fin = input("Entrez la date de fin format YYYY-MM-DD : ")

#ecrire le code sql
sql = "INSERT INTO Proprietaire (animal, client, debut, fin)\
     VALUES ( %s, %s, '%s', '%s') ;\
    "%(animal, client, debut, fin)
cur.execute(sql)
conn.commit()
conn.close()
print("Information de propriétaire inséré avec succès.")