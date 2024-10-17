import pandas.core.series
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import pyautogui

import os

import pandas as pd
from openpyxl import load_workbook

# form_browser = webdriver.Chrome()
# form_browser.get("https://pt.surveymonkey.com/r/WLXYDX2")


def fill_webform(data: pandas.core.series.Series):
    form_browser = webdriver.Chrome()
    form_browser.get("https://pt.surveymonkey.com/r/WLXYDX2")

    name = WebDriverWait(form_browser, 10).until(lambda x: x.find_element(By.NAME, "166517069"))
    name.send_keys(str(data['Nome']))

    email = WebDriverWait(form_browser, 10).until(lambda x: x.find_element(By.NAME, "166517072"))
    email.send_keys(str(data['Email']))

    phone_number = WebDriverWait(form_browser, 10).until(lambda x: x.find_element(By.NAME, "166517070"))
    phone_number.send_keys(str(data['Telefone']))

    obs = WebDriverWait(form_browser, 10).until(lambda x: x.find_element(By.NAME, "166517073"))
    obs.send_keys(str(data['Sobre']))

    match data['Sexo']:
        case 'Feminino':
            fem_radio_btn = WebDriverWait(form_browser, 10).until(lambda x: x.find_element(By.ID, "166517071_1215509813_label"))
            fem_radio_btn.click()
        case 'Masculino':
            male_radio_btn = WebDriverWait(form_browser, 10).until(lambda x: x.find_element(By.ID, "166517071_1215509812_label"))
            male_radio_btn.click()
        case _:
            pass

    send_btn = WebDriverWait(form_browser, 10).until(lambda x: x.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button'))
    send_btn.click()

    pyautogui.sleep(5)


file_dir = os.path.dirname(os.path.abspath(os.path.abspath(__file__)))
filename = os.path.join(file_dir, "DadosFormulario.xlsx")

data = pd.read_excel(filename, sheet_name='Dados')
data.reset_index()

for index, row in data.iterrows():
    fill_webform(row)
