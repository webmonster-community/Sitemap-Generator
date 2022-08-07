import urllib.parse
import urllib.request
import mysql.connector
from mysql.connector import Error
from slugify import slugify


# CONFIGURATION
URL = 'https://127.0.0.1'
HST = 'localhost'
USR = 'root'
PWD = '123456'
DBN = 'db'
FIND_AVAILABLE_PRODUCTS_QUERY = "SELECT title FROM produits ORDER BY title"
FILENAME = 'sitemap.xml'

# DO NOT TOUCH

def write_sitemap_urls(file, product):
    title = product['title']

    file.write(
        "\n\t\t<url>\n\t\t\t<loc>{location}</loc>\n\t\t\t<changefreq>daily</changefreq><priority>0.8</priority>\n\t\t</url>".format(location=URL + '/' + slugify(title) + '/')
    )


with open(FILENAME, "w") as file:

    print("Fichier %s ouvert." % FILENAME)
    file.write(
      "<?xml version='1.0' encoding='UTF-8'?>\r\t<urlset xmlns='https://www.sitemaps.org/schemas/sitemap/0.9' xmlns:image='http://www.google.com/schemas/sitemap-image/1.1'>"
    )

    try:
        cnx = mysql.connector.connect(
            host=HST,
            database=DBN,
            user=USR,
            password=PWD
        )
        print("Connexion à la base réussie.")

        cursor = cnx.cursor(dictionary=True)

        print("Veuillez patienter...")

        cursor.execute(FIND_AVAILABLE_PRODUCTS_QUERY)
        available_products = cursor.fetchall()

        for product in available_products:
          write_sitemap_urls(file, product)

    except Error as e:
        print("Erreur", e)
    finally:
        if cnx.is_connected():
            cursor.close()
            cnx.close()
            print("Connexion à la base terminée.")

            file.write('\n\t</urlset>')

print('Le sitemap est prêt !')

URLENCODE = 'https://www.google.com/ping?sitemap=' + urllib.parse.quote_plus(URL + '/sitemap.xml')
response = urllib.request.urlopen(URLENCODE)
print('Ping à Google !')
