from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


def test_page_title(browser: webdriver.Chrome) -> None:
    """Проверяет заголовок страницы."""
    assert browser.title == "Форма обратной связи"


def test_form_fields_are_visible(browser: webdriver.Chrome) -> None:
    """Проверяет наличие всех полей формы."""
    assert browser.find_element(By.ID, "name").is_displayed()
    assert browser.find_element(By.ID, "email").is_displayed()
    assert browser.find_element(By.ID, "message").is_displayed()
    assert browser.find_element(By.ID, "submit-btn").is_displayed()


def test_successful_form_submit(browser: webdriver.Chrome) -> None:
    """Проверяет успешную отправку корректно заполненной формы."""
    browser.find_element(By.ID, "name").send_keys("Иван")
    browser.find_element(By.ID, "email").send_keys("ivan@example.com")
    browser.find_element(By.ID, "message").send_keys("Тестовое сообщение")
    browser.find_element(By.ID, "submit-btn").click()

    success_message = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "success-message"))
    )

    assert "успешно отправлена" in success_message.text.lower()


def test_empty_form_shows_validation_error(browser: webdriver.Chrome) -> None:
    """Проверяет сообщение об ошибке при пустой отправке формы."""
    browser.find_element(By.ID, "submit-btn").click()

    error_message = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "error-message"))
    )

    assert "заполните все поля" in error_message.text.lower()


def test_submit_button_text(browser: webdriver.Chrome) -> None:
    """Проверяет текст кнопки отправки."""
    button = browser.find_element(By.ID, "submit-btn")
    assert button.text == "Отправить"
