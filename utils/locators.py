from selenium.webdriver.common.by import By


class Locators:
    # Аккордионы вопросов
    HOW_MUCH_DOES_IT_COST_ACCORDION = (By.ID, 'accordion__heading-0')
    CAN_I_HAVE_MANY_SCOOTERS_ACCORDION = (By.ID, 'accordion__heading-1')
    HOW_TO_PAY_ACCORDION = (By.ID, 'accordion__heading-2')
    CAN_I_ORDER_FOR_TODAY_ACCORDION = (By.ID, 'accordion__heading-3')
    CAN_PROLONG_OR_RETURN_EARLIER_ACCORDION = (By.ID, 'accordion__heading-4')
    CHARDER_WITH_SCOOTER_ACCORDION = (By.ID, 'accordion__heading-5')
    CAN_CANCEL_ACCORDION = (By.ID, 'accordion__heading-6')
    LEAVE_FAR_FROM_MKAD_ACCORDION = (By.ID, 'accordion__heading-7')

    #Текст ответов
    HOW_MUCH_DOES_IT_COST_TEXT = (By.ID, 'accordion__panel-0')
    CAN_I_HAVE_MANY_SCOOTERS_TEXT = (By.ID, 'accordion__panel-1')
    HOW_TO_PAY_TEXT = (By.ID, 'accordion__panel-2')
    CAN_I_ORDER_FOR_TODAY_TEXT = (By.ID, 'accordion__panel-3')
    CAN_PROLONG_OR_RETURN_EARLIER_TEXT = (By.ID, 'accordion__panel-4')
    CHARDER_WITH_SCOOTER_TEXT = (By.ID, 'accordion__panel-5')
    CAN_CANCEL_TEXT = (By.ID, 'accordion__panel-6')
    LEAVE_FAR_FROM_MKAD_TEXT = (By.ID, 'accordion__panel-7')
