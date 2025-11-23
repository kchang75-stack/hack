import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = input("Enter the product URL:")
driver = webdriver.Chrome()


driver.get(url)

product_name = "N/A"
product_price = "N/A"
timer = 0

while((product_name == "N/A" or product_name.strip() == "") and product_price == "N/A" and timer < 10):

    try:
        product_name = driver.find_element(By.CSS_SELECTOR, "h1[class*='title']").text
        product_price = driver.find_element(By.CSS_SELECTOR, "[class*='price']").text

    except:
        product_name = "N/A"
        product_price = "N/A"

    finally:
        time.sleep(1)
        timer += 1

print("Product name: (", product_name, ")")
print("Product price: ", product_price)
print("Parse time: ", timer)



driver.quit()