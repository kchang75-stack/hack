from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from parsers import *
from parse_search import *

product_query = input("Enter product search query: ")

products = [item.strip() for item in product_query.split(",") if item.strip()]

product_list = []
for product in products:
    product_list.extend(search_stores(product, product_list))

if not product_list:
    print("No products found for the given queries.")
else:
    print("Products found.")