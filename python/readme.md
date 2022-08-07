![img](https://jobboard.webmonster.tech/assets/images/webmonster/logo-dark@2x.png)
# PYTHON - SITEMAP
## Script par Webmonster Community

| NOM           | VALEUR                |
| ------------- | --------------------- |
| APPLICATION   | GENERATEUR DE SITEMAP |
| LANGAGE       | PYTHON                |
| VERSION       | 1.0.0                 |
| DATE          | 2022-08-06            |
| AUTHOR        | Webmonster Antilles   |

**NECESSAIRE** : PYTHON 3+ - MYSQL/MARIADB - LINUX

Ce **générateur de sitemap** est très simple, si il est placé à la racine de votre site, en s'executant il va générer un fichier sitemap.xml très apprécié des moteurs de recherche et indispensable à un référencement de qualité.

Le but de ce script est de compléter un sitemap existant avec les URLs des pages dynamiques extraites d'une base de données.

## Configuration

```python
# CONFIGURATION
URL = 'https://127.0.0.1'
HST = 'localhost'
USR = 'root'
PWD = '123456'
DBN = 'db'
FIND_AVAILABLE_PRODUCTS_QUERY = "SELECT title FROM produits ORDER BY title"
FILENAME = 'sitemap.xml'
```

``URL`` : Remplacer par l'adresse de votre site

``USR`` : Remplacer par le nom de l'utilisateur MySQL/MariaDB

``PWD`` : Remplacer par le mot de passe de l'utilisateur MySQL/MariaDB

``DBN`` : Remplacer par le nom de votre base de données

``FIND_AVAILABLE_PRODUCTS_QUERY`` : Requête pour récupérer les données

``FILENAME`` : Nom du fichier sitemap



Si vous avez des questions sur l'utilisation de ce script n'hésitez pas à laisser un commentaire.

![img](https://jobboard.webmonster.tech/assets/images/webmonster/logo-dark.png)

Visiter la communauté [Webmonster](https://discord.gg/XU4g5WfH4R) sur Discord.
