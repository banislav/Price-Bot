from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String 

Base = declarative_base()

class Request(Base):
    __tablename__ = "requests"
    
    id = Column(Integer, primary_key=True)
    source = Column(String)
    query = Column(String)
    user_id = Column(Integer)

    def __init__(self, query:str, user_id:int, source:int) -> None:
        self.source = source
        self.query = query
        self.user_id = user_id
    
    def __str__(self) -> str:
        return f'{self.id}. Searched for {self.query} from {self.source}'