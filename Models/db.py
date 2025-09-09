# Models/db.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Util.settings import URI_PATH

# pega o caminho absoluto da pasta Models (onde este arquivo está)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, f"xposts-{URI_PATH}.db")
DB_PATH = DB_PATH.replace("\\", "/") # Apenas se o SO for Windows

DB_URL = f"sqlite:///{DB_PATH}"

# print("Conectando em:", DB_URL)  # debug
engine = create_engine(str(DB_URL), echo=False, future=True)

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
