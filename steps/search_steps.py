import time

from selene.support.shared import browser
from page_objects.search_page import SearchPage
from steps.app_mix_steps import PageSteps
from utilities.logger import get_logger


class SearchSteps(PageSteps):

    def __init__(self):
        super().__init__()
        self.browser = browser

    logger = get_logger()

    side_dropdown = SearchPage.side_dropdown
    ask_side = SearchPage.ask_side
    search_in_section = SearchPage.search_in_section
    close_section = SearchPage.close_section
    clear_all = SearchPage.clear_all
    asset_type_section = SearchPage.asset_type_section
    corporate_asset_type = SearchPage.corporate_asset_type
    currency_section = SearchPage.currency_section
    usd_currency = SearchPage.usd_currency
    issuer_section = SearchPage.issuer_section
    apple_issuer = SearchPage.apple_issuer
    country_section = SearchPage.country_section
    usa_country = SearchPage.usa_country
    ytw_inputs = SearchPage.ytw_inputs
    search_btn = SearchPage.search_btn
    search_table_body = SearchPage.search_table_body
    results_apple_rows = SearchPage.results_apple_rows
    action_menu = SearchPage.action_menu
    bonds_comparison = SearchPage.bonds_comparison
    comparison_table_label = SearchPage.comparison_table_label
    comparison_table_body = SearchPage.comparison_table_body
    close_comparison_icon = SearchPage.close_comparison_icon

    def select_ask(self):
        time.sleep(5)
        self.side_dropdown.click()
        self.ask_side.click()
        SearchSteps.logger.info("ASK side is selected")

    def select_corporate_asset_type(self):
        self.asset_type_section.click()
        self.clear_all.click()
        self.corporate_asset_type.click()
        self.close_section.click()
        SearchSteps.logger.info("Corporate asset type is selected")

    def select_usd_currency(self):
        self.currency_section.click()
        self.clear_all.click()
        self.usd_currency.click()
        self.close_section.click()
        SearchSteps.logger.info("USD currency is selected")

    def select_issuer(self, issuer_name):
        self.issuer_section.click()
        self.search_in_section.send_keys(issuer_name)
        self.apple_issuer.click()
        self.close_section.click()
        SearchSteps.logger.info("Issuer=Apple is selected")

    def select_country(self, country):
        self.country_section.click()
        self.clear_all.click()
        self.search_in_section.send_keys(country)
        self.usa_country.click()
        self.close_section.click()
        SearchSteps.logger.info("USA country is selected")

    def select_ytw(self):
        time.sleep(3)
        first_input = self.ytw_inputs[0]
        self.js_scroll_to_element(first_input)
        first_input.clear()
        first_input.send_keys('2')
        SearchSteps.logger.info("Set ytw min=2")

    def do_search(self):
        self.search_btn.click()
        SearchSteps.logger.info("Search button is pressed")

    def select_two_rows(self):
        rows = self.results_apple_rows
        for row in rows[:3]:
            row.click()
        SearchSteps.logger.info("Search result rows are selected")

    def go_to_compare_bonds(self):
        self.action_menu.click()
        self.bonds_comparison.click()
        SearchSteps.logger.info("Compare bonds table is opened")

    def get_table_name(self):
        text = self.comparison_table_label.text
        time.sleep(3)
        self.close_comparison_icon.click()
        return text
