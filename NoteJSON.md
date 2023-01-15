
## Note sur le JSON:

Suite à la réalisation de notre MLD dans un premier temps, nous avons implémenter un MLD faisant intervenir du JSON.

Ayant constaté que la classe **Dossier_Médical** est une classe composite de la classe **Animal**, nous avons opté de la transformer en attribut JSON de la classe **Animal**. Ceci permettant ainsi plus facilement d'attribuer des dossiers médicaux à des animaux.

De plus, les relations d'association entre **Dossier_Medical - Procedure** et **Dossier_Médical - Traitement** sont de ce fait transformées en relation **Animal - Procedure** et **Animal - Traitement**. Ceci permettant de toujours garder les informations entre les procédures et les traitements suivis par un animal.
