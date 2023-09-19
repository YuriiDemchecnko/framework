from time import sleep
from modules.ui.page_objects.base_tt import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert


class ContactPage(Base):
    def __init__(self, driver=None):
        # Call the constructor of the Base class
        super().__init__(driver)

    def open_contact(self, name):
        # Find the contact element by its number and click it to open the contact details
        try:
            element = self.wait.until(
                self.EC.presence_of_element_located(
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
        edit = self.wait.until(
            self.EC.presence_of_element_located((By.ID, "edit-contact"))
        )
        edit.click()

        sleep(0.5)  # temp solution

        # Find all necessary input fields and the submit button using their locators
        # Clear the existing value and set the new value for the input field
        for key, value in data.items():
            input_name = self.wait.until(
                self.EC.presence_of_element_located((By.ID, key))
            )
            input_name.send_keys(Keys.CONTROL + "a")
            input_name.send_keys(Keys.DELETE)
            input_name.send_keys(value)

        submit_button = self.wait.until(
            self.EC.presence_of_element_located((By.ID, "submit"))
        )

        # Click the submit button to submit the form
        submit_button.click()

    def add_contact(self, data={}):
        # Click the 'add a new contact' button to enter add contact mode
        add_button = self.wait.until(
            self.EC.presence_of_element_located((By.ID, "add-contact"))
        )
        add_button.click()
        # Find all necessary input fields and the submit button using their locators
        for key, value in data.items():
            input_name = self.wait.until(
                self.EC.presence_of_element_located((By.ID, key))
            )
            input_name.send_keys(value)

        submit_button = self.wait.until(
            self.EC.presence_of_element_located((By.ID, "submit"))
        )
        # Click the submit button to submit the form
        submit_button.click()

    def delete_contact(self):
        # Click the 'delete contact' button to delete it
        delete_contact_button = self.wait.until(
            self.EC.presence_of_element_located((By.ID, "delete"))
        )
        delete_contact_button.click()
        # Click dialog button OK
        alert = Alert(self.driver)
        alert = self.wait.until(self.EC.alert_is_present())
        alert.accept()
