from bs4 import BeautifulSoup
import re
import requests
import csv

# Csv writing setup
filename = "uo_main_page1_images.csv"
csv_file = open(filename, "w", encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'price', 'link', 'image'])

base_url = "https://www.urbanoutfitters.com"
with open('sneakers_page1_images.html', 'r') as r:
    soup = BeautifulSoup(r.read(), "lxml")

    products = soup.findAll('div', class_="c-pwa-product-tile")

    for product in products:
        try:
            name = product.find('p', class_="c-pwa-product-tile__heading").text.strip()
        except:
            name = "N/A"

        try:
            price = product.find('span', class_="c-pwa-product-price__current").text.strip()
        except:
            price = "N/A"

        try:
            link = base_url + product.find('a', class_="c-pwa-product-tile__link c-pwa-link c-pwa-link--client")["href"]
        except:
            link = "N/A"

        try:
            image_s = product.find('picture', class_="c-pwa-product-tile__media").find('source').find('source')["srcset"]
            image = str(image_s)
            image = image.replace("&", "&amp;")
        except:
            image = "N/A"
        # print(image)
        csv_writer.writerow([name, price, link, image])
    
csv_file.close()