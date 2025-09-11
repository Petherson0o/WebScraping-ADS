"""
Arquivo de configurações globais e parâmetros de funções
"""
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# url das páginas do twitter
ROOT_PATH: str = "https://x.com/" # Url home
ROOT_PATH_LOGIN: str = "https://x.com/i/flow/login" # Url de login
URI_PATH: str = "g1" # @id da conta do Twitter


# dados do usuário para login através do arquivo .env
EMAIL_ACCOUNT: str = os.getenv("EMAIL_ACCOUNT")
USER_ACCOUNT: str = os.getenv("USER_ACCOUNT")
USER_PASSWORD: str = os.getenv("USER_PASSWORD")

PERSIST_TWT: bool = True

PIXELS_PER_LINE: int = 60
SCROLL_STEP: int = 3 * PIXELS_PER_LINE