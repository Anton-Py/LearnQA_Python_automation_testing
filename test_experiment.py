def test_hello_selenium1(driver):
    driver.get(url=driver.base_url)
    assert driver.title == "Your Store"


def test_hello_selenium2(driver):
    driver.get(url=driver.base_url)
    # driver.save_screenshot("test.png")
    assert driver.title == "YourStore"
