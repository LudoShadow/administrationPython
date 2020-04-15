"""Ce fichier définit des fonctions utiles pour le programme SCRIPT.py

On utilise les données du programme contenues dans Donnees.py"""

import os
import paramiko
from donnees import *
import logging
from datetime import datetime
import time

# Création du réperoire pour les resultats des tests s'il n'existe pas
def repertoire():
    try: 
        os.makedirs("resultat")
    except OSError:
        if not os.path.isdir("resultat"):
            Raise 

# Création des fichiers qui contiendront les résultats si besoin avec srv comme variable qui correspond au nom du serveur
def fichier_resultat(srv):   
    try:
        with open(str("resultat/" + srv)): pass
    except IOError:
        with open(str("resultat/" + srv + ".txt"), "w"):
            print ("Le fichier " + srv  + ".txt a été créé")
  
# Test de la Connexion en SSH
def connexion_ssh(srv, login, passwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    client.load_system_host_keys()
    # Tentative de connexion en ssh avec srv comme non du serveur, login comme compte de connexion et passwd le mot de passe de connexion
    try: 
        client.connect(srv, username = login, password = passwd )
        fic_result = open("resultat/tmp.txt", "a")
        fic_result.write("OK")
        fic_result.close()
        fic_result = open("resultat/" + srv + ".txt", "a")
        fic_result.write (" Le test de connexion ssh a réussi ")
        fic_result.write(("\n" +  " " + "\n"))
        fic_result.close()
        print("La connexion ssh sur le poste ", srv, " a réussi, les tests sont en cours.")

                    
    # Message en cas d'erreur de connexion SSH            
    except Exception as e:
        fic_result = open("resultat/" + srv + ".txt", "a")
        fic_result.write("\n" + " Le test de connexion ssh a échoué avec l'erreur : ")
        fic_result.write(str(e))
        fic_result.write("\n" + " ")
        print("La connexion ssh a échoué :", e)
        fic_result.close()
        result= "KO"
        fic_result = open("resultat/tmp.txt", "a")
        fic_result.write( "KO")
        fic_result.close()

# Lancement du test sur la machine distante avec la variable test_test comme ligne de commande, srv comme non du serveur, login comme compte de connexion et passwd le mot de passe de connexion
def test_realise(srv, login, passwd, test_test):
    fic_result = open("resultat/" + srv + ".txt", "a")   
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    client.load_system_host_keys()
    client.connect(srv, username = login, password = passwd ) 
    stdin, stdout, stderr = client.exec_command(test_test)
    for line in stdout.read().splitlines():
        fic_result.write((str(line) + "\n")[2:])
    fic_result.write(("\n" +  " " + "\n"))
    fic_result.close
  
    
# Paramétrage de la boucle qui sert à la mise en page du contenu du fichier de tests des serveurs 
def mise_en_page(i, name_test, srv):
    a = i
    while a > 0:
        a = a - 1
        fic_result = open("resultat/" + srv + ".txt", "a")
        fic_result.write(("="))
    fic_result.write(name_test)
    while i > 0:
        i = i - 1
        fic_result = open("resultat/" + srv + ".txt", "a")
        fic_result.write(("=")) 
    fic_result.write(("\n" +  " " + "\n"))
    fic_result.close()

## Dans le fichier de résultat indique le nom de la machine avec la date et l'heure des tests
def debut_test(srv):
    date_test = time.strftime('%Y-%m-%d %H:%M:%S')
    a = 3
    fic_result = open("resultat/" + srv + ".txt", "a")
    while a > 0:
        a -= 1
        mise_en_page(59, ("=" ), srv)
    print(srv)
    mise_en_page(35, ("  Début du test sur " + srv + " le " + date_test + "  "), srv)
    fic_result.write(("\n" +  " " + "\n"))
    fic_result.close()
