SCRIPT_admin version 1.0 créé le 15/04/2020 par LudoShadow
contact: LudoShadow@gmail.com

Ce script sert à faire un état d'une machine linux distante.


## Installation

Le programme nécessite que python soit installé sur la machine hôte.

## Utilisation du programme

Ce programme donne le résultats des tests dans un fichier "resultat\nom_machine.txt"


Une premiére sera posé pour savoir si le test s'effectuera sur une machine ou sur une liste pré-definie dans le fichier donnees.py (variable Liste_serveurs).
Question:"Voulez-vous tester tous les serveurs ou 1 seul serveur ? (A pour tous les serveurs, U pour un seul serveur) "
	les réponses "a" ou "A" utilise la liste pré-difinies des machines.
	les réponses "u" ou "U" permettent de donner le nom d'une machine même si elle ne fait pas partie de liste prédéfinie. 


Une deuxiéme qusestion sera posé pour savoir si les tests seront inscrits à la suite du fichier de résultat s'il existe ou si le fichier de résultat sera réinitialisé.
Question: "Voulez-vous Créer un nouveau fichier: o/n "
	la réponse "o" ou "O" réinitialise le ou les fichiers contenant les résultats des tests précédents.
	la réponse "n" ou "N" inscrit les résultats des test à la suite du fichier de la machine testé.


La derniére question demande les identifiants d'un compte utilisateur se retrouvant sur toutes les machines distantes pour pouvoir s'y connecter.




## Paramétrage du programme

Une liste des machines peut être définie dans le fichiers données.py avec la variable Liste_serveurs.


La liste des tests effectuées peut être modifiés dans le fichier donnees.py avec la variable test.

Pour ajouter un test il faut un couple avec nom le nom du test et la commande qui sera effectué.
	exemple pour lire le contenu du répertoire /home avec Test Lecture qui s'affichera dans le fichier de résultat
		
		test = [ "lecture" : "ls -la /home"]
 
	Le résultat affiché sera:
		
		==  Test Lecture  ==
		
		suivi du résultat de la commande effectuée sur la machine	 


## Messages d'erreurs possible pour la connexion ssh

[WinError 10060] Une tentative de connexion a échoué car le parti connecté n’a pas répondu convenablement au-delà d’une certaine durée ou une connexion établie a échoué car l’hôte de connexion n’a pas répondu:
	Vérifier si:
		- Le port ssh est peut-être bloqué
		- La machine est hors-ligne


[Errno 11001] getaddrinfo failed:
	Probéme de résolution de nom

