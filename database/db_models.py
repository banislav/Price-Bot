from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String 

Base = declarative_base()

class Requests(Base):
    __tablename__ = "requests"
    
    id = Column(Integer, primary_key=True)
    source = Column(String)
    query = Column(String)
    user_id = Column(Integer)