import logging
from ..base.actions import Actions
from selenium.webdriver.common.by import By


class LogsPage(Actions):

    def __init__(self):
        Actions.__init__(self)
        self.logger = logging.getLogger()

    btn_reset = (By.ID, "server-logs-date-range-reset")

    def has_view_logs_access(self):
        has_view_logs_access = self.is_element_displayed(self.btn_reset)
        if has_view_logs_access:
            self.logger.checkpoint("Admin has logs access")
            return True
        else:
            self.logger.error("Admin doesn't have logs access")
            return False
