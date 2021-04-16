from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import requests
import csv
import time
from link import *

url_list = url_list_page3
# Csv writing setup

csv_file = open("sneakers_description.csv", "w", encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'price', 'rating', 'num_reviews', 'color', 'description', 'material', 'fit', 'reviews', 'brand'])

br = webdriver.Firefox(executable_path="/Users/mac/Downloads/geckodriver")
for url in url_list:
    br.get(url)
    time.sleep(2)

    br.execute_script("window.scroll(0, 1400);")
    time.sleep(5)

    html = br.page_source
    soup = BeautifulSoup(html, "lxml")

    try:
        brand = soup.find('a', class_="c-pwa-product-partner-url__link c-pwa-link c-pwa-link--client").text.strip()
        brand = brand[8:]
    except:
        brand = "N/A"

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
        details = soup.find_all('div', class_="s-pwa-cms c-pwa-markdown")[0]
        items = details.findAll('p')
        description = items[0].text
    except:
        try:
            details = soup.find_all('div', class_="s-pwa-cms c-pwa-markdown")[1]
            items = details.findAll('p')
            description = items[0].text
        except:
            description = "N/A"
    


    try:
        details = soup.find('div', class_="s-pwa-cms c-pwa-markdown")
        items = details.findAll('p')
        material = items[1].text[14:]
        material = material[:1] + material[1:].replace('-', ' -')
    except:
        material = "N/A"
    
    try:
        details = soup.find('div', class_="s-pwa-cms c-pwa-markdown")
        items = details.findAll('p')
        fit = items[2].text[10:]
    except:
        fit = "N/A"


    try:
        num_pages = soup.find('span', class_="o-pwa-pagination__page-total").text
        int_num = int(num_pages)
    except:
        int_num = 0
    
    print(int_num)
    all_reviews = ""
    # try:
    #     if int_num > 0:
    #         num_pages = soup.find('span', class_="o-pwa-pagination__page-total").text
    #         reviews_lst = soup.findAll('p', class_="c-pwa-review-detail__text")
    #         stripped_reviews_lst = [r.text.strip() for r in reviews_lst]
    #         reviews = '; '.join(stripped_reviews_lst)
    #         all_reviews += reviews

    #         for i in range(2, min(int_num+1, 6)):
    #             url_new = url + "&reviewPage=" + str(i)
    #             br_new = webdriver.Firefox()
    #             br_new.get(url_new)
    #             time.sleep(2)

    #             br_new.execute_script("window.scroll(0, 1500);")
    #             time.sleep(5)

    #             html_new = br_new.page_source
    #             soup_new = BeautifulSoup(html_new, "lxml")

    #             reviews_lst = soup_new.findAll('p', class_="c-pwa-review-detail__text")
    #             stripped_reviews_lst = [r.text.strip() for r in reviews_lst]
    #             new_reviews = '; '.join(stripped_reviews_lst)
    #             all_reviews += new_reviews				
    # except:
    all_reviews += ""
    
    csv_writer.writerow([name, price, rating, num_reviews, color, description, material, fit, all_reviews, brand])

csv_file.close()
