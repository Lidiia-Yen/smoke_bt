import time

from selene.support.shared import browser
from page_objects.edit_page import EditPage
from steps.portfolio_view_steps import PortfolioViewSteps
from utilities.logger import get_logger


class EditSteps(PortfolioViewSteps):

    def __init__(self):
        super().__init__()
        self.browser = browser

    logger = get_logger()

    buy_btn = EditPage.buy_btn_first
    sell_btn = EditPage.sell_btn_second
    nominal_buy = EditPage.nv_input_first
    nominal_sell = EditPage.nv_input_second
    save_as_btn = EditPage.save_as_btn
    port_name_input = EditPage.port_name_input
    submit_btn = EditPage.continue_btn
    table_header = EditPage.table_header

    def buy_bond(self, amount):
        self.buy_btn.click()
        self.nominal_buy.send_keys(amount)
        self.nominal_buy.press_enter()
        time.sleep(5)  # wait until NV will be recalculated
        EditSteps.logger.info("Buy transaction is done")

    def sell_bond(self, amount):
        self.sell_btn.click()
        self.nominal_sell.send_keys(amount)
        self.nominal_sell.press_enter()
        time.sleep(5)  # wait until NV will be recalculated
        EditSteps.logger.info("Sell transaction is done")

    def save_portfolio_as(self, port_name):
        self.save_as_btn.click()
        self.port_name_input.clear()
        self.port_name_input.send_keys(port_name)
        self.submit_btn.click()
        EditSteps.logger.info("Save As child btn is pressed")
        time.sleep(5)  # wait loader
