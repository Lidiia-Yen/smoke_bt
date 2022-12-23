from selene.support.shared import browser
from selene import by


class MyPortfoliosPage:

    def __init__(self):
        self.browser = browser

    page_name_label = browser.element(by.css('div[class="page-title"]'))
    port_names = browser.elements(by.xpath('//div[@role="row"]/div[4]/div/span/app-portfolio-name/a'))

