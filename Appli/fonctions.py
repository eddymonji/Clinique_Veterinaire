import psycopg2, string, re
#connexion sur la BD
from datetime import datetime

def affichesql(result, cur):
    largeur = []
    colonnes = []
    tavnit = '|'
    separateur = '+'
    i = 0
    for cd in cur.description:
        espace = list(map(lambda x: len(str(x[i])), result))
        if len(espace) > 0:
            max_col_length = max(espace)
            largeur.append(max(max_col_length, len(cd[0])))
            colonnes.append(cd[0])
            i +=1
        else:
            print("La table résultat est actuellement null")
            return -1

    for w in largeur:
        tavnit += " %-"+"%s.%ss |" % (w,w)
        separateur += '-'*w + '--+'

    print(separateur)
    print(tavnit % tuple(colonnes))
    print(separateur)
    for row in result:
        print(tavnit % row)
    print(separateur)

def inputTele(message):
    sortie = input(message)
    pattern = r"^0[0-9]{9}$"
    while not (sortie.strip().isdigit() and re.match(pattern, sortie)):
        print("Erreur: L'entrée n'est pas de type numéro de téléphone de 10 chiffres, qui commence par 0")
        sortie = input("Veuillez retaper: ")
    return sortie



    
def inputInt(message):
    sortie = input(message)
    while not sortie.strip().isdigit():
        print("Erreur: L'entrée n'est pas de type nombre")
        sortie = input("Veuillez retaper: ")
    return sortie

def inputAlpha(message):
    sortie = input(message)
    while not all(x.isalpha() or x.isspace() for x in sortie):
        print("Erreur: L'entrée n'est pas de type Alphabets ou espace.")
        sortie = input("Veuillez retaper: ")
    return sortie


def inputDate(message):
    sortie = input(message)
    format = '%Y-%m-%d'
    res = True
    try:
        res = bool(datetime.strptime(sortie, format))
    except ValueError:
        res = False
    while not res:
        print("Erreur: Format Date incorrect. Entrez la date format YYYY-MM-DD")
        sortie = input("Veuillez retaper: ")
        try:
            res = bool(datetime.strptime(sortie, format))
        except ValueError:
            res = False
    return sortie

def inputHeure(message):
    sortie = input(message)
    pattern = r'^(([01]\d|2[0-3]):([0-5]\d)|24:00):([0-5]\d)$'
    while not (re.match(pattern, sortie)):
        print("Erreur: L'entrée n'est pas de type heure, qui est HH:MM:SS")
        sortie = input("Veuillez retaper: ")
    return sortie

def inputBool(message):
    sortie = input(message)
    while not (sortie.strip() == "True" or sortie.strip() == "False"):
        print("Erreur: L'entrée n'est pas de type 'True' or 'False'.")
        sortie = input("Veuillez retaper: ")   
    return sortie



def i1():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()

    nom = inputAlpha("Entrez le nom du personnel: ")
    prenom = inputAlpha("Entrez le prenom du personnel: ")
    date_naissance = inputDate("Entrez la date naissance format YYYY-MM-DD : ")
    adresse = input("Entrez l'adresse : ")
    telephone = inputTele("Entrez le numéro de téléphone : ")
    poste = inputBool("Entrez 'True' pour vétérinaire, 'False' pour assitant : ")

    print("\nVoici le tableau de categorie d'espece existant: ")
    cur.execute("SELECT * FROM categorie_espece")
    result = cur.fetchall()
    affichesql(result, cur)

    categorie_espece = inputInt("Ce personnel est spécialisé dans quelle catégorie? Entrez l'id de catégorie : ")
    #ecrire le code sql
    sql = "INSERT INTO Personnel(nom, prenom, date_naissance, adresse, telephone , poste, categorie_espece)\
        VALUES ('%s', '%s', '%s', '%s', %s,'%s',%s) ;\
        "%(nom, prenom, date_naissance, adresse, telephone, poste, categorie_espece)
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("Personnel inséré avec succès")

