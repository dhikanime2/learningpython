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



filename = "gundam.csv"
f = open(filename, "w")
headers = "Stuff name; Badges; Harga barang; Diskon (%) ; Harga Diskon; Kondisi; Rating; Ulasan  \n"
f.write(headers)


for container in containers:

    #Stuff name
    brand = container.findAll("div", {"class":"product-media"})
    brandName = brand[0].a["title"].title()

    #Original price
    harga = container.find("div", {"class":"product-price"})
    hargaChilds = harga.findChildren()
    hargaAwal = hargaChilds[2].text


    #Discount
    persen = container.find("div", {"class": "product-discount-badge product-discount-badge--active"})
    if persen is not None:
        persenChilds = persen.findChildren()
        persenAngka  = persenChilds[0].text

    else :
        persenAngka = "0"

    # Final Price

    baru = container.find("span", {"class": "product-price__reduced"})
    if baru is not None:
        diskonChilds = baru.findChildren()
        hargaDiskon = diskonChilds[1].text

    else:
        hargaDiskon = "0"


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
    print("Harga barang: " + "Rp "  + hargaAwal + '\n')
    print("Diskon :" + persenAngka + '%' + '\n')
    print("Harga Diskon: "+ hargaDiskon + '\n')
    print("Kondisi : " + kondisi2 + '\n')
    print("Rating : " + rating + '\n')
    print("Ulasan: " + ulasan + '\n')


    f.write(brandName + "; " + lencana + "; "  + hargaAwal + "; " + persenAngka  +" ; " + hargaDiskon + "; " + kondisi2 + "; " + rating + "; " + ulasan +  "\n")
f.close()