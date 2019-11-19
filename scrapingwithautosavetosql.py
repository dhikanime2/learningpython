import MySQLdb
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com

my_url = 'https://www.bukalapak.com/c/hobi-koleksi/mainan?search%5Bkeywords%5D=gundam'

# opens the connection and downloads html page from url
uClient = uReq(my_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_html = uClient.read()

# as if it were a json data type.
uClient.close()

# parses html into a soup data structure to traverse html
page_soup = soup(page_html, "html.parser")

# grab each product
containers = page_soup.findAll("div",{"class": "product-card"})

# Save event data to database
# Open database connection
db = MySQLdb.connect(host='localhost', user='root', passwd='warning13', db='scraping_bukalapak', port=3306)
# prepare a cursor object using cursor() method
cursor = db.cursor()
#delete table if exist
cursor.execute("DROP TABLE IF EXISTS myscraping")
# Create tables myscraping
cursor.execute("""CREATE TABLE myscraping ( id INT NOT NULL AUTO_INCREMENT,
                                                                         stuff_name VARCHAR(300) NOT NULL,
                                                                         badges VARCHAR(300) NOT NULL, 
                                                                         harga_barang VARCHAR(300) NOT NULL,
                                                                         diskon VARCHAR(300) NOT NULL,
                                                                         harga_diskon VARCHAR(300) NOT NULL,
                                                                         kondisi VARCHAR(300) NOT NULL,
                                                                         rating VARCHAR(300) NOT NULL,
                                                                         ulasan VARCHAR(300) NOT NULL,
                                                                         PRIMARY KEY (`id`));""")



for container in containers:

    #Stuff name
    brand = container.findAll("div", {"class":"product-media"})
    brandName = brand[0].a["title"].title()

    #Original price
    harga = container.find("div", {"class":"product-price"})
    hargaChilds = harga.findChildren()
    hargaAwal = hargaChilds[2].text
    hargaAwal = int((hargaAwal.replace(".", "")))



    #Discount
    persen = container.find("div", {"class": "product-discount-badge product-discount-badge--active"})
    if persen is not None:
        persenChilds = persen.findChildren()
        persenAngka  = persenChilds[0].text
        persenAngka = int((persenAngka.replace(".", "")))



    else :
        persenAngka = "0"
        persenAngka = int("0")

    # Final Price

    baru = container.find("span", {"class": "product-price__reduced"})
    if baru is not None:
        diskonChilds = baru.findChildren()
        hargaDiskon = diskonChilds[1].text
        hargaDiskon = int((hargaDiskon.replace(".", "")))


    else:
        hargaDiskon = "Tidak Ada Diskon"



    #Rating dan Ulasan
    bintang = container.find("div", {"class": "product__rating"})
    bintangChilds = bintang.findChildren()
    if len(bintangChilds) > 0:
        rating = bintangChilds[0]["title"].title()
        ulasan = bintangChilds[2].span.text
    else:
        rating = "0.0"
        ulasan = "Tidak ada ulasan"


    #Badges
    badges = container.find("div", {"class": "u-position-absolute u-position-bottom u-position-left u-position-absolute--bottom u-position-absolute--left u-mrgn-left--1 u-mrgn-bottom--1"})
    if badges is not None:
        badgesChilds = badges.findChildren()
        lencana = badgesChilds[0].text


    else:
        lencana = ('Tidak ada Lencana')



    # Stuff Conditions

    kondisi = container.findAll("div", {"class": "product-meta"})
    kondisi2 = kondisi[0].text.strip()

    print("Brand : " + brandName + '\n')
    print("Badges : " + lencana + '\n')
    print("Harga barang: " + "Rp " + str(hargaAwal) + '\n')
    print("Diskon :" + str(persenAngka) + '%' + '\n')
    print("Harga Diskon: " + str(hargaDiskon) + '\n')
    print("Kondisi : " + kondisi2 + '\n')
    print("Rating : " + rating + '\n')
    print("Ulasan: " + ulasan + '\n')


#

    # Save event data to database
    # Open database connection
    db = MySQLdb.connect(host='localhost', user='root', passwd='warning13', db='scraping_bukalapak', port=3306)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO myscraping(stuff_name, badges, harga_barang, diskon, harga_diskon, kondisi, rating, ulasan ) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(brandName, lencana, hargaAwal, persenAngka, hargaDiskon, kondisi2, rating, ulasan, 'NOW()')
    try:
 # Execute the SQL command
        cursor.execute(sql)
 # Commit your changes in the database
        db.commit()
    except:
 # Rollback in case there is any error
        db.rollback()
 # disconnect from server
    db.close()