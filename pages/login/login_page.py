import time


from selenium.webdriver.common.by import By
from framework.web.screenshot import take_element_screenshot, compare_element_images
from framework.web.element import Element
from framework.web.wait import Wait



class LoginTest:


    def __init__(self, driver):
        self.driver = driver
        self.wait = Wait(driver)
        self.element = Element(self.driver)

    def screenshot_command_option(self,request):
        take_screenshot = request.config.getoption("--take-screenshot")  # Get the string ("True" or "False")
        # Convert the string to a boolean
        take_screenshot = take_screenshot.lower() == "true"  # Convert to True if "True" is passed
    def take_screenshot_of_agree_button(self):
        try:
            agree_button = self.driver.find_element(By.ID, 'didomi-notice-agree-button')

            # Case 1: If take_screenshot is True, take a screenshot and compare
            if self.screenshot_command_option:
                agree_button_path = take_element_screenshot(self.driver, agree_button, "agree_button")
                assert compare_element_images("agree_button.png"), "Agree button does not match the baseline!"
            # Case 2: If take_screenshot is False, just compare the screenshot without taking a new one
            else:
                assert compare_element_images("agree_button.png"), "Agree button does not match the baseline!"

        except Exception as e:
            print(f"Agree and close button not found: {e}")

    def login_with_valid_credencial(self):
        wait = Wait(self.driver)

        self.element.click('agree_button')
        wait.wait_until_element_is_visible(By.ID, 'loginbox_login_input',30)
        self.driver.find_element(By.ID, "loginbox_login_input").send_keys("raven_flame")
        self.driver.find_element(By.ID, "loginbox_password_input").send_keys("Ankit007")
        time.sleep(10)
        self.element.click('login_button')
        #self.driver.find_element(By.ID, "func_loginbutton").click()


    def Handle_popup(self):
        #self.driver.switch_to.frame("ifm")
        wait = Wait(self.driver)
        try:
            popup = self.driver.find_element(By.XPATH, "//div[@class='button_close func_close_button']")

            # Case 1: If take_screenshot is True, take a screenshot and compare
            if self.screenshot_command_option:
                popup_screenshot_path = take_element_screenshot(self.driver, popup, "popup_close_button")
                print(f"Popup screenshot saved at: {popup_screenshot_path}")
                assert compare_element_images(
                    "popup_close_button.png"), "Popup close button does not match the baseline!"
            # Case 2: If take_screenshot is False, just compare the screenshot without taking a new one
            else:
                assert compare_element_images(
                    "popup_close_button.png"), "Popup close button does not match the baseline!"

            popup.click()
            print("Popup handled successfully.")
        except Exception as e:
            print(f"Error handling popup: {e}")

        wait.wait_until_element_is_visible(By.XPATH, "(//div[@class='button_close func_close_button'])[1]",30)
        self.driver.find_element(By.XPATH, "(//div[@class='button_close func_close_button'])[1]").click()