

Fonctionnalités attendues 
Implémenter les endpoints permettant de : 
Enregistrer un patient 
Enregistrer un médecin robot 
Consulter les rendez-vous d'un patient 
Rechercher des médecins robots par spécialité et disponibilité 
Prendre un rendez-vous 
Modifier l'horaire d'un rendez-vous 
Annuler un rendez-vous 
Mettre à jour les informations d'un patient 
 
 
Résultat attendu 
Application exécutable localement 
Documentation Swagger fonctionnelle 
Tests manuels réalisables via Swagger UI 
Modèle de données cohérent et normalisé
 


 patient prend nom prenom, date de naissance, email

 Medecin: id, nom, prenom, specilaité (generaliste, chirurgien, opticien)
 rendez vous: on peut avoir plusieurs rendez vous pour un patient chez differents medecins, 
table rdv : avec une foreign key vers le patient et vers le mdecin

ressources rets: /doctors , /patients, /doctors/appointments et /patients/appointements