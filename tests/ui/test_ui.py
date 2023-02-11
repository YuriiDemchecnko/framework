import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(
        service=Service(r"C:\\Users\\Deedg\\framework\\" + "chromedriver.exe")
    )

    driver.get("https://github.com/login")

    # incorrect user/email test
    login_elem = driver.find_element(By.ID, "login_field")
    login_elem.send_keys("wronemail@wrong.com")

    # incorrect pass test
    pass_elem = driver.find_element(By.ID, "password")
    pass_elem.send_keys("wrong password")

    # sign in button click test
    btn_elem = driver.find_element(By.NAME, "commit")
    btn_elem.click()

    # page title name test
    assert driver.title == "Sign in to GitHub · GitHub"

    driver.close()
