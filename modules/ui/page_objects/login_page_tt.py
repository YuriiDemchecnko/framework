from modules.ui.page_objects.base_tt import Base


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
        self.find_element("id", "email").send_keys(email)
        self.find_element("id", "password").send_keys(password)
        self.find_element("id", "submit").click()

    def get_title(self):
        return self.find_element("xpath", "/html/body/h1")

    def logout(self):
        # Find the logout button and click it
        self.find_element("id", "logout").click()
