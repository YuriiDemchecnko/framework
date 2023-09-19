from modules.ui.page_objects.base_tt import Base
from selenium.webdriver.common.by import By

# from selenium.webdriver.support import expected_conditions as EC


class LoginPage(Base):
    def __init__(self, driver=None):
        # Call the constructor of the Base class
        super().__init__(driver)

    def go_to(self):
        # Navigate to the URL
        self.get(Base.URL)

    def login(self):
        # Find the login elements, input the credentials and click the submit
        email_input = self.driver.find_element(By.ID, "email")
        pass_input = self.driver.find_element(By.ID, "password")
        submit_button = self.driver.find_element(By.ID, "submit")

        email_input.send_keys(Base.CREDENTIALS["email"])
        pass_input.send_keys(Base.CREDENTIALS["pass"])
        submit_button.click()

    def logout(self):
        # Find the logout button and click it
        logout_button = self.wait.until(
            self.EC.presence_of_element_located((By.ID, "logout"))
        )
        logout_button.click()
