from .parser import Parser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By


class MvideoParser(Parser):

    #Overriding abstract method
    def find_price(self, product_name: str) -> int:
        content = self.get_page_content(product_name=product_name)
        soup = BeautifulSoup(content, features="lxml")   
        
        return soup.findAll('div', attrs={'class':"_3NaXx _33ZFz _2m5MZ"})


    def get_page_content(self, product_name:str) -> str:
        ua = UserAgent()
        options = Options()
        agent = ua.random
        options.add_argument("window-size=1400,600")
        options.add_argument(f'user-agent={agent}')

        url = "https://market.yandex.ru/"
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
        driver.get(url)
        sleep(20)
        search_element = driver.find_element(By.XPATH, '//*[@id="header-search"]')
        search_element.click()
        sleep(2)
        search_element.clear()
        sleep(2)
        search_element.send_keys(product_name)
        sleep(2)
        search_element.send_keys(Keys.ENTER)
        content = driver.page_source

        return content