from .parser import Parser
from bs4 import BeautifulSoup


class TechnoparkParser(Parser):

    def __init__(self) -> None:
        self.url = "https://www.technopark.ru"
        self.searchbar_xpath = '//*[@id="header-search-input-main"]'

    #Overriding abstract method
    def find_price(self, product_name: str) -> int:
        content = super().get_page_content(product_name=product_name, url=self.url, searchbar_xpath=self.searchbar_xpath)
        soup = BeautifulSoup(content, features="lxml")   
        
        items_list = soup.findAll('div', attrs={'class':"product-prices__price"})

        return items_list
