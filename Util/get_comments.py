from selenium.webdriver.remote.webelement import WebElement


from Util.settings import ROOT_PATH, URI_PATH
from Util.login import login_in_x


from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


from Models.db import Session
from Models.models import Post

session = Session()

try:
    posts: list[type[Post]] = session.query(Post).all()
except Exception as e:
    print(f"Erro ao obter a conexão: {e}")


driver = login_in_x()

pixels_por_linha = 60
scroll_step = 3 * pixels_por_linha

# Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver.get(f"{ROOT_PATH}{URI_PATH}")
time.sleep(5)

# Inicializa dicionário
twt_dict = {}
# Loop para capturar 30 tweets
while len(twt_dict) < 30:
    # Rola a página
    driver.execute_script(f"window.scrollBy(0, {scroll_step});")
    time.sleep(1)

    # Captura tweets visíveis
    elements: list[WebElement] = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")

    for e in elements:
        try:
            # Texto do tweet (ignora elementos sem texto)
            try:
                text_divs = e.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text
            except:
                text_divs = ""

            # Link do tweet
            link = e.find_element(By.XPATH, ".//a[contains(@href, '/status/')]").get_attribute("href")

            # Evita duplicados
            if link not in twt_dict:
                twt_dict[link] = text_divs
                print(f"[{len(twt_dict)}] {link} -> {text_divs[:50]}...")  # preview do texto
        except Exception as ex:
            print("Erro ao processar tweet:", ex)

print(f"\nTotal de tweets coletados: {len(twt_dict)}")



from Models.db import Session
from Models.models import Post

session = Session()
for key, value in twt_dict.items():
    try:
        post = Post(link=key, nome_portal=URI_PATH ,texto_postagem=value)
        session.add(post)
        session.commit()
        print("Tweet cadastrado no BD")
        # driver.get(key)
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
    finally:
        session.close()
