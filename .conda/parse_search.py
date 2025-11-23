from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from parsers import *

def search_stores(query, list):

    try:
        driver = webdriver.Chrome()
        driver.get("https://www.aldi.us/results?q=" + query)
        parser = AldiParser()
        product_list = parser.get_list(driver, query)
        list.extend(product_list)
        driver.quit()
    except:
        print("Error parsing Aldi! Continuing...")

    try:
        driver = webdriver.Chrome()
        driver.get("https://shop.capcentremarket.com/shop#!/?q=" + query)
        parser = CapCentreMarketParser()
        product_list = parser.get_list(driver, query)
        list.extend(product_list)
        driver.quit()
    except:
        print("Error parsing Capitol Centre Market! Continuing...")
    
    try:
        driver = webdriver.Chrome()
        driver.get("https://shop.freshmadisonmarket.com/shop#!/?q=" + query)
        parser = FreshMadisonMarketParser()
        product_list = parser.get_list(driver, query)
        list.extend(product_list)
        driver.quit()
    except:
        print("Error parsing Madison Fresh Market! Continuing...")
    
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.target.com/s?searchTerm=" + query)
        parser = TargetParser()
        product_list = parser.get_list(driver, query)
        list.extend(product_list)
        driver.quit()
    except:
        print("Error parsing Target! Continuing...")
    
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.traderjoes.com/home/search?q=" + query)
        parser = TraderJoesParser()
        product_list = parser.get_list(driver, query)
        list.extend(product_list)
        driver.quit()
    except:
        print("Error parsing Trader Joe's! Continuing...")

    return list