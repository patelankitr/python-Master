from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def __init__(self, driver):
    self.driver = driver


def verify_element_is_present_on_screen(self, locator_type, locator_value, comment, wait):
        element = WebDriverWait(self.driver, wait).until(ec.presence_of_element_located((locator_type, locator_value)))
    # Check if the element is present
        if element is not None:
            print(f"Print: '{comment}' is present on screen")
        else:
            print(f"Print: '{comment}' is NOT present on screen")