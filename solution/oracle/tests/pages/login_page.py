class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element("id", "username").send_keys(username)
        self.driver.find_element("id", "password").send_keys(password)
        # Fixed locator: use name 'login' instead of id 'submit'
        submit_btn = self.driver.find_element("name", "login")
        submit_btn.click()
