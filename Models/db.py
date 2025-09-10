import os
import platform
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Util.settings import URI_PATH

# Armazena o caminho absoluto da pasta Models (onde este arquivo está)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, f"xposts-{URI_PATH}.db")

# Checa se o SO é Windows e, se for, faz a substituição do // por \
if os.name == "nt" or platform.system() == "Windows":
    DB_PATH = DB_PATH.replace("\\", "/")

DB_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(str(DB_URL), echo=False, future=True)

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
