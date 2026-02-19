### Objectifs du projet
- Créer des brutes
- Les filtrer pour ne garder que les talents
- Faire monter les talents niveau 3
- Les filtrer une seconde fois pour ne garder que les exceptions


#### Dépendances:
- Installer le module playwright avec la commande "pip install playwright".
- Installer les dépendances de playwright avec la commande qu'ils indiquent.


#### Se servir du projet
1 - Choisir un nom et un mot de passe et les mettre dans les variables "username" et "password" des deux programmes.

2 - Créer des brutes avec la commande "python3 machine.py <nombre d'instances> <nombre de brutes par instance> <id de départ>". <br />
    Par exemple, la commande "python3 machine.py 3 10 2500" va lancer 3 instances qui crééront chacune 10 brutes, en commençant à l'id 2500.<br />
    30 brutes seront créées d'id 2500 à 2529.<br />
    Les mauvaises brutes ne sont pas enregistrées et les talents sont envoyés dans le fichier camp_talents.json

4 - Entraîner les talents avec la commande "python3 entrainer_talents.py".
    Choisir les bonus à chaque niveau en tapant "a" ou "b"
    Envoyer les mauvaises brutes au cimetière après l'entraînement en tapant sur entrée.
    Envoyer les exceptions au camp d'exception après l'entraînement en tapant n'importe quoi.
