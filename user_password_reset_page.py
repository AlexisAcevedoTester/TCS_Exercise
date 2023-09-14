import logging
import time
from ..base.actions import Actions
from ..base.client_functions import ClientFunctions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UserPasswordResetPage(Actions):

    def __init__(self):
        Actions.__init__(self)
        self.logger = logging.getLogger()
        self.client_functions = ClientFunctions()

    # Locators for UI elements
    txt_new_password = (By.ID, "newPassword")
    txt_password_repeat = (By.ID, "passwordRepeat")
    btn_submit_password = (By.ID, "btn-submitpassword")
    lbl_passwords_does_not_match_error = (By.XPATH, "//p[text()='Passwords do not match!']")
    lbl_invalid_password_error = (By.XPATH, "//p[@class = 'error']")
    lnk_return_to_login = (By.CLASS_NAME, "return-link")

    # Actions perform on elements
    def enter_new_password(self, new_password, confirm_password):
        self.logger.step(f"Enter new password {new_password}")
        self.clear_text_box(self.txt_new_password)
        self.send_keys(new_password, self.txt_new_password)
        self.logger.step(f"Confirm new password {confirm_password}")
        self.clear_text_box(self.txt_password_repeat)
        self.send_keys(confirm_password, self.txt_password_repeat)
        time.sleep(3)
        self.send_keys(Keys.SPACE, self.txt_password_repeat)
        self.send_keys(Keys.BACKSPACE, self.txt_password_repeat)

    def click_submit_password_button(self):
        self.logger.step("Click submit password")
        self.click(self.btn_submit_password)

    def verify_passwords_do_not_match_message_is_present(self):
        self.logger.step("Checks passwords do not match")
        if self.is_element_present(self.lbl_passwords_does_not_match_error):
            self.logger.checkpoint("Error message appeared")
            return True
        return False

    def password_reset(self, new_password):
        self.enter_new_password(new_password, new_password)
        self.click_submit_password_button()

    def return_to_login_link(self):
        self.logger.step("Click return to login")
        self.client_functions.click_by_class_name(self.lnk_return_to_login)

    def verify_invalid_password_message_is_displayed(self):
        self.logger.step("Check password error message appears")
        errors_list = self.get_element_list(self.lbl_invalid_password_error)
        if len(errors_list) > 0:
            self.logger.checkpoint("Errors messages appeared")
            return True
        return False
