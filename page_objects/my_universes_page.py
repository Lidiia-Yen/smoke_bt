from selene.support.shared import browser
from selene import by


class EditPage:

    def __init__(self):
        self.browser = browser

    # buy_btn_first = browser.all(by.css('span[class="buyButton ng-star-inserted"]'))[0]
    # continue_btn = browser.element(by.css('div[data-qa-id="continue-btn"]'))