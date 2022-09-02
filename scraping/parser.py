from abc import ABC, abstractmethod

#Abstract class parser
class Parser(ABC):

    @abstractmethod
    def find_price(self, product_name: str):
        pass