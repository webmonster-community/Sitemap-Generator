![img](https://jobboard.webmonster.tech/assets/images/webmonster/logo-dark@2x.png)
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

## Connexion à la base de données

```php
$pdo = new PDO($dsn.$dbn, $usr, $pwd);
```
Une fois la configuration terminé, le script se connecte à votre base de données pour récupérer dans notre exemple un champ ``Titre`` pour le convertir avec la fonction Slugify en chaine de caractères adaptés à une URL et performante pour votre référencement.

```php
$stm = $pdo->query("SELECT title FROM articles ORDER BY title;");
```
Cette étape est importante puisqu'il faut adapter la requête à vos besoins.

Prenons un exemple simple avec un blog :

Vous récupérez le champ ``titre`` de vos articles parce qu'ils forment l'URL pour afficher vos articles sur le blog exemple

``https://monsite.fr/blog/mon-slug-url-unique/``

Votre variable ``$url`` dans la configuration sera donc :

```php
$url = 'https://monsite.fr/blog
```
Sans le / à la fin de l'adresse URL.

Une fois que la requete s'execute, les résultats sont stockés dans un tableau qui est ensuite parcouru ligne par ligne pour ajouter chaque url dans le fichier sitemap.

```php
foreach ($results AS $result):
    $sitemap .= "<url>\r\t<loc>".$url.'/'.slugify($result->title)."/</loc>\r\t<priority>0.5</priority>\r\t<changefreq>daily</changefreq>\r</url>\n\r";
endforeach;
```
Le script utilise une fonction Slugify qui permet de convertir une chaine de caractère en lien URL.

`````
## Astuce
Vous pouvez aussi dupliquer cette partie du code pour récupérer les données d'une autre table.
`````

## Ecriture du fichier sitemap.xml

```php
$sitemap_xml = './sitemap.xml';
$file = fopen($sitemap_xml, 'w+');
fputs($file, $sitemap);
```
La variable ``$sitemap_xml`` correspond au nom du fichier de destination.

http://www.google.com/ping?sitemap=https://techmonster.info/sitemap.xml

Si vous avez des questions sur l'utilisation de ce script n'hésitez pas à laisser un commentaire.

![img](https://jobboard.webmonster.tech/assets/images/webmonster/logo-dark@2x.png)

Visiter la communauté [Webmonster](https://discord.gg/XU4g5WfH4R) sur Discord.
