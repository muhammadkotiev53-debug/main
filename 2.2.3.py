import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    # 1. Заполняем текстовые поля: имя, фамилия, email
    browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("Иван")
    browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("Петров")
    browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("ivan.petrov@example.com")

    # 2. Работа с файлом
    # Создаём пустой текстовый файл в текущей директории
    file_name = "bio.txt"
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), file_name)

    # Создаём файл, если его нет
    with open(file_path, "w") as file:
        file.write("Это мой короткий био-файл для загрузки.")

    # Находим элемент для загрузки файла (input с type="file")
    file_input = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    # Отправляем путь к файлу в этот элемент
    file_input.send_keys(file_path)

    # 3. Нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Небольшая пауза, чтобы увидеть результат
    time.sleep(5)

finally:
    # Удаляем созданный файл после завершения
    if os.path.exists(file_path):
        os.remove(file_path)
    browser.quit()