#i2-----------------
def i2():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()

    nom = inputAlpha("Entrez le nom du client: ")
    prenom = inputAlpha("Entrez le prenom du personnel: ")
    date_naissance = inputDate("Entrez la date naissance format YYYY-MM-DD : ")
    adresse = input("Entrez l'adresse : ")
    telephone = inputTele("Entrez le numéro de téléphone : ")
    #ecrire le code sql
    sql = "INSERT INTO Client(nom, prenom, date_naissance, adresse, telephone ) \
        VALUES ( '%s', '%s', '%s', '%s', %s) ;\
        "%(nom, prenom, date_naissance, adresse, telephone)
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("Client inséré avec succès")

#i3-----------------

def i3():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()

    print("Bonjour. Bienvenue à l'insertion de l'information de propriétaire pour un animal")

    print("Voici le tableau de l'animal existant: ")
    cur.execute("SELECT * FROM Animal")
    result = cur.fetchall()

    affichesql(result, cur)
    animal = inputInt("Entrez l'id de l'animal ciblé: ")

    print("\nVoici le tableau de client existant: ")
    cur.execute("SELECT * FROM Client")
    result = cur.fetchall()
    affichesql(result, cur)

    client = inputInt("Entrez l'id du propriétaire ciblé: ")

    debut = inputDate("Entrez la date de debut format YYYY-MM-DD : ")
    fin = inputDate("Entrez la date de fin format YYYY-MM-DD (rien si c'est le propriétaire actuel : ")
    #rajouter if pour null
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
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()

    nom = inputAlpha("Entrez le nom de l'animal: ")
    date_naissance = inputDate("Entrez la date naissance format YYYY-MM-DD : ")
    num_puce = inputInt("Entrez le num puce : ")
    num_passeport = inputInt("Entrez le numéro de passeport : ")

    print("\nVoici le tableau de categorie d'espece existant: ")
    cur.execute("SELECT * FROM categorie_espece")
    result = cur.fetchall()
    affichesql(result, cur)

    categorie_espece = inputInt("Entrez id de catégorie d'espèce : ")

    #ecrire le code sql
    sql = "INSERT INTO Animal (nom, date_naissance, num_puce, num_passeport, categorie_espece)\
        VALUES ( '%s', '%s', %s, %s, %s) ;\
        "%(nom, date_naissance, num_puce, num_passeport, categorie_espece)
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("Animal inséré avec succès")

#i5 ----------------
def i5():
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
    print("Médicament inséré avec succès")

#i6 -------------------
def i6():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()

    print("\nVoici le tableau de l'animal existant: ")
    cur.execute("SELECT * FROM Animal")
    result = cur.fetchall()
    affichesql(result, cur)

    animal = inputInt("Entrez l'id de l'animal ciblé: ")

    taille = inputInt("\nEntrez la taille: ")
    poids = inputInt("Entrez le poids : ")
    resultat = inputAlpha("Entrez le resultat : ")
    observation = inputAlpha("Entrez l'observation: ")
    date = inputDate("Entrez la date format YYYY-MM-DD : ")
    heure = inputHeure("Entrez l'heure: ")
    procedure = inputInt("Entrez l'id du procedure: ")
    #ecrire le code sql
    sql = "INSERT INTO Dossier_Medical (animal, taille, poids, resultat, observation, date, heure, procedure)\
        VALUES ( %s, %s, %s, '%s', '%s', '%s', '%s', %s) ;\
        "%(animal, taille, poids, resultat, observation, date, heure, procedure)
    cur.execute(sql)
    conn.commit()

    print("Dossier médical inséré avec succès")
    conn.close()

def s1():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()

    dateDebut = inputDate("Entrez la date de debut format YYYY-MM-DD: ")
    dateFin = inputDate("Entrez la date de fin format YYYY-MM-DD: ")
    sql = "SELECT d.medicament , d.quantite , t.debut , t.fin\
        FROM  Dosage d\
        INNER JOIN Traitement t ON d.traitement = t.id_traitement\
        WHERE t.debut >= '%s'  AND t.fin <= '%s'\
        ORDER BY d.quantite DESC , t.debut DESC , t.fin DESC"%(dateDebut,dateFin)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result, cur)
    conn.close()

def s2():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()
    dateDebut = inputDate("Entrez la date de debut format YYYY-MM-DD: ")
    dateFin = inputDate("Entrez la date de fin format YYYY-MM-DD: ")
    sql = "SELECT t.nom, COUNT(traitement) AS nombre_traitement\
        FROM traitement t\
        INNER JOIN dossier_traitement d  ON t.id_traitement = d.traitement\
        WHERE t.debut >= '%s' AND t.fin <= '%s'\
        GROUP BY t.nom\
        ORDER BY  nombre_traitement"%(dateDebut,dateFin)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result, cur)
    conn.close()

