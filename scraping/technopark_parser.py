import re

from bs4 import BeautifulSoup
from item import Item
from .parser import Parser


class TechnoparkParser(Parser):

    def __init__(self) -> None:
        self.url = "https://www.technopark.ru"
        self.searchbar_xpath = '//*[@id="header-search-input-main"]'
        self.source = 'Technopark'
        self.scroll = True

    #Overriding abstract method
    def get_product_list(self, product_name: str) -> list:
        content = super().get_page_content(product_name=product_name, url=self.url, searchbar_xpath=self.searchbar_xpath, scroll=self.scroll)
        soup = BeautifulSoup(content, features="lxml")

        raw_list = soup.find_all('div', attrs={'class':'product-card-big__container'})
        item_list = []
        
        for raw in raw_list:
            soup = BeautifulSoup(str(raw), features='lxml')
            url = self.url + soup.find('a', attrs={'class':"product-card-link product-card-big__title product-card-link--cover-container"})['href']
            name = soup.find('a', attrs={'class':"product-card-link product-card-big__title product-card-link--cover-container"})['title']
            img = soup.find('img', attrs={'class':'tp-lazy-image'}).get('src')
            
            price = soup.find('div', attrs={'class':"product-prices__price"}).get_text()
            price = re.sub('\\s+', ' ', price)

            item_list.append(Item(name=name, price=price, link=url, image=img, source=self.source))

        return item_list
