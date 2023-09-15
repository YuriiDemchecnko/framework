from time import sleep
from modules.ui.page_objects.base_tt import Base
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class SignInPage(Base):
    URL = "https://thinking-tester-contact-list.herokuapp.com/"

    def __init__(self):
        super().__init__()
        self.wait = WebDriverWait(
            self.driver, 10, poll_frequency=1, ignored_exceptions=NoSuchElementException
        )

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        login_elem = self.driver.find_element(By.ID, "email")
        login_elem.send_keys(username)
        pass_elem = self.driver.find_element(By.ID, "password")
        pass_elem.send_keys(password)
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()

    def logout(self):
        logout_button = self.wait.until(
            EC.presence_of_element_located((By.ID, "logout"))
        )
        logout_button.click()

    def open_first_contact(self):
        try:
            element = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='myTable']/tr/td[2]")
                )
            )
            element.click()
        except Exception as e:
            print(e)

    def first_contact_edit(
        self,
        first_name,
        last_name,
        city,
    ):
        # Enter edit form
        edit = self.driver.find_element(By.ID, "edit-contact")
        edit.click()

        sleep(0.5)  # temp solution

        # locators
        first_name_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "firstName"))
        )
        last_name_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "lastName"))
        )
        city_input = self.wait.until(EC.presence_of_element_located((By.ID, "city")))
        submit_button = self.wait.until(
            EC.presence_of_element_located((By.ID, "submit"))
        )

        # Actions
        first_name_input.clear()
        first_name_input.send_keys(Keys.CONTROL + "a")
        first_name_input.send_keys(Keys.DELETE)
        first_name_input.send_keys(first_name)

        last_name_input.send_keys(Keys.CONTROL + "a")
        last_name_input.send_keys(Keys.DELETE)
        last_name_input.send_keys(last_name)

        city_input.send_keys(Keys.CONTROL + "a")
        city_input.send_keys(Keys.DELETE)
        city_input.send_keys(city)

        # Press submit button
        submit_button.click()
