from selene.support.shared import browser
from selene import by


class PortfolioViewPage:

    def __init__(self):
        self.browser = browser

    portfolio_name = browser.element(by.css('div[class="portfolio_name ng-star-inserted"]'))
    st_icon = browser.element(by.css('span[class="bondit-generate ng-star-inserted"]'))
    apply_filters_btn = browser.element(by.css('button[data-qa-id="apply-btn"]'))
    submit_st_btn = browser.element(by.css('button[data-qa-id="switch-btn"]'))
    edit_btn = browser.element(by.css('button[data-qa-id="sec-list-edit-button-btn"]'))
    switch_trade_idea = browser.element(by.css('div[row-index="0"]'))
    transaction_list_btn = browser.element(by.css('span[data-qa-id="transaction-list-btn"]'))
    transaction_table = browser.element(by.css('div[class="ag-root-wrapper ag-layout-normal ag-ltr"]'))
    transaction_close_btn = browser.element(by.css('div[data-qa-id="close-x"]'))
