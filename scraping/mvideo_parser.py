from parser import Parser
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

class MvideoParser(Parser):

    #Overriding abstract method
    def find_price(self, product_name: str) -> int:
        url = "https://www.mvideo.ru/product-list-page?q=" + product_name.replace(' ', '+')
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)
        content = driver.page_source
        soup = BeautifulSoup(content)
        
        return soup.findAll('span', attrs={'class':"price__main-value"})

