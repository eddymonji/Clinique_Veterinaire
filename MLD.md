## MLD (Projet Veto)
+ Client ( #id_client : Int ; nom : String ; prenom : String ; date_naissance : date ; adresse : String ; telephone : Integer)
+ Personnel ( #id_personnel : Int ; nom : String ; prenom : String ; date_naissance : date ; adresse : String ; telephone : Integer, poste : Boolean; categorie_espece => Categorie_Espece : int)  
avec categorie_espece NOT NULL et poste NOT NULL
avec poste=True pour vetérinaire et False pour assistant 
+ Animal (#id_animal : int ; nom : string ; date_naissance : Date ; num_puce : int ; num_passeport : int; categorie_espece => Categorie_Espece) 
avec categorie_espece NOT NULL num_puce UNIQUE,num_passeport UNIQUE
+ Historique_veto(#personnel => Personnel ; #animal =>Animal ; date_debut : Date) 
avec Personnel.poste=TRUE
+ Proprietaire(#animal => Animal ; #client =>Client.Personne, debut: Date, fin: Date )
avec fin >= debut
+ Medicament (#nom : string ; description : text)
+ Traitement (#id_traitement :int ; nom : String ; début : Date ; fin : Date )
avec fin >= debut
+ Dosage (#medicament =>Medicament ; #traitement => Traitement, quantite : Reel)
avec quantite > 0

+ Categorie_Espece (#id_categorie : int ; nom_categorie: string)
+ Medicament_Categorie_espece (#medicament=>Medicament ; #categorie => Categorie_Espece) 
+ Dossier_Medical ( #animal => Animal ; taille : int ; poids : int ; resultat : string ; observation : string ; date : Date ; heure : Time ; procédure => Procédure) 
avec (procedure NOT NULL)
+ Procedure (#id_procedure : int ; nom : string ; description : Text) 
+ Dossier_Traitement(#dossier_mediacl => Dossier_Medical ; #traitement => Traitement) 

+ Veterinaire_Traitement(#traitement =>Traitement ; #veterinaire =>Personnel)avec Personnel.poste=TRUE

+ Notes: 
    - Passage par classes filles pour l'héritage entre Personne et Personnel/Client. Cela permet de respecter d'office l'héritage exclusif et comme Client et Personnel n'ont pas d'interactions commune, cela est d'autant plus pertinent
    - Passage par classes mère entre Personnel et Assistant/Veterinaires par l'ajout d'un attribut booléen. Comme un seul paramètre change (le poste), cela facilite l'implémentation en SQL même si des projections seront nécessaires pour certaines tâches uniquement exécutables par des vétérinaires.
 
 