def s3():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()
    print("\nVoici le tableau de l'animal existant: ")
    cur.execute("SELECT * FROM Animal")
    result = cur.fetchall()
    affichesql(result, cur)

    nomAni = inputAlpha("Entrez le nom de l'animal ciblé: ")

    sql = "SELECT a.nom AS Animal,p.nom AS procedure, d.date\
        FROM Procedure p\
        INNER JOIN Dossier_Medical d ON p.id_procedure = d.procedure\
        INNER JOIN Animal a ON d.animal = a.id_animal\
        WHERE a.nom = '%s'\
        ORDER BY p.nom , d.date DESC"%(nomAni)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result, cur)
    conn.close()

def s4():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()
    sql = "SELECT COUNT(Animal) AS Nombre_Traite , c.nom_categorie\
        FROM categorie_espece c\
        INNER JOIN Animal a ON c.id_categorie = a.categorie_espece\
        INNER JOIN Historique_Veto h ON a.id_animal = h.animal\
        GROUP BY c.nom_categorie"
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result, cur)
    conn.close()



def s5():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()
    print("\nVoici le tableau des clients existants: ")
    cur.execute("SELECT * FROM client")
    result = cur.fetchall()
    affichesql(result, cur)
    nomCli = inputAlpha("Entrez le nom du client ciblé: ")
    prenomCli = inputAlpha("Entrez le prénom du client ciblé: ")
    sql = "SELECT client.nom AS nom_Client, client.prenom AS prenom_client, a.nom AS nom_animal, \
        categorie_espece.nom_categorie AS espece_animal, a.date_naissance, num_puce, num_passeport \
        FROM animal a \
        INNER JOIN categorie_espece ON a.categorie_espece = categorie_espece.id_categorie\
        INNER JOIN proprietaire ON a.id_animal = proprietaire.animal\
        INNER JOIN client ON client.id_client = proprietaire.client\
        WHERE client.nom = '%s'\
        AND client.prenom = '%s';"%(nomCli,prenomCli)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result, cur)
    conn.close()


def s6():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()
    print("\nVoici le tableau des clients existants: ")
    cur.execute("SELECT * FROM client")
    result = cur.fetchall()
    affichesql(result, cur)
    nomCli = inputAlpha("Entrez le nom du client ciblé: ")
    prenomCli = inputAlpha("Entrez le prénom du client ciblé: ")
    sql = "SELECT client.nom AS nom_Client, client.prenom AS prenom_client, a.nom AS nom_animal, categorie_espece.nom_categorie AS espece_animal, a.date_naissance, num_puce, num_passeport \
        FROM animal a \
        INNER JOIN categorie_espece ON a.categorie_espece = categorie_espece.id_categorie \
        INNER JOIN proprietaire ON a.id_animal = proprietaire.animal\
        INNER JOIN client ON client.id_client = proprietaire.client\
        WHERE proprietaire.fin ISNULL\
        AND client.nom = '%s'\
        AND client.prenom = '%s';"%(nomCli,prenomCli)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result, cur)
    conn.close()



def s7():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()
    print("\nVoici le tableau des clients existants: ")
    cur.execute("SELECT * FROM client")
    result = cur.fetchall()
    affichesql(result, cur)
    nomCli = inputAlpha("Entrez le nom du client ciblé: ")
    prenomCli = inputAlpha("Entrez le prénom du client ciblé: ")
    sql = "SELECT client.nom AS nom_Client, client.prenom AS prenom_client, a.nom AS nom_animal, categorie_espece.nom_categorie AS espece_animal, a.date_naissance, num_puce, num_passeport\
        FROM animal a\
        INNER JOIN categorie_espece ON a.categorie_espece = categorie_espece.id_categorie\
        INNER JOIN proprietaire ON a.id_animal = proprietaire.animal\
        INNER JOIN client ON client.id_client = proprietaire.client\
        WHERE proprietaire.fin < CURRENT_TIMESTAMP\
        AND client.nom = '%s'\
        AND client.prenom = '%s';"%(nomCli,prenomCli)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result, cur)
    conn.close()

