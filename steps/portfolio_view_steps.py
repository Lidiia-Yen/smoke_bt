import time

from selene.support.shared import browser
from page_objects.portfolio_view_page import PortfolioViewPage
from steps.app_mix_steps import SelectColumnsSteps, BonditAppMenuSteps
from steps.my_portfolios_steps import MyPortfoliosSteps
from steps.search_steps import SearchSteps
from utilities.logger import get_logger


class PortfolioViewSteps(MyPortfoliosSteps, SelectColumnsSteps, BonditAppMenuSteps, SearchSteps):

    def __init__(self):
        super().__init__()
        self.browser = browser

    logger = get_logger()

    portfolio_name = PortfolioViewPage.portfolio_name
    switch_trade_icon = PortfolioViewPage.st_icon
    switch_trade_idea = PortfolioViewPage.switch_trade_idea
    apply_filters_btn = PortfolioViewPage.apply_filters_btn
    submit_st_btn = PortfolioViewPage.submit_st_btn
    edit_btn = PortfolioViewPage.edit_btn
    transaction_list_btn = PortfolioViewPage.transaction_list_btn
    transaction_table = PortfolioViewPage.transaction_table
    transaction_close_btn = PortfolioViewPage.transaction_close_btn
    issuer_section = SearchSteps.issuer_section
    search_in_section = SearchSteps.search_in_section
    apple_issuer = SearchSteps.apple_issuer

    def open_portfolio_design_page(self):
        self.js_scroll_to_element(self.edit_btn)
        self.edit_btn.click()

    def open_switch_trade(self):
        self.js_scroll_to_element(self.switch_trade_icon)
        return self.switch_trade_icon.click()

    def apply_filters(self):
        self.apply_filters_btn.click()
        PortfolioViewSteps.logger.info("Apply filters button is pressed")

    def submit_switch_trade(self):
        time.sleep(5)
        self.submit_st_btn.click()
        PortfolioViewSteps.logger.info("Switch Trade button is pressed")

    def get_portfolio_name(self):
        return self.portfolio_name.text

    def navigate_transaction_list(self):
        self.transaction_list_btn.click()
        self.wait_on_element(self.transaction_table)
        self.transaction_close_btn.click()
