from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Actions:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def go_to_site(self, site_link):
        try:
            self.driver.get(site_link)
            self.driver.maximize_window()
        except Exception:
            print(f"Error going to site {site_link}")

    def wait_for_element(self, element_to_wait_for):
        try:
            wait = WebDriverWait(self.driver, timeout=15)
            wait.until(EC.element_to_be_clickable(element_to_wait_for))
        except Exception:
            print(f"Element {element_to_wait_for[1]} not found")

    def get_element(self, element_to_find):
        try:
            self.wait_for_element(element_to_find)
            return self.driver.find_element(*element_to_find)
        except Exception:
            print(f"Error finding element {element_to_find[1]}")

    def click_element(self, element_to_click):
        try:
            element = self.get_element(element_to_click)
            element.click()
        except Exception:
            print(f"Element not clicked {element_to_click[1]}")

    def is_element_displayed(self, element_to_find):
        try:
            element = self.get_element(element_to_find)
            if element.is_displayed():
                return True
            else:
                return False
        except Exception:
            print(f"Error checking if element is displayed: {element_to_find[1]}")

    def send_keys(self, data, element_to_send_keys_to):
        try:
            element = self.get_element(element_to_send_keys_to)
            element.send_keys(data)
        except Exception:
            print(f"Error sending keys to {element_to_send_keys_to[1]}")

    def clear_text_box(self, element_to_clear):
        try:
            element = self.get_element(element_to_clear)
            element.clear()
        except Exception:
            print(f"Element not cleared {element_to_clear[1]}")

    def get_current_url(self):
        try:
            return self.driver.current_url
        except Exception:
            print("Error while getting URL")

    def close_browser(self):
        try:
            self.driver.close()
        except Exception:
            print("Exception Occurred when closing browser")
