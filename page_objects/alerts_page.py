from selene.support.shared import browser
from selene import by


class AlertsPage:
    def __init__(self):
        self.browser = browser

    alert_dates = browser.elements(by.css('span[aria-colindex="11"]'))
    table_body = browser.element(by.css(
        'div[class="ag-body-viewport ag-layout-normal ag-row-no-animation ag-selectable"]'))
