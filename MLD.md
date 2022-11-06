## MLD (Projet Veto)
+ Client ( #id_client : Int ; nom : String ; prenom : String ; date_naissance : date ; adresse : String ; telephone : Integer)
+ Personnel ( #id_personnel : Int ; nom : String ; prenom : String ; date_naissance : date ; adresse : String ; telephone : Integer, poste : Boolean; categorie_espece => Categorie_Espece : int)  
avec categorie_espece NOT NULL et poste NOT NULL
avec poste=True pour vetérinaire et False pour assistant 
+ Animal (#id_animal : int ; nom : string ; date_naissance : Date ; num_puce : int ; num_passport : int; categorie_espece => Categorie_Espece) 
avec categorie_espece NOT NULL
+ Historique_veto(#personnel => Personnel ; #animal =>Animal ; date_debut : Date) 
avec Personnel.poste=TRUE
+ Proprietaire(#animal => Animal ; #client =>Client.Personne, date_adoption: Date )
+ Medicament (#nom : string ; description : text)
+ Traitement (#id_traitement ; début : Date ; duree : Date ; nom : String)
+ Dosage (#medicament =>Medicament ; #traitement => Traitement, quantite : Reel)
Avec(medicament NOT NULL, Traitement NOT NULL)  
+ Categorie_Espece (#id_categorie : int ; nom_categorie: string)
+ Medicament_Categorie_espece (#medicament=>Medicament ; #categorie => Categorie_Espece) 
+ Dossier_Medical ( #animal => Animal ; taille : int ; poids : int ; resultat : string ; observation : string ; date : Date ; heure : Time ; procédure => Procédure) 
avec (procedure NOT NULL)
+ Procedure (#id_procedure : int ; nom : string ; description : Text) 
+ Dossier_Traitement(#dossier=>Dossier_Medical ; #traitement => Traitement) Veterinaire_Traitement(#traitement =>Traitement ; #veterinaire => Veterinaire.Personnel)
 
 


