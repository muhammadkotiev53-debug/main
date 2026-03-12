import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        first_name.send_keys("Ivan")

        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        last_name.send_keys("Petrov")

        email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        email.send_keys("ivan@example.com")

        # Отправляем форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ждем загрузки страницы
        time.sleep(1)

        # Находим элемент с текстом приветствия
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # Проверяем, что ожидаемый текст совпадает с текстом на странице
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем обязательные поля
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
        first_name.send_keys("Ivan")

        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
        last_name.send_keys("Petrov")

        email = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
        email.send_keys("ivan@example.com")

        # Отправляем форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Ждем загрузки страницы
        time.sleep(1)

        # Находим элемент с текстом приветствия
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        # Проверяем, что ожидаемый текст совпадает с текстом на странице
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        browser.quit()


if __name__ == "__main__":
    unittest.main()