from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # Находим все элементы input на странице
    elements = browser.find_elements(By.TAG_NAME, "input")

    # Заполняем каждый найденный input
    for element in elements:
        element.send_keys("Мой ответ")

    # Находим и нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()