from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from parsers import *

url = input("Enter URL: ")

driver = webdriver.Chrome()
driver.get(url)

product_name = "N/A"
product_price = "N/A"

parser = CapCentreMarketParser()

product_name = parser.get_name(driver)
product_price = parser.get_price(driver)

print("Product name: ", product_name)
print("Product price: ", product_price)

driver.quit()
