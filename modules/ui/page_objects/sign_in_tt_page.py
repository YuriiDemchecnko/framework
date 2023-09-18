from time import sleep
from modules.ui.page_objects.base_tt import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert


class SignInPage(Base):
    URL = "https://thinking-tester-contact-list.herokuapp.com/"
    CREDENTIALS = {"email": "d1@example.com", "pass": "1234567"}

    def __init__(self):
        # Call the constructor of the Base class and initialize the WebDriverWait instance
        super().__init__()
        self.wait = WebDriverWait(
            self.driver,
            10,
            poll_frequency=1,
            ignored_exceptions=NoSuchElementException,
        )

    def go_to(self):
        # Navigate to the URL
        self.driver.get(SignInPage.URL)

    def login(self):
        # Find the login elements, input the credentials and click the submit
        email_input = self.driver.find_element(By.ID, "email")
        pass_input = self.driver.find_element(By.ID, "password")
        submit_button = self.driver.find_element(By.ID, "submit")

        email_input.send_keys(self.CREDENTIALS["email"])
        pass_input.send_keys(self.CREDENTIALS["pass"])
        submit_button.click()

    def logout(self):
        # Find the logout button and click it
        logout_button = self.wait.until(
            EC.presence_of_element_located((By.ID, "logout"))
        )
        logout_button.click()

    def open_contact(self, name):
        # Find the contact element by its number and click it to open the contact details
        try:
            element = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//td[contains(text(), '{name}')]")
                )
            )
            element.click()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def return_button_press(self):
        return_button = self.driver.find_element(By.ID, "return")
        return_button.click()

    def cancel_button_press(self):
        return_button = self.driver.find_element(By.ID, "cancel")
        return_button.click()

    def contact_edit(self, data={}):
        # Click the edit button to enter edit mode for the contact
        edit = self.driver.find_element(By.ID, "edit-contact")
        edit.click()

        sleep(0.5)  # temp solution

        # Find all necessary input fields and the submit button using their locators
        # Clear the existing value and set the new value for the input field
        for key, value in data.items():
            input_name = self.wait.until(EC.presence_of_element_located((By.ID, key)))
            input_name.send_keys(Keys.CONTROL + "a")
            input_name.send_keys(Keys.DELETE)
            input_name.send_keys(value)

        submit_button = self.wait.until(
            EC.presence_of_element_located((By.ID, "submit"))
        )

        # Click the submit button to submit the form
        submit_button.click()

    def add_contact(self, data={}):
        # Click the 'add a new contact' button to enter add contact mode
        add_button = self.wait.until(
            EC.presence_of_element_located((By.ID, "add-contact"))
        )
        add_button.click()
        # Find all necessary input fields and the submit button using their locators
        for key, value in data.items():
            input_name = self.wait.until(EC.presence_of_element_located((By.ID, key)))
            input_name.send_keys(value)

        submit_button = self.wait.until(
            EC.presence_of_element_located((By.ID, "submit"))
        )
        # Click the submit button to submit the form
        submit_button.click()

    def delete_contact(self):
        delete_contact_button = self.wait.until(
            EC.presence_of_element_located((By.ID, "delete"))
        )
        delete_contact_button.click()
        # Click dialog button OK
        alert = Alert(self.driver)
        alert.accept()
