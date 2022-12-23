import time
from datetime import datetime
from steps.app_mix_steps import PageSteps
from page_objects.generate_page import GeneratePage
from utilities.logger import get_logger
from selene.support.shared import browser


class GenerateSteps(PageSteps):

    def __init__(self):
        super().__init__()
        self.browser = browser

    logger = get_logger()

    port_name = GeneratePage.port_name
    inv_amount = GeneratePage.inv_amount
    constraints_tab = GeneratePage.constraints_tab
    expand_all = GeneratePage.expand_all
    upgrade_probability = GeneratePage.upgrade_probability
    senior_seniority = GeneratePage.senior_seniority
    subordinated_seniority = GeneratePage.subordinated_seniority
    exempt_offering_144a = GeneratePage.exempt_offering_144a
    exempt_offering_regs = GeneratePage.exempt_offering_regs
    generate_button = GeneratePage.generate_button
    generate_toaster = GeneratePage.generate_toaster
    close_toaster_btn = GeneratePage.close_toaster_btn

    def enter_port_name(self, name):
        return self.port_name.send_keys(f'{name} {datetime.now()}')

    def enter_amount(self, amount):
        return self.inv_amount.send_keys(amount)

    def navigate_constraints_tab(self):
        self.constraints_tab.click()
        GenerateSteps.logger.info("Constraints tab is opened")

    def expand_all_sections(self):
        self.expand_all.click()
        GenerateSteps.logger.info("All subsections are expanded")

    def click_upgrade_probability(self):
        self.upgrade_probability.click()
        GenerateSteps.logger.info("Clicking on upgrade_probability toggle")

    def click_senior(self):
        self.js_scroll_to_element(self.senior_seniority)
        self.senior_seniority.click()
        GenerateSteps.logger.info("Clicking on senior_seniority toggle")

    def click_subordinated(self):
        self.subordinated_seniority.click()
        GenerateSteps.logger.info("Clicking on subordinated_seniority toggle")

    def click_144a(self):
        self.exempt_offering_144a.click()
        GenerateSteps.logger.info("Clicking on exempt_offering_144a toggle")

    def click_regs(self):
        self.exempt_offering_regs.click()
        GenerateSteps.logger.info("Clicking on exempt_offering_regs toggle")

    def submit_generate_portfolio(self):
        self.generate_button.click()
        GenerateSteps.logger.info("Generate request is sent")

    def get_toaster_text(self):
        time.sleep(7)  # blue toaster appears and disappears, then green toaster appears
        text = self.generate_toaster.text
        self.close_toaster_btn.click()
        return text
