from selenium import webdriver
from selenium.webdriver.common.by import By

def open_saucedemo():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    # поиск текстового поля username
    username = driver.find_element(By.CSS_SELECTOR, '#user-name')
    
    # поиск текстового поля password
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    
    # поиск кнопки submit
    submit = driver.find_element(By.CSS_SELECTOR, '#login-button')
    
    print('Все элементы найдены')

open_saucedemo()
