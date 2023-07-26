from selenium.webdriver.common.by import By


class NoButtonRow:
    def __init__(self, detail):
        self.btn_no = (By.XPATH, f"//label[contains(text(), '{detail}')]/following-sibling::div/label[text()= 'No']")


class ChallengePage:

    def __init__(self, actions):
        self.actions = actions

    txt_first_name = (By.XPATH, "//input[contains(@id, 'SurveyControl_Question943')]")
    txt_last_name = (By.XPATH, "//input[contains(@id, 'SurveyControl_Question946')]")
    txt_email = (By.XPATH, "//input[contains(@id, 'SurveyControl_Question949')]")
    txt_address = (By.XPATH, "//input[contains(@id, 'SurveyControl_Question950')]")
    txt_city = (By.XPATH, "//input[contains(@id, 'SurveyControl_Question951')]")
    txt_zip_code = (By.XPATH, "//input[contains(@id, 'SurveyControl_Question952')]")
    btn_next = (By.ID, "SurveyControl_SurveySubmit")
    btn_submit = (By.ID, "SurveyControl_SurveySubmit")

    def enter_first_name(self, name):
        self.actions.clear_text_box(self.txt_first_name)
        self.actions.send_keys(name, self.txt_first_name)

    def enter_last_name(self, last_name):
        self.actions.clear_text_box(self.txt_last_name)
        self.actions.send_keys(last_name, self.txt_last_name)

    def enter_email(self, email):
        self.actions.clear_text_box(self.txt_email)
        self.actions.send_keys(email, self.txt_email)

    def enter_address(self, address):
        self.actions.clear_text_box(self.txt_address)
        self.actions.send_keys(address, self.txt_address)

    def enter_city(self, city):
        self.actions.clear_text_box(self.txt_city)
        self.actions.send_keys(city, self.txt_city)

    def enter_zip_code(self, zip_code):
        self.actions.clear_text_box(self.txt_zip_code)
        self.actions.send_keys(zip_code, self.txt_zip_code)

    def click_next(self):
        self.actions.click_element(self.btn_next)

    def fill_all_text_fields(self, name, last_name, email, address, city, zip_code):
        self.enter_first_name(name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_address(address)
        self.enter_city(city)
        self.enter_zip_code(zip_code)

    def click_no_button(self, detail):
        no_button_row = NoButtonRow(detail)
        self.actions.click_element(no_button_row.btn_no)

    def answer_no_to_all_questions(self):
        self.click_no_button("SNAP")
        self.click_no_button("TANF")
        self.click_no_button("Forces")
        self.click_no_button("disability")
        self.click_no_button("felony")
        self.click_no_button("unemployed")

    def click_submit_button(self):
        self.actions.click_element(self.btn_submit)
