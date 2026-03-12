from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # Открываем браузер
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    print("Страница загружена. Ждем цену $100...")

    # Ждем, пока цена не станет $100 (ожидание до 15 секунд)
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    print("Цена достигла $100! Нажимаем Book...")

    # Нажимаем кнопку Book
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    print("Решаем математическую задачу...")

    # Решаем математическую задачу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Вводим ответ
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    print("Ждем появление окна с ответом...")

    # Ждем появления ответа в алерте
    WebDriverWait(browser, 5).until(EC.alert_is_present())

    # Получаем текст из алерта
    alert = browser.switch_to.alert
    alert_text = alert.text
    answer = alert_text.split()[-1]

    print("=" * 50)
    print(f"ОТВЕТ: {answer}")
    print("=" * 50)
    print("\nОкно с ответом сейчас закроется, но ответ уже сохранен выше!")
    print("Вы можете скопировать его отсюда.")

    # Даем время прочитать сообщение (5 секунд)
    time.sleep(5)

    # Принимаем алерт (закрываем окно с ответом)
    alert.accept()

    # Дополнительное время, чтобы увидеть страницу после закрытия алерта
    print("\nДаю еще 15 секунд, чтобы вы могли осмотреться...")
    print("Браузер закроется автоматически через 15 секунд.")
    time.sleep(15)

except Exception as e:
    print(f"Произошла ошибка: {e}")
    print("Ожидание 20 секунд перед закрытием...")
    time.sleep(20)

finally:
    # Закрываем браузер
    print("Закрываю браузер...")
    browser.quit()