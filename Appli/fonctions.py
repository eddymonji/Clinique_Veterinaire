import psycopg2
#i1 -----------
#connexion sur la BD
conn = psycopg2.connect("dbname = 'dbnf18a044' user= 'nf18a044' host = 'tuxa.sme.utc' password = 'tDLssh0N'")
#ouvir un curseur
cur = conn.cursor()

def affichesql(result):
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

def i1():
    nom = input("Entrez le nom du personnel: ")
    prenom = input("Entrez le prenom du personnel: ")
    date_naissance = input("Entrez la date naissance format YYYY-MM-DD : ")
    adresse = input("Entrez l'adresse : ")
    telephone = input("Entrez le numéro de téléphone : ")
    poste = input("Entrez 'True' pour vétérinaire, 'False' pour assitant : ")

    print("\nVoici le tableau de categorie d'espece existant: ")
    cur.execute("SELECT * FROM categorie_espece")
    result = cur.fetchall()
    affichesql(result)

    categorie_espece = input("Ce personnel est spécialisé dans quelle catégorie? Entrez l'id de catégorie : ")
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
    nom = input("Entrez le nom du client: ")
    prenom = input("Entrez le prenom du personnel: ")
    date_naissance = input("Entrez la date naissance format YYYY-MM-DD : ")
    adresse = input("Entrez l'adresse : ")
    telephone = input("Entrez le numéro de téléphone : ")
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
    print("Bonjour. Bienvenue à l'insertion de l'information de propriétaire pour un animal")

    print("Voici le tableau de l'animal existant: ")
    cur.execute("SELECT * FROM Animal")
    result = cur.fetchall()

    affichesql(result)
    animal = input("Entrez l'id de l'animal ciblé: ")

    print("\nVoici le tableau de client existant: ")
    cur.execute("SELECT * FROM Client")
    result = cur.fetchall()
    affichesql(result)

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
    nom = input("Entrez le nom de l'animal: ")
    date_naissance = input("Entrez la date naissance format YYYY-MM-DD : ")
    num_puce = input("Entrez le num puce : ")
    num_passeport = input("Entrez le numéro de passeport : ")

    print("\nVoici le tableau de categorie d'espece existant: ")
    cur.execute("SELECT * FROM categorie_espece")
    result = cur.fetchall()
    affichesql(result)

    categorie_espece = input("Entrez la catégorie d'espèce : ")

    #ecrire le code sql
    sql = "INSERT INTO Animal (nom, date_naissance, num_puce, num_passeport, categorie_espece)\
        VALUES ( '%s', '%s', %d, %d, %d) ;\
        "%(nom, date_naissance, num_puce, num_passeport, categorie_espece)
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("Médicament inséré avec succès")

#i5 ----------------
def i5():
    nom = input("Entrez le nom du medicament: ")
    description = input("Entrez la description: ")
    #ecrire le code sql
    sql = "INSERT INTO medicament(nom, description)\
        VALUES ('%s', '%s') ;\
        "%(nom, description)
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("Membre du personnel inséré avec succès")

#i6 -------------------
def i6():
    print("\nVoici le tableau de l'animal existant: ")
    cur.execute("SELECT * FROM Animal")
    result = cur.fetchall()
    affichesql(result)

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
    print("Dossier médical inséré avec succès")

def s1():
    dateDebut = input("Entrez la date de debut format YYYY-MM-DD: ")
    dateFin = input("Entrez la date de fin format YYYY-MM-DD: ")
    sql = "SELECT d.medicament , d.quantite , t.debut , t.fin\
        FROM  Dosage d\
        INNER JOIN Traitement t ON d.traitement = t.id_traitement\
        WHERE t.debut >= '%s'  AND t.fin <= '%s'\
        ORDER BY d.quantite DESC , t.debut DESC , t.fin DESC"%(dateDebut,dateFin)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result)

def s2():
    dateDebut = input("Entrez la date de debut format YYYY-MM-DD: ")
    dateFin = input("Entrez la date de fin format YYYY-MM-DD: ")
    sql = "SELECT t.nom, COUNT(traitement) AS nombre_traitement\
        FROM traitement t\
        INNER JOIN dossier_traitement d  ON t.id_traitement = d.traitement\
        WHERE t.debut >= '%s' AND t.fin <= '%s'\
        GROUP BY t.nom\
        ORDER BY  nombre_traitement"%(dateDebut,dateFin)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result)

def s3():
    print("\nVoici le tableau de l'animal existant: ")
    cur.execute("SELECT * FROM Animal")
    result = cur.fetchall()
    affichesql(result)

    nomAni = input("Entrez le nom de l'animal ciblé: ")

    sql = "SELECT a.nom AS Animal,p.nom AS procedure, d.date\
        FROM Procedure p\
        INNER JOIN Dossier_Medical d ON p.id_procedure = d.procedure\
        INNER JOIN Animal a ON d.animal = a.id_animal\
        WHERE a.nom = '%s'\
        ORDER BY p.nom , d.date DESC"%(nomAni)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result)