def s8():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()
    print("\nVoici le tableau de l'animal existant: ")
    cur.execute("SELECT * FROM Animal")
    result = cur.fetchall()
    affichesql(result, cur)

    nomAni = inputAlpha("Entrez le nom de l'animal ciblé: ")

    sql = "SELECT taille, poids, date, heure FROM Dossier_Medical d\
        INNER JOIN Animal a ON a.id_animal = d.animal\
        WHERE a.nom = '%s'\
        ORDER BY date, heure ASC ;"%(nomAni)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result, cur)
    conn.close()

def s9():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()
    print("\nVoici le tableau de l'animal existant: ")
    cur.execute("SELECT * FROM Animal")
    result = cur.fetchall()
    affichesql(result, cur)

    nomAni = inputAlpha("Entrez le nom de l'animal ciblé: ")

    sql = "SELECT t.nom, debut, fin FROM Traitement t\
        INNER JOIN Dossier_Traitement d ON t.id_traitement = d.traitement\
        INNER JOIN Animal a ON a.id_animal = d.dossier_medical\
        WHERE a.nom = '%s'\
        GROUP BY t.nom, debut, fin\
        ORDER BY debut ASC, fin ASC ;"%(nomAni)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result, cur)
    conn.close()

def s10():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()
    print("\nVoici le tableau de l'animal existant: ")
    cur.execute("SELECT * FROM Animal")
    result = cur.fetchall()
    affichesql(result, cur)

    nomAni = inputAlpha("Entrez le nom de l'animal ciblé: ")

    sql = "SELECT t.nom, debut, fin FROM Traitement t\
        INNER JOIN Dossier_Traitement d ON t.id_traitement = d.traitement\
        INNER JOIN Animal a ON a.id_animal = d.dossier_medical\
        WHERE a.nom = '%s' AND fin > CURRENT_TIMESTAMP\
        GROUP BY t.nom, debut, fin\
        ORDER BY debut ASC, fin ASC;"%(nomAni)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result, cur)
    conn.close()

def s11():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()
    sql = "SELECT nom, prenom, date_naissance, adresse, telephone,\
        CASE\
            WHEN poste = 'True' THEN 'Veterinaire'\
            WHEN poste = 'False' THEN 'Assistant'\
            ELSE 'Data error'\
        END as poste\
        FROM Personnel p\
        INNER JOIN Categorie_Espece c ON p.categorie_espece = c.id_categorie\
        WHERE c.nom_categorie = 'Reptiles';"
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result, cur)
    conn.close()

def s12():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()

    print("\nVoici le tableau de vétérinaire existant: ")
    cur.execute("SELECT * FROM Personnel WHERE poste = 'True' ")
    result = cur.fetchall()
    affichesql(result, cur)

    nomVet = inputAlpha("Entrez le nom de vétérinaire ciblé: ")
    prenomVet = inputAlpha("Entrez le prenom de vétérinaire ciblé: ")

    sql = "SELECT a.nom, a.date_naissance, num_puce, num_passeport, nom_categorie\
        FROM Animal a\
        INNER JOIN historique_veto h ON a.id_animal = h.animal\
        INNER JOIN Personnel p ON h.personnel = p.id_personnel\
        INNER JOIN Categorie_Espece c ON a.categorie_espece = c.id_categorie\
        WHERE p.nom = '%s' AND p.prenom = '%s';" %(nomVet,prenomVet)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result, cur)
    conn.close()

def s13():
    conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
    #ouvir un curseur
    cur = conn.cursor()
    print("\nVoici le tableau de l'animal existant: ")
    cur.execute("SELECT * FROM Animal")
    result = cur.fetchall()
    affichesql(result, cur)

    nomAni = inputAlpha("Entrez le nom de l'animal ciblé: ")

    sql = "SELECT p.nom, prenom, p.date_naissance, adresse, telephone, poste, nom_categorie, date_debut FROM Personnel p\
        INNER JOIN historique_veto h ON p.id_personnel = h.personnel\
        INNER JOIN Animal a ON h.animal =  a.id_animal\
        INNER JOIN Categorie_Espece c ON p.categorie_espece = c.id_categorie\
        WHERE a.nom =  '%s' AND p.poste =  'True'\
        ORDER BY date_debut ASC;"%(nomAni)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result, cur)
    conn.close()