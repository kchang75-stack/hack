from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from .parser_base import ParserBase

class TargetParser(ParserBase):
    @classmethod
    def get_name(driver):
        return driver.find_element(By.CSS_SELECTOR, "[class*='title']").text

    @classmethod
    def get_price(driver):
        return driver.find_element(By.CSS_SELECTOR, "[class*='price']").text