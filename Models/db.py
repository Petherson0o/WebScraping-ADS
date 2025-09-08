from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Util.settings import URI_PATH

DB_URL:str = f"sqlite:///xposts-{URI_PATH}.db"
engine = create_engine(DB_URL, echo=False)

Session = sessionmaker(bind=engine)