def s4():
    sql = "SELECT COUNT(Animal) AS Nombre_Traite , c.nom_categorie\
        FROM categorie_espece c\
        INNER JOIN Animal a ON c.id_categorie = a.categorie_espece\
        INNER JOIN Historique_Veto h ON a.id_animal = h.animal\
        GROUP BY c.nom_categorie"
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result)



def s5():
    print("\nVoici le tableau des clients existants: ")
    cur.execute("SELECT * FROM client")
    result = cur.fetchall()
    affichesql(result)
    nomCli = input("Entrez le nom du client ciblé: ")
    prenomCli = input("Entrez le prénom du client ciblé: ")
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
    affichesql(result)


def s6():
    print("\nVoici le tableau des clients existants: ")
    cur.execute("SELECT * FROM client")
    result = cur.fetchall()
    affichesql(result)
    nomCli = input("Entrez le nom du client ciblé: ")
    prenomCli = input("Entrez le prénom du client ciblé: ")
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
    affichesql(result)



def s7():
    print("\nVoici le tableau des clients existants: ")
    cur.execute("SELECT * FROM client")
    result = cur.fetchall()
    affichesql(result)
    nomCli = input("Entrez le nom du client ciblé: ")
    prenomCli = input("Entrez le prénom du client ciblé: ")
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
    affichesql(result)

def s8():
    print("\nVoici le tableau de l'animal existant: ")
    cur.execute("SELECT * FROM Animal")
    result = cur.fetchall()
    affichesql(result)

    nomAni = input("Entrez le nom de l'animal ciblé: ")

    sql = "SELECT taille, poids, date, heure FROM Dossier_Medical d\
        INNER JOIN Animal a ON a.id_animal = d.animal\
        WHERE a.nom = '%s'\
        ORDER BY date, heure ASC ;"%(nomAni)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result)

def s9():
    print("\nVoici le tableau de l'animal existant: ")
    cur.execute("SELECT * FROM Animal")
    result = cur.fetchall()
    affichesql(result)

    nomAni = input("Entrez le nom de l'animal ciblé: ")

    sql = "SELECT t.nom, debut, fin FROM Traitement t\
        INNER JOIN Dossier_Traitement d ON t.id_traitement = d.traitement\
        INNER JOIN Animal a ON a.id_animal = d.dossier_medical\
        WHERE a.nom = '%s'\
        GROUP BY t.nom, debut, fin\
        ORDER BY debut ASC, fin ASC ;"%(nomAni)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result)

def s10():
    print("\nVoici le tableau de l'animal existant: ")
    cur.execute("SELECT * FROM Animal")
    result = cur.fetchall()
    affichesql(result)

    nomAni = input("Entrez le nom de l'animal ciblé: ")

    sql = "SELECT t.nom, debut, fin FROM Traitement t\
        INNER JOIN Dossier_Traitement d ON t.id_traitement = d.traitement\
        INNER JOIN Animal a ON a.id_animal = d.dossier_medical\
        WHERE a.nom = '%s' AND fin > CURRENT_TIMESTAMP\
        GROUP BY t.nom, debut, fin\
        ORDER BY debut ASC, fin ASC;"%(nomAni)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result)

def s11():
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
    affichesql(result)

def s12():

    print("\nVoici le tableau de vétérinaire existant: ")
    cur.execute("SELECT * FROM Personnel WHERE poste = 'True' ")
    result = cur.fetchall()
    affichesql(result)

    nomVet = input("Entrez le nom de vétérinaire ciblé: ")
    prenomVet = input("Entrez le prenom de vétérinaire ciblé: ")

    sql = "SELECT a.nom, a.date_naissance, num_puce, num_passeport, nom_categorie\
        FROM Animal a\
        INNER JOIN historique_veto h ON a.id_animal = h.animal\
        INNER JOIN Personnel p ON h.personnel = p.id_personnel\
        INNER JOIN Categorie_Espece c ON a.categorie_espece = c.id_categorie\
        WHERE p.nom = '%s' AND p.prenom = '%s';" %(nomVet,prenomVet)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result)

def s13():
    print("\nVoici le tableau de l'animal existant: ")
    cur.execute("SELECT * FROM Animal")
    result = cur.fetchall()
    affichesql(result)

    nomAni = input("Entrez le nom de l'animal ciblé: ")

    sql = "SELECT p.nom, prenom, p.date_naissance, adresse, telephone, poste, nom_categorie, date_debut FROM Personnel p\
        INNER JOIN historique_veto h ON p.id_personnel = h.personnel\
        INNER JOIN Animal a ON h.animal =  a.id_animal\
        INNER JOIN Categorie_Espece c ON p.categorie_espece = c.id_categorie\
        WHERE a.nom =  '%s' AND p.poste =  'True'\
        ORDER BY date_debut ASC;"%(nomAni)
    cur.execute(sql)
    result = cur.fetchall()
    affichesql(result)
