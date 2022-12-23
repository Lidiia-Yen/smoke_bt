from selene.support.shared import browser
from selene import by


class LoginPage:

    def __init__(self):
        self.browser = browser

    org_id = browser.element(by.css('input#client_id'))
    next_button = browser.element(by.css('input[value="Next"]'))
    username = browser.element(by.css('input#user_name'))
    password = browser.element(by.css('input#user_password'))
    login_button = browser.element(by.css('input[type="submit"]'))

