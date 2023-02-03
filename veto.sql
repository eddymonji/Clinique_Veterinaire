CREATE TABLE Client (
id_client SERIAL PRIMARY KEY,
nom VARCHAR(25),
prenom VARCHAR(25),
date_naissance DATE NOT NULL,
adresse VARCHAR(30),
telephone BIGINT
);

CREATE TABLE Medicament (
nom VARCHAR(30) PRIMARY KEY,
description VARCHAR(200)
);

CREATE TABLE Categorie_Espece (
id_categorie SERIAL PRIMARY KEY,
nom_categorie VARCHAR(30)
);


CREATE TABLE Animal (
id_animal SERIAL PRIMARY KEY,
nom VARCHAR(30),
date_naissance DATE,
num_puce INTEGER,
num_passeport INTEGER,
CONSTRAINT num_animal_unique UNIQUE (id_animal,num_puce,num_passeport), 
categorie_espece INTEGER NOT NULL,
FOREIGN KEY (categorie_espece) REFERENCES Categorie_Espece(id_categorie)
);

CREATE TABLE Personnel (
id_personnel SERIAL PRIMARY KEY,
nom VARCHAR(30),
prenom VARCHAR(30),
date_naissance DATE NOT NULL,
adresse VARCHAR(30),
telephone BIGINT,
poste BOOLEAN NOT NULL,
categorie_espece INTEGER NOT NULL,
FOREIGN KEY (categorie_espece) REFERENCES Categorie_Espece(id_categorie)
);

CREATE TABLE Historique_veto (
personnel INTEGER,
FOREIGN KEY (personnel) REFERENCES Personnel(id_personnel),
animal INTEGER,
FOREIGN KEY (animal) REFERENCES Animal(id_animal),
PRIMARY KEY (personnel, animal),
date_debut DATE
);
-- CONSTRAINT dois_etre_veterinaire CHECK (Personnel.poste =true)

CREATE TABLE Proprietaire (
animal INTEGER,
FOREIGN KEY (animal) REFERENCES Animal(id_animal),
client INTEGER,
FOREIGN KEY (client) REFERENCES Client(id_client),
PRIMARY KEY (animal, client),
debut DATE,
fin DATE,
CONSTRAINT fin_sup_debut CHECK (fin >= debut)
);

CREATE TABLE Medicament_Categorie_espece (
medicament VARCHAR(30),
FOREIGN KEY (medicament) REFERENCES Medicament(nom),
categorie INTEGER,
FOREIGN KEY (categorie) REFERENCES Categorie_Espece(id_categorie),
PRIMARY KEY (medicament, categorie)
);

CREATE TABLE Procedure (
	id_procedure SERIAL PRIMARY KEY,
	nom	VARCHAR(30),
	description	TEXT
);

CREATE TABLE Dossier_medical (
	animal	INTEGER PRIMARY KEY,
	taille	FLOAT,
	poids	FLOAT,
	resultat	TEXT,
	observation	TEXT, 
	procedure	INTEGER NOT NULL,
	date  DATE,
	heure TIME,
	FOREIGN KEY(animal) REFERENCES Animal(id_animal),
	FOREIGN KEY(procedure) REFERENCES Procedure(id_procedure),
	CONSTRAINT taille CHECK (taille > 0),
	CONSTRAINT poids CHECK (poids > 0)
);


CREATE TABLE Traitement (
	id_traitement	SERIAL PRIMARY KEY,
	nom VARCHAR(30),
	debut DATE,
	fin  DATE
    CONSTRAINT fin_sup_debut CHECK (fin >= debut)
);


CREATE TABLE Dossier_traitement (
	dossier_medical	INTEGER,
	traitement	INTEGER,
	FOREIGN KEY(dossier_medical) REFERENCES Dossier_medical(animal),
	FOREIGN KEY(traitement) REFERENCES Traitement(id_traitement),
	PRIMARY KEY(dossier_medical,traitement)
);


CREATE TABLE Veterinaire_Traitement (
	traitement	INTEGER,
	FOREIGN KEY(traitement) REFERENCES Traitement(id_traitement),
	veterinaire	INTEGER,
	FOREIGN KEY(veterinaire) REFERENCES Personnel(id_personnel),
	PRIMARY KEY(traitement,veterinaire)
);
-- CONSTRAINT dois_etre_veterinaire CHECK (Personnel poste = true)


