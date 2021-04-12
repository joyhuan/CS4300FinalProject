from bs4 import BeautifulSoup
import re
import requests
import csv

# url = "https://www.urbanoutfitters.com/shop/converse-chuck-taylor-all-star-canvas-platform-high-top-sneaker?category=SEARCHRESULTS&color=015&searchparams=q%3Dsneaker&type=REGULAR&quantity=1"

# Csv writing setup
filename = "sneakers.csv"
csv_file = open(filename, "w", encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'price', 'rating', 'num_reviews', 'color', 'description', 'material', 'fit', 'reviews'])

# soup = BeautifulSoup(r.content, "html.parser")
# soup = BeautifulSoup(r.content, "html5lib")

with open('downloaded.html', 'r') as r:
	soup = BeautifulSoup(r.read(), "lxml")

	try:
		name = soup.find('h1', class_="c-pwa-product-meta-heading").text.strip()
	except:
		name = "N/A"

	try:
		price = soup.find('span', class_="c-pwa-product-price__current").text.strip()
	except:
		price = "N/A"

	try:
		rating = soup.find('div', class_="c-pwa-reviews-snippet__rating-count").text.strip()
	except:
		rating = "N/A"

	try:
		num_reviews = soup.find('a', class_="c-pwa-reviews-snippet__reviews-link").text.strip()[0:-8]
	except:
		num_reviews = 0

	try:
		color = soup.find('span', class_="c-pwa-sku-selection__color-value").text.strip()
	except:
		color = "N/A"

	try:
		details = soup.find('div', class_="s-pwa-cms c-pwa-markdown")
		items = details.findAll('p')
		description = items[0].text
		material = items[1].text[14:]
		material = material[:1] + material[1:].replace('-', ' -')
		fit = items[2].text[10:]
	except:
		description = "N/A"
		material = "N/A"
		fit = "N/A"

	try:
		reviews_lst = soup.findAll('p', class_="c-pwa-review-detail__text")
		stripped_reviews_lst = [r.text.strip() for r in reviews_lst]
		reviews = '; '.join(stripped_reviews_lst)
	except:
		reviews = "N/A"
	
	csv_writer.writerow([name, price, rating, num_reviews, color, description, material, fit, reviews])

csv_file.close()
