import pytest
from selenium import webdriver
from framework.readers.jsonFileReader import Reader
from selenium.webdriver.edge.service import Service as EdgeService


def __init__(self, driver):
    self.driver = driver


@pytest.fixture(scope="function")
def setup():
    """
    Set up WebDriver instance and configuration for each test.
    """
    # Read configuration using Reader
    reader = Reader()
    config = reader.get_config()

    if not config:
        pytest.fail("No configuration found for the specified run key.")

    platform = config.get("platform")
    browser = config.get("browser")
    env = config.get("env")

    if not env or not browser:
        pytest.fail("Configuration must include 'env' and 'browser'.")

    # Set up WebDriver instance
    if platform == 'web':
        if browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        elif browser == 'edge':
            driver = webdriver.Edge(service=EdgeService())
        else:
            pytest.fail(f"Unsupported browser: {browser}")
    else:
        pytest.fail("Currently, We are supporting WEB only, Mobile support will be soon! ")

    driver.get(env)
    driver.maximize_window()
    yield driver
    driver.quit()