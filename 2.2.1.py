import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math # Эта библиотека не нужна для сложения, но импортируем на всякий случай

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html") # Можно заменить на selects2.html

    # 1. Находим элементы с числами и получаем их текст
    num1_element = browser.find_element(By.CSS_SELECTOR, "span#num1")
    num2_element = browser.find_element(By.CSS_SELECTOR, "span#num2")

    num1 = int(num1_element.text)
    num2 = int(num2_element.text)

    # 2. Вычисляем сумму
    total = num1 + num2
    print(f"Найдены числа: {num1} и {num2}. Их сумма: {total}")

    # 3. Работаем с выпадающим списком
    #    Находим сам элемент <select>
    select_element = browser.find_element(By.CSS_SELECTOR, "select#dropdown")
    #    Создаём объект Select для работы с ним
    select = Select(select_element)

    #    Выбираем опцию по значению (value). total нужно преобразовать в строку!
    select.select_by_value(str(total))
    # Можно было бы выбрать и по видимому тексту: select.select_by_visible_text(str(total))

    # 4. Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Небольшая пауза, чтобы увидеть результат перед закрытием окна
    time.sleep(5)

finally:
    # Закрываем браузер
    browser.quit()