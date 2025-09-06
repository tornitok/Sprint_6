from utils.locators import Locators
from base.base_object import BaseObject
from support.assertions import Assertions
from utils.constants import QuestionText
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class MainPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.assertion = Assertions
        self.locators = Locators
        self.questions = QuestionText
        self.close_cookie_banner_if_present()

    def close_cookie_banner_if_present(self):
        try:
            banner = self.driver.find_element(By.CLASS_NAME, "App_CookieConsent__1yUIN")
            button = banner.find_element(By.TAG_NAME, "button")
            button.click()
        except NoSuchElementException:
            pass
        except Exception:
            pass

    def check_question_text(self, accordion_locator, text_locator, expected_text):
        self.click(accordion_locator)
        actual_text = self.get_text(text_locator)
        self.assertion.assert_equal(
            expected=expected_text,
            actual=actual_text
        )