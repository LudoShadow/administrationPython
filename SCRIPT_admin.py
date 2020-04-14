# -*- coding : utf8 -*-

import os
import getpass
from Donnees import *
from Fonctions import *


# Demander si liste serveur ou 1 seul serveur?

while choix not in ("A",  "a", "u", "U"):
    choix = input("Voulez-vous tester tous les serveurs ou 1 seul serveur ? (A pour tous les serveurs, U pour un seul serveur) ")
    print(choix)

    if (choix == "a") or (choix == "A"):
        #print("les serveurs seront chargés depuis le fichier 'liste liste_srv.txt' ")
        # charger la liste des serveurs
        #fichier = open("liste_srv.txt", "r")
        #serveur = fichier.read()
        #serveur = serveur.split(' ')
        serveur = Liste_serveurs
        # print(type(serveur))
    elif (choix == "U") or (choix == "u"):
        
        serveur = input("Quel serveur voulez-vous tester ? ")
        print("Le serveur tester sera: ", serveur)
        serveur =  serveur.split()
        # print(type(serveur))
    else:
        choix = input( "Merci de choisir A pour charger la liste des serveurs ou U pour lancer le test sur un seul serveur! ")
      
# Demander si nouveau fichier ou à la suite

while fichier not in ( "o", "O", "n", "N"):
    fichier =input("Voulez-vous Créer un nouveau fichier: o/n ")
    if (fichier == "o") or (fichier == "O"):
    # Créer un nouveau fichier ou plusieurs
        for i in serveur:
            repertoire()
            i = i.lower()
            fichier_resultat(i)
           # print("Création nouveau fichier")
    elif (fichier == "N") or (fichier == "n"):
        repertoire()
        print ("Pas de nouveau fichier créé")
    else:
        print ("Merci de choisir o/O pour créer un nouveau fichier ou n/N pour ne pas créer un nouveau fichier ")

# Demander les identifiants de connexion

login = input("Quel compte voulez-vous utiliser? ")
passwd = getpass.getpass("Entrez le mot de passe associé: ")

### Lancer les tests pour chaque serveur

for srv in serveur:
    debut_test(srv)
    ## Tester la connexion ssh
    connexion_ssh(srv, login, passwd)
    result_ssh = (open("resultat/tmp.txt", "r")).read()
    os.remove("resultat/tmp.txt")

    ## Si la connexion ssh est bonne faire les tests, sinon passer à la machine suivante
    if result_ssh == "OK":
        name_srv = srv
        for cle, valeur in test.items():
            decalage = (affichage + 1) * 2
            affichage += 2
            nom_test = str("  Test " + cle.capitalize() + "  ")
            mise_en_page(decalage, nom_test, name_srv)
            test_realise(name_srv, login, passwd, valeur)
    else:
        pass


print()
print("       ========================================== ")
print( " ")
print("Le choix du ou des serveur(s) était : ")
print(serveur)
print("       ========================================== ")

os.system("pause")
