import time

from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
import pyautogui as pag

import xlsxwriter as excel
import os


def launchBrowser():
    options = wd.ChromeOptions()
    options.add_experimental_option("detach", True)
    _driver = wd.Chrome(options=options)

    _driver.get("http://www.google.com/")
    return _driver


driver = launchBrowser()
pag.sleep(2)
searchbox = driver.find_element(By.NAME, "q")
searchbox.send_keys('Dólar hoje')
pag.sleep(2)
searchbox.send_keys(Keys.RETURN)
pag.sleep(2)
resultbox = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
dolar = resultbox.text

pag.sleep(2)
searchbox = driver.find_element(By.NAME, "q")
pag.sleep(2)
searchbox.clear()
pag.sleep(2)
searchbox.send_keys('Euro hoje')
pag.sleep(2)
searchbox.send_keys(Keys.RETURN)
pag.sleep(2)
resultbox = driver.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
euro = resultbox.text

print(f"Dolar: {dolar}, Euro: {euro}")


driver.close()

pag.sleep(2)

filename = "C:\\Users\\trjeh\\PycharmProjects\\AulasRPA\\DolarEuro.xlsx"

workbook = excel.Workbook(filename)

sheet1 = workbook.add_worksheet()

dolar = dolar.replace(",", ".")
euro = euro.replace(",", ".")

dolar_float = float(dolar)
euro_float = float(euro)

sheet1.write("A1", 'Dolar')
sheet1.write('B1', 'Euro')
sheet1.write('A2', dolar_float)
sheet1.write('B2', euro_float)

workbook.close()

os.startfile(filename)