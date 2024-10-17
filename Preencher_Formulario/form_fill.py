from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui

form_browser = webdriver.Chrome()

form_browser.get("https://pt.surveymonkey.com/r/WLXYDX2")

pyautogui.sleep(6)

name = form_browser.find_element(By.NAME, "166517069")

name.send_keys("Amanda Martins")

pyautogui.sleep(1)

email = form_browser.find_element(By.NAME, "166517072")

email.send_keys("amanda.martins@gmail.com")

pyautogui.sleep(1)

telephone = form_browser.find_element(By.NAME, "166517070")

telephone.send_keys("11987564231")

pyautogui.sleep(1)

#TODO: Radio Buttons

radio_button = form_browser.find_element(By.ID, '166517071_1215509813_label')

radio_button.click()

pyautogui.sleep(1)

obs = form_browser.find_element(By.NAME, "166517073")

obs.send_keys("Sei automatizar processos com Python")

send_button = form_browser.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button')

pyautogui.sleep(10)
#send_button.click()
