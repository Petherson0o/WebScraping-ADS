from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time



ROOT_PATH: str = "https://x.com/"
URI_PATH: str = "g1"

# Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# Inicia o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(f"{ROOT_PATH}{URI_PATH}")

time.sleep(5)  # espera carregar os primeiros tweets
# Define o deslocamento (3 linhas ≈ 180px, ajuste conforme sua tela)
pixels_por_linha = 60
scroll_step = 3 * pixels_por_linha

twt_dict = {}

# tweets = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
# print(f"tweets: {len(tweets)}")
# Rola continuamente

for i in range(45):  # 20 passos = 20 segundos
    driver.execute_script(f"window.scrollBy(0, {scroll_step});")
    time.sleep(1)  # espera 1 segundo antes do próximo scroll

    elements = driver.find_elements(By.TAG_NAME, 'article')  # procura pela tag <article>
    for e in elements:
        tweet = e.find_element(By.XPATH, "//article[@data-testid='tweet']")
        text_divs = tweet.find_element(By.XPATH, ".//div[@data-testid='tweetText']").text
        text = "".join([t for t in text_divs])
        link = e.find_element(By.XPATH, ".//a[contains(@href, '/status/')]").get_attribute("href")
    #tweets = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
    #link = driver.find_element(By.XPATH, ".//a[contains(@href, '/status/')]").get_attribute("href")

        twt_dict[link] = text
    #print(f"tweets: {len(tweets)}")
for key,value in twt_dict.items():
    print(f"{key}: {value}\n")

"""
last_height = driver.execute_script("return document.body.scrollHeight")
scroll_count = 0
while scroll_count < 20:  # Limita o número de rolagens para evitar um loop infinito
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Espera o conteúdo carregar após a rolagem
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    scroll_count += 1

actions = ActionChains(driver)

# # Pega os artigos (tweets)
# tweets = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
# print(f"tweets: {len(tweets)}")
# tweets1 = driver.find_elements(By.TAG_NAME, "article")
# print(f"tweets: {len(tweets1)}")

for i, tweet in enumerate(tweets, start=1):
    try:
        # rola até o tweet atual
        actions.move_to_element(tweet).perform()
        time.sleep(2)  # espera carregar o próximo bloco de tweets

        # tenta pegar o texto do tweet
        text_divs = tweet.find_elements(By.XPATH, ".//div[@data-testid='tweetText']")
        text = " ".join([t.text for t in text_divs])

        #print(f"--- Tweet {i} ---\n{text}\n")
    except Exception as e:
        # print(f"Tweet {i} não tem texto (imagem/vídeo/repost)\n")
        continue
"""
"""
    # Rolagem da página para carregar mais postagens
    last_height = driver.execute_script("return document.body.scrollHeight")


    scroll_count = 0
    while scroll_count < 20: # Limita o número de rolagens para evitar um loop infinito
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2) # Espera o conteúdo carregar após a rolagem
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        scroll_count += 1

    # Encontrando todas as postagens após a rolagem
    # elements = driver.find_elements(By.TAG_NAME, 'article')
    elements = driver.find_elements(By.XPATH, "//div[@data-testid='tweetText']")

    actions = ActionChains(driver)
    for el in elements:
        actions.move_to_element(el).perform()
        time.sleep(1)  # força carregamento

    print(f"Número de postagens encontradas: {len(elements)}")

    for i, e in enumerate(elements):
        try:
            # Algumas postagens podem ter texto, outras podem ser retweets, etc.
            # Vamos tentar encontrar o texto principal dentro da postagem.
            # post_text = e.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetText"]').text
            post_text = e.text
            print(f"--- Postagem {i+1} ---")
            print(post_text)
            print("--------------------\n")
        except Exception:
            # Ignora elementos que não têm o texto da postagem de forma esperada
            continue

except Exception as ex:
    print(f"Ocorreu um erro: {ex}")

finally:
    if 'driver' in locals() and driver is not None:
        driver.quit()

"""
from db import Session
from Models.models import Post

session = Session()
for key, value in twt_dict.items():
    try:
        post = Post(link=key, nome_portal=URI_PATH ,texto_postagem=value)
        session.add(post)
        session.commit()
        print("Tweet cadastrado no BD")
        driver.get(key)
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
    finally:
        session.close()

