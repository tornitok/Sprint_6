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

    # Order flow locators
    ORDER_BUTTONS = (By.XPATH, "//button[contains(., 'Заказать')]")
    # First modal - customer info
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.CLASS_NAME, 'select-search')
    METRO_OPTIONS = (By.CSS_SELECTOR, '.select-search__select .select-search__option')
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[contains(., 'Далее')]")

    # Second modal - renting info
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-root')
    RENTAL_PERIOD_OPTIONS = (By.CLASS_NAME, 'Dropdown-option')
    COLOR_BLACK = (By.ID, 'black')
    COLOR_GREY = (By.ID, 'grey')
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # More specific selector for the 'Заказать' button inside the order modal
    BUTTON_ORDER = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[normalize-space(text())='Заказать']")

    # Confirmation modal
    CONFIRM_MODAL = (By.CLASS_NAME, 'Order_Modal__YZ-d3')
    CONFIRM_MODAL_TEXT = (By.CLASS_NAME, 'Order_Text__2broi')
    BUTTON_YES = (By.XPATH, "//button[contains(., 'Да')]")

    # Logos
    LOGO_SCOOTER = (By.XPATH, "//div[contains(@class, 'Header')]/a")
    LOGO_YANDEX = (By.CSS_SELECTOR, 'a.Header_LogoYandex__3TSOI')

    # --- Helpers / overlays ---
    # Datepicker overlay (used to wait until datepicker is closed)
    DATEPICKER_OVERLAY = (By.CSS_SELECTOR, '.react-datepicker, .DatePicker, .DatePicker__overlay')

    # Cookie consent - container and accept button inside it.
    # The page may render a cookie consent banner that blocks clicks; selector targets the wrapper and a button inside.
    COOKIE_CONSENT = (By.CSS_SELECTOR, '.App_CookieConsent__1yUIN')
    COOKIE_CONSENT_ACCEPT = (By.CSS_SELECTOR, '.App_CookieConsent__1yUIN button')
