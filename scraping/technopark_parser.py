from .parser import Parser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By


class TechnoparkParser(Parser):

    #Overriding abstract method
    def find_price(self, product_name: str) -> int:
        content = self.get_page_content(product_name=product_name)
        soup = BeautifulSoup(content, features="lxml")   
        
        price_list = soup.findAll('div', attrs={'class':"product-prices__price"})
        # for i in range(0, len(price_list)):
        #     price_list[i] = soup.find('span', attrs={"class": 'price__main-value'})

        return price_list

    def get_page_content(self, product_name:str) -> str:
        ua = UserAgent()
        options = Options()
        agent = ua.random
        options.add_argument("window-size=3024,1964")
        # options.add_argument(f'user-agent={agent}')
        # options.add_argument('--proxy-server=85.26.146.169:80')

        url = "https://www.technopark.ru"
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
        driver.get(url)
        sleep(10)
        search_element = driver.find_element(By.XPATH, '//*[@id="header-search-input-main"]')
        search_element.click()
        sleep(5)
        search_element.clear()
        sleep(5)
        search_element.send_keys(product_name)
        sleep(5)
        search_element.send_keys(Keys.ENTER)
        sleep(10)
        content = driver.page_source

        return content