CREATE TABLE Dosage (
	medicament	VARCHAR(30),
	traitement	INTEGER,
	quantite	FLOAT,
	PRIMARY KEY(medicament,traitement),
	FOREIGN KEY(traitement) REFERENCES Traitement(id_traitement),
	FOREIGN KEY(medicament) REFERENCES Medicament(nom),
	CONSTRAINT quantite_not_null CHECK (quantite > 0)
);


-- LES INSERTIONS:

-- INSERTION TABLE CLIENT
INSERT INTO Client(nom, prenom, date_naissance, adresse, telephone ) VALUES ( 'Robbin', 'Dabank', '2002-12-02', ' Compiegne ', 0639820427) ;
INSERT INTO Client(nom, prenom, date_naissance, adresse, telephone ) VALUES ( 'Dubois', 'Roland', '2004-08-02', 'Marseille', 0639820032) ;
INSERT INTO Client(nom, prenom, date_naissance, adresse, telephone ) VALUES ( 'Ronaldo', 'Christ', '1990-11-02', 'Lyon', 0631122331) ;
INSERT INTO Client(nom, prenom, date_naissance, adresse, telephone ) VALUES ( 'Rigobert', 'alex', '2000-12-03', 'Paris', 0639821231) ;


-- INSERTION CATEGORIE_ESPECE
INSERT INTO Categorie_Espece(nom_categorie ) VALUES ( 'Felins') ;
INSERT INTO Categorie_Espece(nom_categorie ) VALUES ( 'Canidés') ;
INSERT INTO Categorie_Espece(nom_categorie ) VALUES ( 'Reptiles') ;
INSERT INTO Categorie_Espece(nom_categorie ) VALUES ( 'Rongeur') ;


-- INSERTION TABLE PERSONNEL
INSERT INTO Personnel(nom, prenom, date_naissance, adresse, telephone , poste, categorie_espece)
 VALUES ( 'Alexandre', 'Dico', '1989-01-02', ' Toulouse', 0639812345,'True',2) ;
INSERT INTO Personnel (nom, prenom, date_naissance, adresse, telephone, poste, categorie_espece)
VALUES (' Tom B', 'Erichsen', '1969-11-06', 'New York', 0630854217, 'True', 1);
INSERT INTO Personnel (nom, prenom, date_naissance, adresse, telephone, poste, categorie_espece)
VALUES (' Tom Alan ', 'Julien', '1999-02-03', 'Tokyo', 060649217, 'False', 1);
INSERT INTO Personnel (nom, prenom, date_naissance, adresse, telephone, poste, categorie_espece)
VALUES (' Cruse', 'Sam', '1997-02-07', 'Compiegne', 060734517, 'False', 2 );
INSERT INTO Personnel(nom, prenom, date_naissance, adresse, telephone , poste, categorie_espece)
VALUES ( 'John', 'Appleseed', '1997-01-02', ' Californie', 0758395738,'True',3) ;



-- INSERTION TABLE ANIMAL
INSERT INTO Animal (nom, date_naissance, num_puce, num_passeport, categorie_espece)
VALUES ('Rex', '2013-02-10', 1234, 5678, 1);
INSERT INTO Animal (nom, date_naissance, num_puce, num_passeport, categorie_espece)
VALUES ('Min', '2016-03-05', 1123, 5045, 2);
INSERT INTO Animal (nom, date_naissance, num_puce, num_passeport, categorie_espece)
VALUES ('Mia', '2018-06-06', 1033, 6045, 4);
INSERT INTO Animal (nom, date_naissance, num_puce, num_passeport, categorie_espece)
VALUES ('Mina', '2019-06-04', 3333, 3345, 3);


-- INSERTION TABLE HISTORIQUE_VETO
INSERT INTO Historique_veto (personnel, animal, date_debut)
VALUES (2, 1, '2021-09-12');
INSERT INTO Historique_veto (personnel, animal, date_debut)
VALUES (3, 2, '2019-02-21');
INSERT INTO Historique_veto (personnel, animal, date_debut)
VALUES (1, 3, '2018-06-11');
INSERT INTO Historique_veto (personnel, animal, date_debut)
VALUES (4, 4, '2019-06-11');


