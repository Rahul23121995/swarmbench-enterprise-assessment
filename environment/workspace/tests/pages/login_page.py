class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element("id", "username").send_keys(username)
        self.driver.find_element("id", "password").send_keys(password)
        # Broken locator: uses id 'submit' which is outdated
        submit_btn = self.driver.find_element("id", "submit")
        submit_btn.click()
