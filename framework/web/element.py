import json

from selenium.webdriver.common.by import By


class Element:
    def __init__(self, driver, file_path = "D:\Projects\Python-Framework\pages\login\login_locator.json"):
        self.file_path = file_path
        self.locators = self.load_locators()
        self.locator_reader = file_path
        self.driver = driver


    def load_locators(self):
        """
        Loads the locators from the JSON file and returns them as a dictionary.
        """
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading locator file: {e}")
            return {}

    def get_locator(self, locator_name):
        """
        Retrieves the locator details based on the locator name.
        """
        print(f"locator_name: '{locator_name}'")
        locator = self.locators.get(locator_name)
        if locator:
            print(f"Found locator for {locator_name}: {locator}")
            return locator
        else:
            print(f"Locator {locator_name} not found.")
            return None



    def click(self, locator_name):
        locator = self.get_locator(locator_name)
        print(f"locator: '{locator}'")
        if locator:
            locator_type = locator.get("locator_type").lower()
            locator_value = locator.get(f"{locator['platform']}_locator")
            print(f"Object Name: {locator_name}")
            print(f"locator_value: '{locator_value}'")
            print(f"locator_type: '{locator_type}'")


            if locator_type == 'xpath':
                locator = self.driver.find_element(By.XPATH, locator_value)
            elif locator_type == "id":
                locator = self.driver.find_element(By.ID, locator_value)
            elif locator_type == "cssSelector":
                locator = self.driver.find_element(By.CSS_SELECTOR, locator_value)
            else:
                print(f"Unsupported locator type: {locator_type}")
                return

            locator.click()
            print(f"Clicked on {locator_name}")
        else:
            print(f"Locator {locator_name} not found.")


