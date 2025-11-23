from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from .parser_base import ParserBase

class FreshMadisonMarketParser(ParserBase):

    @classmethod
    def get_name(self, driver):
        try:
            name = WebDriverWait(driver, 10).until(
            lambda d: (elem := d.find_element(
                By.CSS_SELECTOR, "h1.fp-page-header.fp-page-title")
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
                By.CSS_SELECTOR, "span.fp-item-base-price").text.strip() or None
            )
            )
        except TimeoutException:
            price = "N/A"
        return price