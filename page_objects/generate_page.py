from selene.support.shared import browser
from selene import by


class GeneratePage:

    def __init__(self, driver):
        self.driver = driver

    port_name = browser.element(by.css('input[data-qa-id="port-name-min"]'))
    inv_amount = browser.element(by.css('input[data-qa-id="investment-amount-min"]'))
    constraints_tab = browser.element(by.css('div[data-qa-id="constraints-btn"]'))
    expand_all = browser.element(by.css('span[data-qa-id="header-expend-all"]'))
    upgrade_probability = browser.element(by.css('div[title="Upgrade Probability"]'))
    senior_seniority = browser.element(by.css('input[data-qa-id="senior-toggle"]'))
    subordinated_seniority = browser.element(by.css('input[data-qa-id="subordinated-toggle"]'))
    exempt_offering_144a = browser.element(by.css('input[data-qa-id="144a-toggle"]'))
    exempt_offering_regs = browser.element(by.css('input[data-qa-id="regs-toggle"]'))
    generate_button = browser.element(by.css('button[data-qa-id="generate-btn"]'))
    generate_toaster = browser.element(by.css('div[class="title ng-star-inserted"]'))
    close_toaster_btn = browser.element(by.css('div[class="close bondit-close"]'))
