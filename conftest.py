import pytest
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import MainPage
from pages.order_page import OrderPage
from config import URL


@pytest.fixture(scope='session')
def get_firefox_options():
    options = Options()
    options.set_preference("dom.webnotifications.enabled", False)
    return options

@pytest.fixture(scope='session')
def get_web_driver(get_firefox_options):
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(
        service=service,
        options=get_firefox_options
    )
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def main_page(get_web_driver):
    get_web_driver.get(URL.BASE_URL)
    get_web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    yield MainPage(get_web_driver)


@pytest.fixture(scope='function')
def order_page(get_web_driver):
    get_web_driver.get(URL.BASE_URL)
    yield OrderPage(get_web_driver)
    handles = get_web_driver.window_handles
    if len(handles) > 1:
        for h in handles[1:]:
            try:
                get_web_driver.switch_to.window(h)
                get_web_driver.close()
            except Exception:
                pass
        get_web_driver.switch_to.window(get_web_driver.window_handles[0])
