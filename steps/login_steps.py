from selene.support.shared import browser
from page_objects.login_page import LoginPage
from utilities.logger import get_logger


class LoginSteps:

    def __init__(self):
        self.browser = browser

    logger = get_logger()

    org_id = LoginPage.org_id
    next_button = LoginPage.next_button
    username = LoginPage.username
    password = LoginPage.password
    login_button = LoginPage.login_button

    def login(self, url, org_id, username, password):
        self.browser.open_url(url)
        self.org_id.send_keys(org_id)
        self.next_button.click()
        LoginSteps.logger.info("Organization_id is sent")
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.login_button.click()
        LoginSteps.logger.info("Clicking on Login btn")
