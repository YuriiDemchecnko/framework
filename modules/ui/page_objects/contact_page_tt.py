from time import sleep
from modules.ui.page_objects.base_tt import Base
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


class ContactPage(Base):
    def __init__(self, driver=None):
        # Call the constructor of the Base class
        super().__init__(driver)

    def open_contact(self, name):
        # Find the contact element by its name and click it to open the contact details
        self.find_element("xpath", f"//td[contains(text(), '{name}')]").click()

    def return_button_press(self):
        self.find_element("id", "return").click()

    def contact_edit(self, data={}):
        # Click the edit button to enter edit mode for the contact
        self.find_element("id", "edit-contact").click()

        sleep(0.5)  # temp solution

        # Find all necessary input fields and the submit button using their locators
        # Clear the existing value and set the new value for the input field
        for key, value in data.items():
            input_name = self.find_element("id", key)
            input_name.send_keys(Keys.CONTROL + "a")
            input_name.send_keys(Keys.DELETE)
            input_name.send_keys(value)

        # Click the submit button to submit the form
        self.find_element("id", "submit").click()

    def add_contact(self, data={}):
        # Click the 'add a new contact' button to enter add contact mode
        self.find_element("id", "add-contact").click()

        # Find all necessary input fields and the submit button using their locators
        for key, value in data.items():
            self.find_element("id", key).send_keys(value)

        # Click the submit button to submit the form
        self.find_element("id", "submit").click()

    def delete_contact(self):
        # Click the 'delete contact' button to delete it
        self.find_element("id", "delete").click()
        # Click dialog button OK
        alert = Alert(self.driver)
        alert = self.wait.until(self.EC.alert_is_present())
        alert.accept()
