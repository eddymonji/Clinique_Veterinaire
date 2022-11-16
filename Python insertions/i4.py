#charger le module psycopg2
import psycopg2 
#connexion sur la BD 
conn = psycopg2.connect("dbname = 'dbnf18a042' user= 'nf18a042' host = 'tuxa.sme.utc' password = 'aKlQ6ckN'")
#ouvir un curseur
cur = conn.cursor() 
nom = input("Entrez le nom de l'animal: ")
date_naissance = input("Entrez la date naissance format YYYY-MM-DD : ")
num_puce = input("Entrez le num puce : ")
num_passeport = input("Entrez le numéro de passeport : ")

print("\nVoici le tableau de categorie d'espece existant: ")
cur.execute("SELECT * FROM categorie_espece")
result = cur.fetchall()
for x in result:
  print(x)

categorie_espece = input("Entrez la catégorie d'espèce : ")

#ecrire le code sql
sql = "INSERT INTO Animal (nom, date_naissance, num_puce, num_passeport, categorie_espece)\
     VALUES ( '%s', '%s', %d, %d, %d) ;\
    "%(nom, date_naissance, num_puce, num_passeport, categorie_espece)
cur.execute(sql)
conn.commit()
conn.close()
