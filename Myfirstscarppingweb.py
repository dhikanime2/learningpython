from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20card'

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
containers = page_soup.findAll("div",{"class": "item-info"})

# name the output file to write to local disk
filename = "products.csv"
f = open(filename, "w")
headers = "brand; product_name; shipping \n"
f.write(headers)


# loops over each product and grabs attributes about
# each product

for container in containers:


    brand = container.findAll("div", {"class": "item-branding"})
    brand_name = brand[0].img["title"].title()



    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand : " + brand_name + '\n')
    print("product_name: " + product_name + '\n')
    print("shipping : " + shipping + '\n')


    f.write(brand_name + "; " + product_name.replace(",", "|") + "; " + shipping + "\n")
f.close()