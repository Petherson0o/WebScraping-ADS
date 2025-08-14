from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URL:str = "sqlite:///xposts.db"
engine = create_engine(DB_URL, echo=False)

Session = sessionmaker(bind=engine)