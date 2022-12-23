from selene.support.shared import browser
from page_objects.alerts_page import AlertsPage
from steps.app_mix_steps import PageSteps
from utilities.logger import get_logger
from datetime import datetime, timedelta


class AlertsSteps(PageSteps):

    def __init__(self):
        super().__init__()
        self.browser = browser

    logger = get_logger()

    alert_dates = AlertsPage.alert_dates
    table_body = AlertsPage.table_body

    def take_last_alert_date(self):
        last_alert_date = self.alert_dates[1].text
        AlertsSteps.logger.info("Last alert date is taken")
        return last_alert_date

    def select_three_past_days(self):
        now = datetime.today()
        two_days_ago = datetime.today() - timedelta(2)
        alert_dates = [date for date in (two_days_ago, now)]
        return alert_dates
