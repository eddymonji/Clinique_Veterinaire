--Requête 1 :
--par exemple

SELECT d.medicament , d.quantite , t.debut , t.fin
FROM  Dosage d
INNER JOIN Traitement t ON d.traitement = t.id_traitement
WHERE t.debut >= '2020-12-12'  AND t.fin <= '2022-10-12'
ORDER BY d.quantite DESC , t.debut DESC , t.fin DESC

--Requête 2 :
--correction
1)SELECT t.nom, COUNT(traitement) AS nombre_traitement
FROM traitement t
INNER JOIN dossier_traitement d  ON t.id_traitement = d.traitement
WHERE t.debut >= '2020-12-12'  AND t.fin <= '2022-10-12'
GROUP BY t.nom
ORDER BY nombre_traitement

--Requête 3 :

SELECT a.nom AS Animal,p.nom AS procedure, d.date
FROM Procedure p
INNER JOIN Dossier_Medical d ON p.id_procedure = d.procedure
INNER JOIN Animal a ON d.animal = a.id_animal
WHERE a.nom = 'Rex'
ORDER BY p.nom , d.date DESC

--Requête 4 :

SELECT COUNT(Animal) AS Nombre_Traite , c.nom_categorie
FROM categorie_espece c
INNER JOIN Animal a ON c.id_categorie = a.categorie_espece
INNER JOIN Historique_Veto h ON a.id_animal = h.animal
GROUP BY c.nom_categorie


--Requête 5:
--Par exemple avec client “Dubois Christ”
SELECT client.nom AS nom_Client, client.prenom AS prenom_client, a.nom AS nom_animal, categorie_espece.nom_categorie AS espece_animal, proprietaire.debut AS date_adoption, a.date_naissance, num_puce, num_passeport 
FROM animal a
INNER JOIN categorie_espece ON a.categorie_espece = categorie_espece.id_categorie
INNER JOIN proprietaire ON a.id_animal = proprietaire.animal
INNER JOIN client ON client.id_client = proprietaire.client
WHERE client.nom = 'Dubois' AND client.prenom = 'Christ'
ORDER BY proprietaire.debut DESC;


--Requête 6 :
--Par exemple avec client “Dubois Christ”
SELECT client.nom AS nom_Client, client.prenom AS prenom_client, a.nom AS nom_animal, categorie_espece.nom_categorie AS espece_animal, proprietaire.debut AS date_adoption, a.date_naissance, num_puce, num_passeport 
FROM animal a
INNER JOIN categorie_espece ON a.categorie_espece = categorie_espece.id_categorie
INNER JOIN proprietaire ON a.id_animal = proprietaire.animal
INNER JOIN client ON client.id_client = proprietaire.client
WHERE client.nom = 'Dubois' AND client.prenom = 'Christ'
AND proprietaire.fin ISNULL
ORDER BY proprietaire.debut DESC;




--Requête 7 :
--Par exemple avec client “Dubois Christ”
SELECT client.nom AS nom_Client, client.prenom AS prenom_client, a.nom AS nom_animal, categorie_espece.nom_categorie AS espece_animal, proprietaire.debut AS date_adoption, a.date_naissance, num_puce, num_passeport
FROM animal a
INNER JOIN categorie_espece ON a.categorie_espece = categorie_espece.id_categorie
INNER JOIN proprietaire ON a.id_animal = proprietaire.animal
INNER JOIN client ON client.id_client = proprietaire.client
WHERE proprietaire.fin < CURRENT_TIMESTAMP
AND client.nom = 'Dubois' AND client.prenom = 'Christ'
ORDER BY proprietaire.debut DESC ;




--Requête 8:
--Par exemple si l’animal demandé est « Rex »
 
SELECT taille, poids, date, heure FROM Dossier_Medical d
INNER JOIN Animal a ON a.id_animal = d.animal
WHERE a.nom = 'Rex'
ORDER BY date, heure ASC ;

--Requête 9:
--Données pour tester:
INSERT INTO Dossier_Traitement (dossier_medical, traitement) VALUES (1, 1);
INSERT INTO Dossier_Traitement (dossier_medical, traitement) VALUES (1, 3);

--Par exemple si l’animal demandé est « Rex »
SELECT t.nom, debut, fin FROM Traitement t
INNER JOIN Dossier_Traitement d ON t.id_traitement = d.traitement
INNER JOIN Animal a ON a.id_animal = d.dossier_medical
WHERE a.nom = 'Rex'
GROUP BY t.nom, debut, fin
ORDER BY debut ASC, fin ASC ;
 
 
--Requête 10:
--Par exemple si l’animal est “Rex”
 
--Données pour tester:
INSERT INTO Traitement (nom, debut, fin)
VALUES ('Antivirus', '2022-08-12', '2022-12-30');
INSERT INTO Dossier_Traitement (dossier_medical, traitement)
VALUES (1, 4);
 
 
SELECT t.nom, debut, fin FROM Traitement t
INNER JOIN Dossier_Traitement d ON t.id_traitement = d.traitement
INNER JOIN Animal a ON a.id_animal = d.dossier_medical
WHERE a.nom = 'Rex' AND fin > CURRENT_TIMESTAMP
GROUP BY t.nom, debut, fin
ORDER BY debut ASC, fin ASC; 
 
 
--Requête 11: 
--Données pour tester:
INSERT INTO Personnel(nom, prenom, date_naissance, adresse, telephone , poste, categorie_espece)
VALUES ( 'John', 'Appleseed', '1997-01-02', ' Californie', 0758395738,'True',3) ;
 
SELECT nom, prenom, date_naissance, adresse, telephone,
CASE
	WHEN poste = 'True' THEN 'Veterinaire'
	WHEN poste = 'False' THEN 'Assistant'
	ELSE 'Data error'
END as poste
FROM Personnel p
INNER JOIN Categorie_Espece c ON p.categorie_espece = c.id_categorie
WHERE c.nom_categorie =  'Reptiles';
 
 
 
 
--Requête 12:

--Par exemple si le vétérinaire est “Alexandre Dico”
SELECT a.nom, a.date_naissance, num_puce, num_passeport, nom_categorie
FROM Animal a
INNER JOIN historique_veto h ON a.id_animal = h.animal
INNER JOIN Personnel p ON h.personnel = p.id_personnel
INNER JOIN Categorie_Espece c ON a.categorie_espece = c.id_categorie
WHERE p.nom = 'Alexandre' AND p.prenom = 'Dico';
 
 
--Requête 13:
--Par exemple pour animal ‘Rex’:
 
SELECT p.nom, prenom, p.date_naissance, adresse, telephone, poste, nom_categorie, date_debut FROM Personnel p
INNER JOIN historique_veto h ON p.id_personnel = h.personnel
INNER JOIN Animal a ON h.animal =  a.id_animal 
INNER JOIN Categorie_Espece c ON p.categorie_espece = c.id_categorie
WHERE a.nom =  'Rex' AND p.poste =  'True'
ORDER BY date_debut ASC;
