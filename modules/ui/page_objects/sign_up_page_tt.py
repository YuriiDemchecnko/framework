from modules.ui.page_objects.base_tt import Base
from selenium.webdriver.common.by import By


class SignupPage(Base):
    def __init__(self, driver=None):
        # Call the constructor of the Base class
        super().__init__(driver)

    def signup_button_press(self):
        signup_button = self.wait.until(
            self.EC.presence_of_element_located((By.ID, "signup"))
        )
        signup_button.click()
