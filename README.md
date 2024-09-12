# Programmation avancée

## Lancement du projet

Créer un environnement virtuel à la racine du projet

`virtualenv -p python3 venv`

Activer l'environnement créé

`source venv/bin/activate`

Lancer le projet

`./GestionProduits/manage.py runserver`


## Les commandes utiles

Migrations du models.py vers la base de données sqlite

`python3 ./GestionProduits/manage.py makemigrations LesProduits`

`python3 ./GestionProduits/manage.py sqlmigrate LesProduits 0001`

`python3 ./GestionProduits/manage.py migrate`

Lancer le shell Django

`python3 ./GestionProduits/manage.py shell`

Créer un super-utilisateur

`python3 ./GestionProduits/manage.py createsuperuser`