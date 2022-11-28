import psycopg2
#i1 -----------
def i1():

    #connexion sur la BD
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
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
        VALUES ( '%s', '%s', '%s', '%s', '%s','%s','%s') ;\
        "%(nom, prenom, date_naissance, adresse, telephone, poste, categorie_espece)
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("Personnel inséré avec succès")

#i2-----------------
def i2():
    #connexion sur la BD
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
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

#i3-----------------

def i3():
    #connexion sur la BD
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
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

#i4----------------------
def i4():
    #connexion sur la BD
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
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

#i5 ----------------
def i5():
    #connexion sur la BD
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
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

#i6 -------------------
def i6():
    #connexion sur la BD
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()
    print("Bienvenue. Insertion d'une entrée dans un dossier médical")
    print("\nVoici le tableau de l'animal existant: ")
    cur.execute("SELECT * FROM Animal")
    result = cur.fetchall()
    for x in result:
        print(x)

    animal = input("Entrez l'id de l'animal ciblé: ")

    taille = input("\nEntrez la taille: ")
    poids = input("Entrez le poids : ")
    resultat = input("Entrez le resultat : ")
    observation = input("Entrez l'observation: ")
    date = input("Entrez la date format YYYY-MM-DD : ")
    heure = input("Entrez l'heure: ")
    procedure = input("Entrez l'id du procedure: ")
    #ecrire le code sql
    sql = "INSERT INTO Dossier_Medical (animal, taille, poids, resultat, observation, date, heure, procedure)\
        VALUES ( %d, %d, %d, '%s', '%s', '%s', '%s', %d) ;\
        "%(animal, taille, poids, resultat, observation, date, heure, procedure)
    cur.execute(sql)
    conn.commit()
    conn.close()
