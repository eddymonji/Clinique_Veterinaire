+ ## Personne(nom, prenom, dateNaiss, adresse, telephone, période)
    + client -> possède des **<ins>animaux</ins>** (* - *)
    + personnel (poste) 
        + specialisé sur une **<ins>catégorie-espèce</ins>** (*-1)
        + suit **<ins>animal</ins>** (1-*)
        + de type **<ins>Vétérinaire</ins>** <br> 
        + ou de type **<ins>Assistant</ins>**
<br> 

+ ## Animal(nom, dateNaiss, numPuce, numPassport)
    + possédé par un **<ins>client</ins>**(1..*  -  1..*) 
    + a un **<ins>Vétérinaire</ins>** (* -  1)
    + a un **<ins>dossierMedical</ins>** (1 - 1)
    + est d'une **<ins>catégorie-espèce</ins>** (* -1)
<br> 

+ ## Catégorie-espèce(nom, autre_espèce)
<br> 

+ ## dossierMedical(taille, poids, resultat, observation, date, heure)
    + comporte **<ins>procedure</ins>** (1-1)
    + comporte **<ins>traitement</ins>** (1-1..*)
<br> 

+ ## Procedure(nom, description)
<br> 

+ ## Medicament(nom, description)
    + autorisé pour **<ins>catégorie-espèce</ins>** (0..*  -  0..*)
<br>

+ ## Traitement(debut, duree, nom, quantité)
    + possède **<ins>Medicament</ins>** (1..* - 1..*)
    + est prescrit par **<ins>Vétérinaire</ins>** (1..* - 1..*)
<br> 





