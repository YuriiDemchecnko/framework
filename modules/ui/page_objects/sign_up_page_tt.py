from modules.ui.page_objects.base_tt import Base


class SignupPage(Base):
    def __init__(self, driver=None):
        # Call the constructor of the Base class
        super().__init__(driver)

    def signup_button_press(self):
        self.find_element("id", "signup").click()

    def add_user(self, data={}):
        # Find all necessary input fields and the submit button
        # using their locators
        for key, value in data.items():
            self.find_element("id", key).send_keys(value)

        # Click the submit button to submit the form
        self.find_element("id", "submit").click()
