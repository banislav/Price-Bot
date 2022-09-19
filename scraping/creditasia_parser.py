import re

from bs4 import BeautifulSoup

from .parser import Parser
from item import Item

class CreditAsiaParser(Parser):

    def __init__(self) -> None:
        self.url = "https://www.creditasia.uz"
        self.searchbar_xpath = '//*[@id="search"]'
        self.source = "Credit Asia"
        self.scroll = False

    def get_product_list(self, product_name: str) -> list:
        content = super().get_page_content(product_name=product_name, url=self.url, searchbar_xpath=self.searchbar_xpath, scroll=self.scroll)
        soup = BeautifulSoup(content, features="lxml")

        raw_list = soup.find_all('div', attrs={'class':'item'})
        item_list = []
        
        for raw in raw_list:
            soup = BeautifulSoup(str(raw), features='lxml')
            img = self.url + soup.find('img')['src']
            url = self.url + soup.find('a', attrs={'class':'product__image__inner d-flex align-items-center justify-content-center'})['href']
            
            price = soup.find('div', attrs={'class':"price"}).get_text()
            price = re.sub('\\s+', ' ', price)
            
            name = soup.find('div', attrs={'class': 'product__title'})
            soup = BeautifulSoup(str(name), features='lxml')
            name = soup.find('a').get_text()

            item_list.append(Item(name=name, price=price, link=url, image=img, source=self.source))

        return item_list