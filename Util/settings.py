import os
from dotenv import load_dotenv

load_dotenv()

# url das páginas
ROOT_PATH: str = "https://x.com/" # Url home
ROOT_PATH_LOGIN: str = "https://x.com/i/flow/login" # Url de login
URI_PATH: str = "g1" # @id da conta do Twitter


# dados do usuário para login através do arquivo .env
EMAIL_ACCOUNT: str = os.getenv("EMAIL_ACCOUNT")
USER_ACCOUNT: str = os.getenv("USER_ACCOUNT")
USER_PASSWORD: str = os.getenv("USER_PASSWORD")