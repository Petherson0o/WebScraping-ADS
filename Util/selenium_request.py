from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicializando o driver
try:
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)

    # Acessando o X (antigo Twitter)
    driver.get("https://www.x.com/g1")

    # Tempo de espera para a página carregar completamente
    time.sleep(5)

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
    elements = driver.find_elements(By.TAG_NAME, 'article')

    print(f"Número de postagens encontradas: {len(elements)}")

    for i, e in enumerate(elements):
        try:
            # Algumas postagens podem ter texto, outras podem ser retweets, etc.
            # Vamos tentar encontrar o texto principal dentro da postagem.
            post_text = e.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetText"]').text
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