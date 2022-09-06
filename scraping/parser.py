from abc import ABC, abstractmethod
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

#Abstract class parser
class Parser(ABC):

    @abstractmethod
    def find_price(self, product_name: str) -> list:
        pass
    
    def get_page_content(self, product_name: str, url: str, searchbar_xpath: str) -> str:
        options = Options()
        options.add_argument("window-size=1920,1080")
        # ua = UserAgent()
        # agent = ua.random
        # options.add_argument(f'user-agent={agent}')
        # options.add_argument('--proxy-server=85.26.146.169:80')

        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
        #Simulate real user
        driver.get(url)
        sleep(5)
        search_element = driver.find_element(By.XPATH, searchbar_xpath)
        search_element.click()
        sleep(3)
        search_element.clear()
        sleep(3)
        search_element.send_keys(product_name)
        sleep(3)
        search_element.send_keys(Keys.ENTER)
        sleep(4)
        content = driver.page_source

        return content