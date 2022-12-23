from selene.support.shared import browser
from selene import by


class EditPage:

    def __init__(self):
        self.browser = browser

    buy_btn_first = browser.all(by.css('span[class="buyButton ng-star-inserted"]'))[0]
    sell_btn_second = browser.all(by.css('span[class="sellButton ng-star-inserted"]'))[1]
    nv_input_first = browser.all(by.css('input[type="text"]'))[0]
    nv_input_second = browser.all(by.css('input[type="text"]'))[1]
    save_as_btn = browser.element(by.css('button[data-qa-id="save-as-btn"]'))
    port_name_input = browser.element(by.css('input[data-qa-id="save-as-name"]'))
    continue_btn = browser.element(by.css('div[data-qa-id="continue-btn"]'))
    table_header = browser.element(by.css('div[class="ag-header ag-pivot-off"]'))
    # loader = browser.element(by.css('img[id="loader-img"]'))
