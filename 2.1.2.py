import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открываем страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    # 1. Находим элемент-картинку (сундук)
    treasure_chest = browser.find_element(By.CSS_SELECTOR, "img#treasure")

    # 2. Извлекаем значение атрибута 'valuex'
    x_value = treasure_chest.get_attribute("valuex")
    print(f"Значение атрибута valuex: {x_value}")

    # 3. Вычисляем ответ, преобразуя строку в число
    # Убедимся, что извлечённое значение действительно является числом
    if x_value is not None and x_value.isdigit():
        y = calc(x_value)
        print(f"Вычисленный ответ: {y}")
    else:
        print("Не удалось получить корректное значение x.")
        # Можно добавить обработку ошибки, но по заданию значение должно быть
        y = calc(0) # fallback, но лучше так не делать

    # 4. Вводим ответ в текстовое поле
    input_field = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input_field.send_keys(y)

    # 5. Отмечаем checkbox "I'm the robot"
    checkbox = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    checkbox.click()

    # 6. Выбираем radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.CSS_SELECTOR, "input#robotsRule")
    radiobutton.click()

    # 7. Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Небольшая пауза, чтобы увидеть результат перед закрытием окна
    time.sleep(5)

finally:
    # Закрываем браузер
    browser.quit()