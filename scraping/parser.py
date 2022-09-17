from time import sleep
from abc import ABC, abstractmethod

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By


class Parser(ABC):
    '''
    Abstract class parser
    '''

    @abstractmethod
    def get_product_list(self, product_name: str) -> list:
        pass
    
    def get_page_content(self, product_name: str, url: str, searchbar_xpath: str) -> str:
        options = Options()
        options.add_argument("window-size=1920,1080")

        with webdriver.Chrome(ChromeDriverManager().install(), options=options) as driver:
            #Simulate real user
            driver.get(url)
            sleep(2)
            search_element = driver.find_element(By.XPATH, searchbar_xpath)
            search_element.click()
            search_element.clear()
            search_element.send_keys(product_name)
            search_element.send_keys(Keys.ENTER)
            sleep(2)
            content = driver.page_source

        return content