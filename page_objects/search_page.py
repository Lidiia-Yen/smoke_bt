from selene.support.shared import browser
from selene import by


class SearchPage:
    def __init__(self):
        self.browser = browser

    side_dropdown = browser.element(by.css('div[data-qa-id="side-drdn"]'))
    ask_side = browser.element(by.css('div[id="ask"]'))
    search_in_section = browser.element(by.css('input[placeholder="Search..."]'))
    close_section = browser.element(by.css('div[class="openConstraintText"]'))
    clear_all = browser.element(by.xpath('//span[text()="Clear all"]'))
    asset_type_section = browser.element(by.xpath('//div[text()="Asset Type "]'))
    corporate_asset_type = browser.element(by.xpath('//li[text()="Corporate"]'))
    currency_section = browser.element(by.xpath('//div[text()="Currency "]'))
    usd_currency = browser.element(by.xpath('//li[text()="USD"]'))
    issuer_section = browser.element(by.xpath('//div[text()="Issuer Name "]'))
    apple_issuer = browser.element(by.xpath('//li[text()="Apple Inc."]'))
    country_section = browser.element(by.xpath('//div[text()="Issue Country of Risk "]'))
    usa_country = browser.element(by.xpath('//li[text()="United States"]'))
    ytw_inputs = browser.all(by.css('input[id="ytw__ask_"]'))
    search_btn = browser.element(by.css('button[data-qa-id="search-btn"]'))
    results_apple_rows = browser.elements(by.xpath('//span[text()="Apple Inc."]'))
    action_menu = browser.element(by.css('div[class="export bondit-asstes_actions"]'))
    bonds_comparison = browser.element(by.xpath('//span[text()="Comparison Table"]'))
    comparison_table_label = browser.element(by.xpath('//div[text()= " Bonds Comparison Table"]'))
    comparison_table_body = browser.element(by.css('div[class="search-table-comparison fixTop"]'))
    close_comparison_icon = browser.element(by.css('div[data-qa-id="close-x"]'))
    search_table_body = browser.element(by.css('div[class="ag-center-cols-container"]'))


