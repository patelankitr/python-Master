
Here's an example of how to use markers:

```@pytest.mark.smoke
def test_smoke_1():
    assert True

@pytest.mark.smoke
def test_smoke_2():
    assert True

@pytest.mark.regression
def test_regression_1():
    assert True


```
Common Examples
Locator Strategy	Example Code
ID	driver.find_element(By.ID, "username")
Name	driver.find_element(By.NAME, "password")
Class Name	driver.find_element(By.CLASS_NAME, "login-button")
Tag Name	driver.find_element(By.TAG_NAME, "input")
CSS Selector	driver.find_element(By.CSS_SELECTOR, "div.container > a")
XPath	driver.find_element(By.XPATH, "//div[@id='main']")
Link Text	driver.find_element(By.LINK_TEXT, "Click here")
Partial Link Text	driver.find_element(By.PARTIAL_LINK_TEXT, "Click")
```