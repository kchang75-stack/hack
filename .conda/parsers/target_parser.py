from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from .parser_base import ParserBase

class TargetParser(ParserBase):

    def get_list(self, driver, query):

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^='styles_ndsTruncate']")))
        names = driver.find_elements(By.CSS_SELECTOR, "div[class^='styles_ndsTruncate']")
        prices = driver.find_elements(By.CSS_SELECTOR, "span[class*='sc-67b4d80d-3']")
        
        product_list = [{"itemName": name.text, "itemPrice": price.text[1:], "storeName": "target", "query": query} for name, price in zip(names, prices)]

        filtered_list = []

        for product in product_list:
            item_name_lower = product["itemName"].lower()
            if (
                query in item_name_lower
                and not any(item["itemName"].lower() == item_name_lower for item in filtered_list)
            ):
                filtered_list.append(product)

        return filtered_list