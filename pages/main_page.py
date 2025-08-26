from utils.locators import Locators
from base.base_object import BaseObject
from support.assertions import Assertions
from config import URL


class MainPage(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.assertion = Assertions
        self.locators = Locators

    @classmethod
    def scroll_to_bottom(cls, driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_text_how_much_does_it_cost(self):
        self.click(self.locators.HOW_MUCH_DOES_IT_COST_ACCORDION)
        self.get_text(self.locators.HOW_MUCH_DOES_IT_COST_TEXT)

    def get_text_can_i_have_many_scooters(self):
        self.click(self.locators.CAN_I_HAVE_MANY_SCOOTERS_ACCORDION)
        self.get_text(self.locators.CAN_I_HAVE_MANY_SCOOTERS_TEXT)

    def get_text_how_to_pay(self):
        self.click(self.locators.HOW_TO_PAY_ACCORDION)
        self.get_text(self.locators.HOW_TO_PAY_TEXT)

    def get_text_can_i_order_today(self):
        self.click(self.locators.CAN_I_ORDER_FOR_TODAY_ACCORDION)
        self.get_text(self.locators.CAN_I_ORDER_FOR_TODAY_TEXT)

    def get_text_can_i_prolong_or_return_earlier(self):
        self.click(self.locators.CAN_PROLONG_OR_RETURN_EARLIER_ACCORDION)
        self.get_text(self.locators.CAN_PROLONG_OR_RETURN_EARLIER_TEXT)

    def get_text_carger_with_scooter(self):
        self.click(self.locators.CHARDER_WITH_SCOOTER_ACCORDION)
        self.get_text(self.locators.CHARDER_WITH_SCOOTER_TEXT)

    def get_text_can_cancel(self):
        self.click(self.locators.CAN_CANCEL_ACCORDION)
        self.get_text(self.locators.CAN_CANCEL_TEXT)

    def get_text_leave_far_from_mkad(self):
        self.click(self.locators.LEAVE_FAR_FROM_MKAD_ACCORDION)
        self.get_text(self.locators.LEAVE_FAR_FROM_MKAD_TEXT)

    def is_question_text_correct(self):
        self.assertion.assert_equal(
            expected=message,
            actual=self.get_text(self.ERROR_MESSAGE)
        )
