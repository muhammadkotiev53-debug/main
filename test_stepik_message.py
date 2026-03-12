import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Список ссылок на уроки
links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.mark.parametrize('link', links)
def test_stepik_message(browser, link):
    # Открыть страницу
    browser.get(link)

    # Авторизация
    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth"))
    )
    login_button.click()

    email_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='login']"))
    )
    email_input.send_keys("m-kotiev06@mail.ru")

    password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    password_input.send_keys("qugra1-dEsdic-bejcev")

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ждем, что авторизация прошла (кнопка логина исчезла)
    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "a.navbar__auth"))
    )

    # Ждем появления поля для ответа
    textarea = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area"))
    )

    # Очищаем поле (если там уже что-то есть) и вводим ответ
    textarea.clear()
    answer = math.log(int(time.time()))
    textarea.send_keys(str(answer))

    # Нажимаем кнопку "Отправить"
    send_button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    send_button.click()

    # Ждем появления фидбека и проверяем текст
    feedback = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.attempt__message pre"))
    )
    feedback_text = feedback.text

    # Проверяем, что текст фидбека - "Correct!"
    assert feedback_text == "Correct!", f"Ожидался 'Correct!', но получен: '{feedback_text}'"