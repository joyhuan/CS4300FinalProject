from bs4 import BeautifulSoup
import re
import requests
import csv
from time import gmtime, strftime

# Csv writing setup
csv_file = open("uo_main.csv", "w", encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'price', 'link', 'image'])

base_url = "https://www.urbanoutfitters.com"
url = "https://www.urbanoutfitters.com/search?q=sneakers"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "lxml")

products = soup.findAll('div', class_="c-pwa-product-tile")
# products_link_file = open("products_link", "w", encoding='utf-8')

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
		image = product.find('picture', class_="c-pwa-product-tile__image")
	except:
		image = "N/A"
	# print(image)

	csv_writer.writerow([name, price, link, image])

csv_file.close()
