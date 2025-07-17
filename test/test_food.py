from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_01():
    driver = webdriver.Chrome()
    driver.get("https://valval-82.github.io")
    assert driver.find_element(By.TAG_NAME, "h1").text == "Простой бутерброд с сыром"

def test_02():
    driver = webdriver.Chrome()
    driver.get("https://valval-82.github.io")
    assert driver.find_element(By.TAG_NAME, "h2").text == "Что нужно"

def test_03():
    driver = webdriver.Chrome()
    driver.get("https://valval-82.github.io")
    assert driver.find_element(By.TAG_NAME, "p").text == "Хлеб, сливочное масло, сыр, зелень (по желанию)"

def test_04_how():
    driver = webdriver.Chrome()
    driver.get("https://valval-82.github.io")
    assert driver.find_element(By.CSS_SELECTOR, "p ~ h2").text == "Как приготовить"

def test_05_steps():
    driver = webdriver.Chrome()
    driver.get("https://valval-82.github.io")
    assert driver.find_element(By.CSS_SELECTOR, "p:nth-of-type(2)").text == "1. Намажьте хлеб маслом."
    assert driver.find_element(By.CSS_SELECTOR, "p:nth-of-type(3)").text == "2. Положите сверху ломтик сыра."
    assert driver.find_element(By.CSS_SELECTOR, "p:nth-of-type(4)").text == "3. Добавьте зелень, если хотите."
    assert driver.find_element(By.CSS_SELECTOR, "p:nth-of-type(5)").text == "4. Бутерброд готов!"
