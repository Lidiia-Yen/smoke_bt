import time

from page_objects.my_portfolios_page import MyPortfoliosPage
from selene.api import browser
from utilities.logger import get_logger


class MyPortfoliosSteps:

    def __init__(self):
        self.browser = browser

    logger = get_logger()

    page_name_label = MyPortfoliosPage.page_name_label
    port_names = MyPortfoliosPage.port_names

    def get_page_name_label(self):
        return self.page_name_label.text

    def open_portfolio_view_page(self):
        time.sleep(7)
        for portfolio in self.port_names:
            if "GGR" in portfolio.text:
                portfolio.click()
                break
        MyPortfoliosSteps.logger.info("Opening portfolio with name '...GGR'")
