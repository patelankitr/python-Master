import pytest
from framework.init.base import setup
from pages.login.login_page import LoginTest

@pytest.mark.smoke
def test_login_and_take_screenshot(setup):
        driver = setup
        login = LoginTest(driver)

        # Step 1: Take screenshot of agree button
        login.take_screenshot_of_agree_button()
        # Step 2: Login
        login.login_with_valid_credencial()
        # Step 3: Handle the login iframe popup
        #login.Handle_popup()