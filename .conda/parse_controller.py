from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from parsers.trader_joes_parser import TraderJoesParser
from parsers.target_parser import TargetParser
from parsers.aldi_parser import AldiParser
from parsers.fresh_madison_market_parser import FreshMadisonMarketParser
from parsers.capital_centre_market_parser import CapCentreMarketParser

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
