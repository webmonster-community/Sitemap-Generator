# PHP - SITEMAP
## Script par Webmonster Community

| NOM           | VALEUR                |
| ------------- | --------------------- |
| APPLICATION   | GENERATEUR DE SITEMAP |
| LANGAGE       | PHP                   |
| VERSION       | 1.0.0                 |
| DATE          | 2022-08-06            |
| AUTHOR        | Webmonster Antilles   |

**NECESSAIRE** : PHP5+ - MYSQL/MARIADB - LINUX

Ce **générateur de sitemap** est très simple, si il est placé à la racine de votre site, en s'executant il va générer un fichier sitemap.xml très apprécié des moteurs de recherche et indispensable à un référencement de qualité.

Le but de ce script est de compléter un sitemap existant avec les URLs des pages dynamiques extraites d'une base de données.

## Configuration

```php
/** CONFIGURATION */
$url = 'https://mydomain.com';
$dsn = "mysql:host=localhost;dbname=";
$usr = "user12";
$pwd = "12user";
$dbn = "db";
```
``$url`` : Remplacer par l'adresse de votre site
``$usr`` : Remplacer par le nom de l'utilisateur MySQL/MariaDB
``$pwd`` : Remplacer par le mot de passe de l'utilisateur MySQL/MariaDB
``$dbn`` : Remplacer par le nom de votre base de données

Une fois la configuration terminé, le script se connecte à votre base de données pour récupérer dans notre exemple un champ ``Titre`` pour le convertir avec la fonction Slugify en chaine de caractères adaptés à une URL et performante pour votre référencement.



Vous pouvez aussi dupliquer cette partie du code pour récupérer les données d'une autre table.

La fin du script


Visiter la communauté [Webmonster](https://discord.gg/XU4g5WfH4R) sur Discord.
