from time import sleep
from modules.ui.page_objects.base_tt import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class SignInPage(Base):
    URL = "https://thinking-tester-contact-list.herokuapp.com/"
    CREDENTIALS = {"email": "d1@example.com", "pass": "1234567"}

    def __init__(self):
        # Call the constructor of the Base class and initialize the WebDriverWait instance
        super().__init__()
        self.wait = WebDriverWait(
            self.driver, 10, poll_frequency=1, ignored_exceptions=NoSuchElementException
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

    def open_contact(self, contact_number):
        # Find the contact element by its number and click it to open the contact details
        try:
            element = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//*[@id='myTable']/tr/td[{contact_number + 1}]")
                )
            )
            element.click()
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def contact_edit(
        self,
        first_name,
        last_name,
        city,
        dob,
        email,
    ):
        # Click the edit button to enter edit mode for the contact
        edit = self.driver.find_element(By.ID, "edit-contact")
        edit.click()

        sleep(0.5)  # temp solution

        # Find all necessary input fields and the submit button using their locators
        first_name_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "firstName"))
        )
        last_name_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "lastName"))
        )
        city_input = self.wait.until(EC.presence_of_element_located((By.ID, "city")))
        dob_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "birthdate"))
        )
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "email")))

        submit_button = self.wait.until(
            EC.presence_of_element_located((By.ID, "submit"))
        )

        # Clear the existing value and set the new value for the input field
        first_name_input.send_keys(Keys.CONTROL + "a")
        first_name_input.send_keys(Keys.DELETE)
        first_name_input.send_keys(first_name)

        last_name_input.send_keys(Keys.CONTROL + "a")
        last_name_input.send_keys(Keys.DELETE)
        last_name_input.send_keys(last_name)

        city_input.send_keys(Keys.CONTROL + "a")
        city_input.send_keys(Keys.DELETE)
        city_input.send_keys(city)

        dob_input.send_keys(Keys.CONTROL + "a")
        dob_input.send_keys(Keys.DELETE)
        dob_input.send_keys(dob)

        email_input.send_keys(Keys.CONTROL + "a")
        email_input.send_keys(Keys.DELETE)
        email_input.send_keys(email)

        # Click the submit button to submit the form
        submit_button.click()
