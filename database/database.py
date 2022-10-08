from sqlalchemy import create_engine
import configuration.config as cfg
from db_models import Base

db_engine = create_engine(cfg.DATABASE_CONNECTION)

Base.meta.create_all(db_engine)