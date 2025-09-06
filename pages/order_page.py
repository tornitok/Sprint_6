from base.base_object import BaseObject, url_contains, new_tab_opened, url_not_blank_and_contains
from utils.locators import Locators
from support.assertions import Assertions
from config import URL
from selenium.webdriver import Keys


class OrderPage(BaseObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.assertion = Assertions
        self.locators = Locators

    def _dismiss_cookie(self) -> None:
        """If a cookie consent banner is present, try to accept it so it doesn't block clicks."""
        try:
            elems = self.driver.find_elements(*self.locators.COOKIE_CONSENT_ACCEPT)
            if elems:
                try:
                    elems[0].click()
                except Exception:
                    self.driver.execute_script("arguments[0].click();", elems[0])
        except Exception:
            pass

    def open_order_by_index(self, index: int = 0):
        buttons = self.driver.find_elements(*self.locators.ORDER_BUTTONS)
        if not buttons:
            raise AssertionError("Order buttons not found on page")

        # dismiss cookie if it blocks the buttons
        self._dismiss_cookie()

        btn = buttons[index if index >= 0 else len(buttons) + index]
        btn.click()

    def fill_personal_info(self, name: str, surname: str, address: str, metro: str | None, phone: str):
        self.send_keys(self.locators.INPUT_NAME, name)
        self.send_keys(self.locators.INPUT_SURNAME, surname)
        self.send_keys(self.locators.INPUT_ADDRESS, address)

        self.click(self.locators.INPUT_METRO)
        options = self.driver.find_elements(*self.locators.METRO_OPTIONS)
        chosen = next((o for o in options if metro and metro.lower() in o.text.lower()), options[0])
        chosen.click()

        self.send_keys(self.locators.INPUT_PHONE, phone)
        self.click(self.locators.BUTTON_NEXT)

    def fill_rental_info(self, date: str, rental_period_index: int, color: str | None, comment: str | None):
        self.send_keys(self.locators.INPUT_DATE, date)
        self.driver.find_element(*self.locators.INPUT_DATE).send_keys(Keys.ESCAPE)

        self._is_not_visible(self.locators.DATEPICKER_OVERLAY)

        self.click(self.locators.RENTAL_PERIOD_DROPDOWN)
        periods = self.driver.find_elements(*self.locators.RENTAL_PERIOD_OPTIONS)
        (periods[rental_period_index] if rental_period_index < len(periods) else periods[0]).click()

        if color:
            self.click(self.locators.COLOR_BLACK if color.lower() == "black" else self.locators.COLOR_GREY)

        if comment:
            self.send_keys(self.locators.INPUT_COMMENT, comment)

        self._dismiss_cookie()

        self.click(self.locators.BUTTON_ORDER)

    def confirm_order(self) -> str:
        self.click(self.locators.BUTTON_YES)
        self._is_visible(self.locators.CONFIRM_MODAL_TEXT)
        return self.get_text(self.locators.CONFIRM_MODAL_TEXT)

    def click_logo_scooter_and_check(self) -> str:
        self.click(self.locators.LOGO_SCOOTER)
        self.wait.until(url_contains(URL.BASE_URL.split("//")[1]))
        return self.driver.current_url

    def click_logo_yandex_and_switch(self) -> str:
        original_handles = self.driver.window_handles
        self.click(self.locators.LOGO_YANDEX)

        self.wait.until(new_tab_opened(original_handles))
        new_handle = next(h for h in self.driver.window_handles if h not in original_handles)
        self.driver.switch_to.window(new_handle)

        self.wait.until(url_not_blank_and_contains(["dzen", "zen", "yandex"]))
        return self.driver.current_url
