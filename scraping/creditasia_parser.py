from .parser import Parser
from bs4 import BeautifulSoup

class CreditAsiaParser(Parser):

    def __init__(self) -> None:
        self.url = "https://www.creditasia.uz/"
        self.searchbar_xpath = '//*[@id="search"]'

    def find_price(self, product_name: str):
        content = super().get_page_content(product_name=product_name, url=self.url, searchbar_xpath=self.searchbar_xpath)
        soup = BeautifulSoup(content, features="lxml")

        items_list = soup.find_all('div', attrs={'class':'item'})
        return items_list