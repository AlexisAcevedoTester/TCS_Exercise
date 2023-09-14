import time
from ..base.shared_settings import SharedSettings
from ..base.actions import *


class ClientFunctions:

    def click_by_id(self, element):
        try:
            time.sleep(3)
            driver = SharedSettings().get_driver()
            script = f"document.getElementById('{element[1]}').click()"
            driver.execute_script(script)
        except:
            Actions().take_screen_shot()
            raise ElementNotVisibleError(f"Element {element[1]} not clicked")

    def click_by_class_name(self, element):
        try:
            time.sleep(3)
            driver = SharedSettings().get_driver()
            script = f"document.getElementsByClassName('{element[1]}')[0].firstChild.click()"
            driver.execute_script(script)
        except:
            Actions().take_screen_shot()
            raise ElementNotVisibleError(f"Element {element[1]} not clicked")
