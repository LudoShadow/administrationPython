#### Initialisation des variables utilisés dans le programme

choix = str()
fichier = 0
affichage = 0


## Liste_serveurs contient la liste de tous les serveurs qui seront testés, si on choisis tous les serveurs
Liste_serveurs = ["srv1", "srv2", "srv3"]


# Dictionnaire contenant la liste de chaque test réalisé sur chaque serveur
test = {"cpu":"top -n1 -b", "ram":"free", "hdd":"df -h", "reseau":"ip a", "ports":"ss -l", "services":"systemctl list-units --type=service "}
