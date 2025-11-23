from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from .parser_base import ParserBase

class TraderJoesParser(ParserBase):

    @classmethod
    def get_name(self, driver):
        try:
            name = WebDriverWait(driver, 10).until(
            lambda d: (elem := d.find_element(
                By.CSS_SELECTOR, "[class*='ProductDetails_main__title__14Cnm']")
            ).text.strip() or None
            )
        except TimeoutException:
            name = "N/A"
        return name


    @classmethod
    def get_price(self, driver):
        try:
            price = WebDriverWait(driver, 10).until(
            lambda d: (elem := d.find_element(
                By.CSS_SELECTOR, "[class*='price']").text.strip() or None
            )
            )
        except TimeoutException:
            price = "N/A"
        return price


        