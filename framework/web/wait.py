

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Wait:

    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_is_visible(self, locator_type, locator_value, wait):
        """
        Wait until the element specified by the locator type and value is visible.

        Args:
            locator_type (By): The type of locator (e.g., By.XPATH, By.ID).
            locator_value (str): The value of the locator.

        Returns:
            WebElement: The visible element.
            :param locator_value:
            :param locator_type:
            :param wait:
        """
        """
        Waits until the element is present in the DOM but not necessarily visible.
        """
        try:
            WebDriverWait(self.driver, wait).until(
                ec.presence_of_element_located((locator_type, locator_value))
            )
            print(f"Element located by {locator_type}='{locator_value}' is present in the DOM.")
        except Exception as e:
            print(f"Timeout waiting for element located by {locator_type}='{locator_value}'. Exception: {e}")