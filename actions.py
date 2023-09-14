import logging
import datetime
import time
import os
from ..base.shared_settings import SharedSettings
from ..base.configurations import Configurations
from ..utilities.util import Util
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Actions:

    actions_objects = []

    def __init__(self):
        self.web_server = SharedSettings.get_app_settings().web_server
        self.util = Util()
        self.logger = logging.getLogger()
        self.driver = SharedSettings().get_driver()
        Actions.actions_objects.append(self)

    def wait_for_element(self, element_to_wait_for, timeout=15):
        try:
            wait = WebDriverWait(self.driver, timeout=timeout)
            wait.until(EC.element_to_be_clickable(element_to_wait_for))
        except:
            self.logger.debug(f"Element {element_to_wait_for[1]} not found")

    def wait_for_invisibility(self, element, timeout=10):
        try:
            self.driver.implicitly_wait(0)
            wait = WebDriverWait(self.driver, timeout=timeout)
            is_element_invisible = wait.until(EC.invisibility_of_element(element))
            return is_element_invisible
        except:
            self.logger.error(f"Error expecting invisibility of {element[1]}")
            self.take_screen_shot()
            raise ElementNotVisibleError(f"Element present {element[1]}")

    def get_element(self, element_to_find):
        try:
            self.wait_for_element(element_to_find)
            return self.driver.find_element(*element_to_find)
        except:
            self.logger.debug(f"Error finding element {element_to_find[1]}")

    def get_element_list(self, elements_to_find):
        try:
            self.wait_for_element(elements_to_find)
            return self.driver.find_elements(*elements_to_find)
        except:
            self.logger.debug(f"Elements {elements_to_find[1]} not found")

    def click(self, element_to_click):
        try:
            element = self.get_element(element_to_click)
            element.click()
        except:
            self.logger.error(f"Element not clicked {element_to_click[1]}")
            self.take_screen_shot()
            raise ElementNotVisibleError(f"Element not clicked {element_to_click[1]}")

    def is_element_present(self, element_to_find):
        try:
            element = self.get_element(element_to_find)
            if element is not None:
                return True
            else:
                return False
        except:
            self.logger.debug(f"Element not present {element_to_find[1]}")

    def is_element_displayed(self, element_to_find):
        try:
            element = self.get_element(element_to_find)
            if element.is_displayed():
                return True
            else:
                return False
        except:
            self.logger.error(f"Error finding element {element_to_find[1]}")

    def is_element_enabled(self, element_to_find):
        try:
            element = self.get_element(element_to_find)
            if element.is_enabled():
                return True
            else:
                return False
        except:
            self.logger.debug(f"Error finding element {element_to_find[1]}")

    def send_keys(self, data, element_to_send_keys_to):
        try:
            element = self.get_element(element_to_send_keys_to)
            element.send_keys(data)
        except:
            self.logger.error(f"Element not found {element_to_send_keys_to[1]}")
            self.take_screen_shot()
            raise ElementNotVisibleError(f"Cannot send key to {element_to_send_keys_to[1]}")

    def clear_text_box(self, element_to_clear):
        try:
            element = self.get_element(element_to_clear)
            element.clear()
        except:
            self.logger.error(f"Element not cleared {element_to_clear[1]}")
            self.take_screen_shot()
            raise ElementNotVisibleError(f"Cannot clear {element_to_clear[1]}")

    def get_text(self, element_to_get_text_from):
        try:
            element = self.get_element(element_to_get_text_from)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
                if len(text) == 0:
                    text = element.get_attribute("value")
            return text.strip()
        except:
            self.logger.error(f"Element not found {element_to_get_text_from[1]}")
            self.take_screen_shot()
            raise ElementNotVisibleError(f"Cannot get text from {element_to_get_text_from[1]}")

    def take_screen_shot(self, current_test=""):
        """
        Takes screenshot of the current open web page
        """
        st = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %Hhh-%Mmm-%Sss")
        if current_test == "":
            current_test = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        file_name = current_test + " - " + st + ".png"
        screenshot_directory = "..\\screenshots\\"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)
        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
        except:
            self.logger.debug("Exception Occurred when taking screenshot")

    @classmethod
    def open_browser(cls):
        """ This method will update other Action's references with the latest WebDriver Driver instance.
        :return:
        """
        driver = Configurations().create_web_driver_instance(SharedSettings().get_app_settings().browser)
        for obj in cls.actions_objects:
            obj.driver = driver
        driver.get(SharedSettings().get_app_settings().web_server)
        driver.maximize_window()

    def close_browser(self):
        self.driver.quit()


class ElementNotVisibleError(Exception):
    # Constructor or Initializer
    def __init__(self, message):
        self.message = message

    # __str__ is to print() the value
    def __str__(self):
        return repr(self.message)


class LoginError(Exception):
    # Constructor or Initializer
    def __init__(self, message):
        self.message = message

    # __str__ is to print() the value
    def __str__(self):
        return repr(self.message)