-- INSERTION TABLE PROPRIETAIRE
INSERT INTO Proprietaire (animal, client, debut, fin)
VALUES (1, 2, '2017-03-11', '2019-06-29');
INSERT INTO Proprietaire (animal, client, debut, fin)
VALUES (2, 1, '2016-02-10', '2017-05-12');
INSERT INTO Proprietaire (animal, client, debut, fin)
VALUES (3, 4, '2019-02-10', '2019-10-11');
INSERT INTO Proprietaire (animal, client, debut, fin)
VALUES (4, 3, '2020-02-10', '2021-05-01');


-- INSERTION TABLE MEDICAMENT
INSERT INTO medicament(nom, description)
VALUES ('Charoux', 'Medicament contre la grippe');
INSERT INTO medicament(nom, description)
VALUES ('Nhamol', 'Medicament contre les douleurs musculaires');
INSERT INTO medicament(nom, description)
VALUES ('Raphaol', 'Medicament contre les demagaisons de la queue');
INSERT INTO medicament(nom, description)
VALUES ('Eddol', 'Medicament contre la viellesse');


-- INSERTION TABLE TRAITEMENT
INSERT INTO Traitement (nom, debut, fin)
VALUES ('Antibacterien', '2020-02-10', '2020-04-12');
INSERT INTO Traitement (nom, debut, fin)
VALUES ('Anti-inflammatoire', '2021-02-11', '2021-06-12');
INSERT INTO Traitement (nom, debut, fin)
VALUES ('Anti-douleur', '2019-03-21', '2019-07-12');
INSERT INTO Traitement (nom, debut, fin)
VALUES ('Antivirus', '2022-08-12', '2022-12-30');



-- INSERTION TABLE DOSAGE
INSERT INTO Dosage (medicament, traitement, quantite)
VALUES ('Charoux', '1', 4);
INSERT INTO Dosage (medicament, traitement, quantite)
VALUES ('Nhamol', '2', 3);
INSERT INTO Dosage (medicament, traitement, quantite)
VALUES ('Raphaol', '3', 5);


-- INSERTION TABLE MEDICAMENT
INSERT INTO Medicament_Categorie_espece (medicament, categorie)
VALUES ('Eddol', 2);
INSERT INTO Medicament_Categorie_espece (medicament, categorie)
VALUES ('Nhamol', 4);
INSERT INTO Medicament_Categorie_espece (medicament, categorie)
VALUES ('Raphaol', 1);


-- INSERTION TABLE PROCEDURE
INSERT INTO Procedure (nom, description)
VALUES ('sterilisation', 'Steriliser un animal');
INSERT INTO Procedure (nom, description)
VALUES ('vaccination', 'Vaccination type B52');


-- INSERTION TABLE DOSSIER_MEDICAL
INSERT INTO Dossier_Medical (animal, taille, poids, resultat, observation, date, heure, procedure)
VALUES (1, 30, 5, 'succes', 'normale', '2022-05-12', '13:30', 2);
INSERT INTO Dossier_Medical (animal, taille, poids, resultat, observation, date, heure, procedure)
VALUES (2, 50, 8, 'succes', 'normale', '2022-06-09', '11:30', 1);

-- INSERTION TABLE DOSSIER_TRAITEMENT
INSERT INTO Dossier_Traitement (dossier_medical, traitement)
VALUES (1, 2);
INSERT INTO Dossier_Traitement (dossier_medical, traitement)
VALUES (2, 1);
INSERT INTO Dossier_Traitement (dossier_medical, traitement) 
VALUES (1, 1);
INSERT INTO Dossier_Traitement (dossier_medical, traitement) 
VALUES (1, 3);
INSERT INTO Dossier_Traitement (dossier_medical, traitement)
VALUES (1, 4);




-- INSERTION TABLE VETERINAIRE_TRAITEMENT
INSERT INTO Veterinaire_Traitement (traitement, veterinaire) 
VALUES (2, 1);
INSERT INTO Veterinaire_Traitement (traitement, veterinaire) 
VALUES (1, 2);
