import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Base:
    # Define the project root and driver path
    PROJECT_ROOT = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..")
    )
    DRIVER_PATH = os.path.join(PROJECT_ROOT, "chromedriver.exe")
    # Define the URL and credentials for the website
    URL = "https://thinking-tester-contact-list.herokuapp.com/"
    CREDENTIALS = {"email": "d1@example.com", "pass": "1234567"}

    def __init__(self, driver=None):
        """
        Initialize the WebDriverWait instance.
        If no driver is provided, a new Chrome webdriver instance is created with the specified options.
        """
        if driver is None:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-notifications")
            prefs = {"autofill.profile_enabled": False}
            chrome_options.add_experimental_option("prefs", prefs)
            self.driver = webdriver.Chrome(
                service=Service(self.DRIVER_PATH), options=chrome_options
            )
        else:
            self.driver = driver
        self.wait = WebDriverWait(
            self.driver,
            10,
            poll_frequency=1,
            ignored_exceptions=NoSuchElementException,
        )
        self.EC = EC

    def close(self):
        """Close the current browser session."""
        self.driver.close()

    def get_current_url(self):
        """Return the current URL."""
        self.URL = self.driver.current_url
        return self.current_url

    def get_title(self):
        self.wait.until(self.EC.title_is(self.driver.title))
        return self.driver.title

    def get(self, url=URL):
        """Navigate to the specified URL and update the title."""
        self.driver.get(url)
        self.current_url = self.driver.current_url
        self.title = self.driver.title  # update the title after navigating

    def find_element(self, by, value):
        """Find an element on the webpage using the specified locator strategy and locator value."""
        return self.driver.find_element(by, value)

    def execute(self, script, *args):
        """Execute the specified JavaScript script."""
        return self.driver.execute_script(script, *args)

    @property
    def switch_to(self):
        """Switch to a different window or frame."""
        return self.driver.switch_to

    def get_error_message(self):
        """This method returns the error message displayed on the webpage."""
        error_message_element = self.wait.until(
            self.EC.visibility_of_element_located((By.ID, "error"))
        )
        return error_message_element.text

    def cancel_button_press(self):
        return_button = self.driver.find_element(By.ID, "cancel")
        return_button.click()
