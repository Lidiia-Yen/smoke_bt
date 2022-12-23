from selene.support.shared import browser
from selene import command
from page_objects.app_mix_interface import SelectColumnsWindow, BonditAppMenu
from utilities.logger import get_logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageSteps:

    def __init__(self):
        self.browser = browser

    def js_scroll_to_element(self, element):
        return element.perform(command.js.scroll_into_view)

    def wait_on_element(self, element):
        WebDriverWait(self.browser, 10).until(EC.visibility_of(element))  # element is (By.LINK_TEXT, text)

    # def wait_to_disappear(self, element):
    #     WebDriverWait(self.browser, 10).until(EC.invisibility_of_element(element))


class BonditAppMenuSteps:

    def __init__(self):
        self.browser = browser

    logger = get_logger()

    my_portfolios_tab = BonditAppMenu.my_portfolios_tab
    generate_tab = BonditAppMenu.generate_tab
    my_universes_tab = BonditAppMenu.my_universes_tab
    my_ips_tab = BonditAppMenu.my_ips_tab
    job_monitoring_menu = BonditAppMenu.job_monitoring_menu
    alerts_tab = BonditAppMenu.alerts_tab
    search_tab = BonditAppMenu.search_tab
    user_menu = BonditAppMenu.user_menu

    def open_my_portfolios_page(self):
        return self.my_portfolios_tab.click()

    def open_generate_page(self):
        self.generate_tab.click()
        BonditAppMenuSteps.logger.info("Click on Generate page")

    def open_my_universes_page(self):
        self.my_universes_tab.click()
        BonditAppMenuSteps.logger.info("Click on My_Universes page")

    def open_my_ips_page(self):
        self.my_ips_tab.click()
        BonditAppMenuSteps.logger.info("Click on My_IPS page")

    def open_job_monitoring_menu(self):
        self.job_monitoring_menu.click()
        BonditAppMenuSteps.logger.info("Click on Job_Monitor icon")

    def open_alerts_page(self):
        self.alerts_tab.click()
        BonditAppMenuSteps.logger.info("Click on Alerts page")

    def open_search_page(self):
        self.search_tab.click()
        BonditAppMenuSteps.logger.info("Click on Search page")

    def open_user_menu(self):
        self.user_menu.click()
        BonditAppMenuSteps.logger.info("Click on User_Menu page")


class SelectColumnsSteps:

    def __init__(self):
        self.browser = browser

    logger = get_logger()

    select_columns = SelectColumnsWindow.select_columns
    clear_all = SelectColumnsWindow.clear_all
    isin_column = SelectColumnsWindow.isin_column
    apply = SelectColumnsWindow.apply

    def unselect_all_columns(self):
        self.select_columns.click()
        self.clear_all.click()
        SelectColumnsSteps.logger.info("Click on Clear all btn in Select Columns")

    def select_isin_column(self):
        self.isin_column.click()
        self.apply.click()
        SelectColumnsSteps.logger.info("Click on Apply btn in Select Columns")
