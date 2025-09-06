from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import urllib.parse


class url_contains:
    def __init__(self, text: str):
        self.text = text

    def __call__(self, driver: WebDriver) -> bool:
        return self.text in driver.current_url


class new_tab_opened:
    def __init__(self, original_handles: list[str]):
        self.original_handles = original_handles

    def __call__(self, driver: WebDriver) -> bool:
        return len(driver.window_handles) > len(self.original_handles)


class url_not_blank_and_contains:
    def __init__(self, keywords: list[str]):
        self.keywords = keywords

    def __call__(self, driver: WebDriver) -> bool:
        url = driver.current_url
        return url not in ("", "about:blank") and any(k in url.lower() for k in self.keywords)


class BaseObject:

    def __init__(self, driver: WebDriver, timeout: int = 5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # --- ожидания стандартные ---
    def _is_visible(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located(locator))

    def _is_clickable(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable(locator))

    def _is_present(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(ec.presence_of_element_located(locator))

    def _is_not_visible(self, locator: tuple[str, str]) -> bool:
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def _is_not_clickable(self, locator: tuple[str, str]) -> bool:
        try:
            self.wait.until_not(ec.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    def _are_present(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.wait.until(ec.presence_of_all_elements_located(locator))


    def click(self, locator: tuple[str, str], ensure_clickable: bool = True) -> None:
        element = self._is_clickable(locator) if ensure_clickable else self._is_present(locator)
        try:
            element.click()
        except Exception:
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center',inline:'center'}); arguments[0].click();",
                element,
            )

    def send_keys(self, locator: tuple[str, str], value: str, ensure_visible: bool = True) -> None:
        element = self._is_visible(locator) if ensure_visible else self._is_present(locator)
        element.send_keys(value)

    def get_current_url(self, wait_locator: tuple[str, str]) -> str:
        """Ждёт исчезновения элемента и возвращает текущий URL."""
        self._is_not_visible(wait_locator)
        return urllib.parse.unquote(self.driver.current_url)

    def get_text(self, locator: tuple[str, str]) -> str:
        return self._is_visible(locator).text
