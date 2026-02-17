Ce projet sert à:
- Créer des brutes
- Les filtrer pour ne garder que les talents
- Faire monter les talents niveau 3
- Les filtrer une seconde fois pour ne garder que les exceptions



1 - Choisir un nom et un mot de passe et les mettre dans les variables "username" et "password" des deux programmes.

2 - Choisir un numéro d'identifiant qui sera incrémenté pour chaque brute, par exemple choississons 69.

3 - Créer des brutes avec la commande "python3 creer_brutes.py 69" 
    Par défaut, 50 brutes seront créées, ici de username69 à username119.
    Le nombre de brutes créé par défaut peut être changé en modifiant la variable "nombre_essaies" du fichier.
    Il est aussi possible de rendre nombre_essaies dynamique en utilisant argv.
    Les mauvaises brutes ne sont pas enregistrées et les talents sont envoyés dans le fichier camp_talents.json

4 - Entraîner les talents avec la commande "python3 entrainer_talents.py"
    Choisir les bonus à chaque niveau en tapant "a" ou "b"
    Envoyer les mauvaises brutes au cimetière après l'entraînement en tapant sur entrée.
    Envoyer les exceptions au camp d'exception après l'entraînement en tapant n'importe quoi.