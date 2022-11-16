#charger le module psycopg2
import psycopg2 
#connexion sur la BD 
conn = psycopg2.connect("dbname = 'dbnf18a042' user= 'nf18a042' host = 'tuxa.sme.utc' password = 'aKlQ6ckN'")
#ouvir un curseur
cur = conn.cursor() 
nom = input("Entrez le nom du personnel: ")
prenom = input("Entrez le prenom du personnel: ")
date_naissance = input("Entrez la date naissance format YYYY-MM-DD : ")
adresse = input("Entrez l'adresse : ")
telephone = input("Entrez le numéro de téléphone : ")
poste = input("Entrez 'True' pour vétérinaire, 'False' pour assitant : ")


print("\nVoici le tableau de categorie d'espece existant: ")
cur.execute("SELECT * FROM categorie_espece")
result = cur.fetchall()
for x in result:
  print(x)


categorie_espece = input("Ce personnel est spécialisé dans quelle catégorie? Entrez l'id de catégorie : ")
#ecrire le code sql
sql = "INSERT INTO Personnel(nom, prenom, date_naissance, adresse, telephone , poste, categorie_espece)\
     VALUES ( '%s', '%s', '%s', '%s', %s,'%s',%s) ;\
    "%(nom, prenom, date_naissance, adresse, telephone, poste, categorie_espece)
cur.execute(sql)
conn.commit()
conn.close()
print("Personnel inséré avec succès")
