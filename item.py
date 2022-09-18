class Item:
    def __init__(self, 
                name:str=None, 
                price:str=None, 
                link:str=None, 
                image:str=None, 
                source:str=None) -> None:
        self.name = name
        self.price = price
        self.link = link
        self.image = image
        self.source = source
    
    def __repr__(self) -> str:
        return f"Product name: {self.name}\nPrice: {self.price}\nUrl: {self.link}\nSource: {self.source}"