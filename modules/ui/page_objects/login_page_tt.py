from modules.ui.page_objects.base_tt import Base
from selenium.webdriver.common.by import By


class LoginPage(Base):
    def __init__(self, driver=None):
        # Call the constructor of the Base class
        super().__init__(driver)

    def login(
        self,
        email=Base.CREDENTIALS["email"],
        password=Base.CREDENTIALS["pass"],
    ):
        # Find the login elements, input the credentials and click the submit
        email_input = self.driver.find_element(By.ID, "email")
        pass_input = self.driver.find_element(By.ID, "password")
        submit_button = self.driver.find_element(By.ID, "submit")

        email_input.send_keys(email)
        pass_input.send_keys(password)
        submit_button.click()

    def logout(self):
        # Find the logout button and click it
        logout_button = self.wait.until(
            self.EC.presence_of_element_located((By.ID, "logout"))
        )
        logout_button.click()
