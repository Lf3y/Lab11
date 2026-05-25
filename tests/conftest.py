import subprocess
import time
from collections.abc import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BASE_URL = "http://127.0.0.1:8000/index.html"


@pytest.fixture(scope="session")
def static_server() -> Generator[None, None, None]:
    """Запускает локальный HTTP-сервер для UI-тестов."""
    process = subprocess.Popen(
        ["python", "-m", "http.server", "8000"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(1)

    yield

    process.terminate()
    process.wait(timeout=5)


@pytest.fixture
def browser(static_server: None) -> Generator[webdriver.Chrome, None, None]:
    """Создает headless-браузер Chrome для Selenium-тестов."""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,720")

    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)

    yield driver

    driver.quit()
