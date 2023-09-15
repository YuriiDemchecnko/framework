import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Base:
    PROJECT_ROOT = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..")
    )
    DRIVER_PATH = os.path.join(PROJECT_ROOT, "chromedriver.exe")

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(self.DRIVER_PATH))

    def close(self):
        self.driver.close()
