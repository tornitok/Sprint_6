import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from config import URL

import requests

from urllib.parse import urlparse


@pytest.fixture
def get_chrome_options():
    options = Options()
    return options

@pytest.fixture
def get_web_driver(get_chrome_options):
    driver = webdriver.Chrome(
        options=get_chrome_options,
        service=Service(
            ChromeDriverManager().install()
        )
    )
    return driver

@pytest.fixture
def login_page(get_web_driver):
    get_web_driver.get(URL.BASE_URL)
    yield MainPage(get_web_driver)
    get_web_driver.quit()
