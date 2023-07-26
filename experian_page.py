from selenium.webdriver.common.by import By


class ExperianPage:

    def __init__(self, actions):
        self.actions = actions

    main_banner = (By.ID, "mainTop")

    def is_banner_present(self):
        return self.actions.is_element_displayed(self.main_banner)

    def get_url(self):
        return self.actions.get_current_url()
