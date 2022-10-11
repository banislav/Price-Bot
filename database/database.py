from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configuration.config as cfg
from database.db_models import Base, Request


db_engine = create_engine(cfg.DATABASE_CONNECTION)
Base.metadata.create_all(db_engine)

Session = sessionmaker(bind=db_engine)

def add_record(query:str, user_id:int, source:str) -> None:
    with Session() as session:
        request = Request(query=query, user_id=user_id, source=source)
        session.add(request)
        session.commit()

def get_user_records(user_id:int) -> None:
    with Session() as session:
        requests = session.query(Request).filter_by(user_id=user_id).all()
    
    return requests

def check_if_user_exists(user_id:int) -> bool:
    with Session() as session:
        usr = session.query(Request).filter_by(user_id=user_id).first()

        if usr is None:
            return False
        
        return True