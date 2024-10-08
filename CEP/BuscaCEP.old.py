from selenium import webdriver as wd
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pyautogui as pag

def launch_browser():
    options = wd.ChromeOptions()
    options.add_experimental_option("detach", True)
    _driver = wd.Chrome(options=options)
    _driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
    return _driver


def query_cep(cep):
    driver = launch_browser()

    pag.sleep(2)

    cep_searchbox = driver.find_element(By.NAME, 'endereco')

    cep_searchbox.send_keys(cep)
    pag.sleep(1)
    cep_searchbox.send_keys(Keys.RETURN)
    pag.sleep(4)
    logradouro_text = \
    driver.find_elements(By.XPATH, '/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[1]')[0].text
    bairro_text = driver.find_elements(By.XPATH, '/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[2]')[
        0].text
    uf_text = driver.find_elements(By.XPATH, '/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[3]')[
        0].text
    cep_text = driver.find_elements(By.XPATH, '/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[4]')[
        0].text

    print(f"Logradouro: {logradouro_text}\nBairro: {bairro_text}\nLocalidade/UF: {uf_text}\nCEP: {cep_text}")

    driver.close()

query_cep('02411000')