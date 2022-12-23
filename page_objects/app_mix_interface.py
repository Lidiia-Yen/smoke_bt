from selene.support.shared import browser
from selene import by


class BonditAppMenu:

    def __init__(self):
        self.browser = browser

    my_portfolios_tab = browser.element(by.css('a[data-qa-id="my-portfolios"]'))
    generate_tab = browser.element(by.css('a[data-qa-id="create-portfolio"]'))
    my_universes_tab = browser.element(by.css('a[data-qa-id="my-universes"]'))
    my_ips_tab = browser.element(by.css('a[data-qa-id="my-ips"]'))
    job_monitoring_menu = browser.element(by.css('div[class="job-monitoring-container"]'))
    alerts_tab = browser.element(by.css('a[data-qa-id="alerts"]'))
    search_tab = browser.element(by.css('a[data-qa-id="search"]'))
    user_menu = browser.element(by.css('a[data-qa-id="user-menu-btn"]'))


class SelectColumnsWindow:

    def __init__(self):
        self.browser = browser

    select_columns = browser.element(by.css('i[awesometooltip="Select Columns"]'))
    clear_all = browser.element(by.xpath('//span[text()="Clear all"]'))
    isin_column = browser.element(by.xpath('//div[text()=" ISIN"]'))
    apply = browser.element(by.xpath('//div[text()="APPLY"]'))
