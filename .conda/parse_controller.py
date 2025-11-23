from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from parsers import *
from parse_search import *
from database_manager import DatabaseManager

def parse(query):
    product_query = query

    product_list = []

    product_list.extend(search_stores(product_query, product_list))

    if not product_list:
        print("No products found for the given queries.")
    else:
        print("Products found.")
        try:
            queries = [query for query in product_query.split(", ") if query.strip()]
            for query in queries:
                DatabaseManager.create_database(product_list, query)
        except:
            print("Error creating database for query: ", product_query)