import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = input("Enter the product URL:")
driver = webdriver.Chrome()


driver.get(url)

product_name = "N/A"
product_price = "N/A"
timer = 0

while(product_price[0] != "$" and timer < 10):

    try:
        product_name = driver.find_element(By.CSS_SELECTOR, "[class*='Product'][class*='title']").text
        product_price = driver.find_element(By.CSS_SELECTOR, "[class*='price']").text

    except:
        print("")

    finally:
        time.sleep(1)
        timer += 1

print("Product name: ", product_name)
print("Product price: ", product_price)
print("Parse time: ", timer)



driver.quit()