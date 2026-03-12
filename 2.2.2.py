import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # 1. Считываем значение x
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x_element.text
    print(f"Найден x: {x}")

    # 2. Вычисляем ответ
    y = calc(x)
    print(f"Вычисленный ответ: {y}")

    # 3. Вводим ответ в текстовое поле (оно может быть перекрыто)
    input_field = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input_field.send_keys(y)

    # 4. Находим checkbox и прокручиваем до него, затем кликаем
    checkbox = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    # 5. Находим radiobutton и прокручиваем до него, затем кликаем
    radiobutton = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    # 6. Находим кнопку и прокручиваем до неё, затем кликаем
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    # Небольшая пауза, чтобы увидеть результат
    time.sleep(5)

finally:
    browser.quit()