import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By


class Chrome:
    browser = None
    path = "source/webdriver/chromedriver"

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path=self.path)

    def goto(self, url):
        self.browser.get(url)

    def post(self, params):
        for param in params:
            self.browser.find_element(by=By.NAME, value=param).send_keys(params[param])

    def click(self, class_name):
        self.browser.find_element(by=By.CLASS_NAME, value=class_name).click()

    def get_buttons(self, class_name):
        return self.browser.find_elements(by=By.CLASS_NAME, value=class_name)
