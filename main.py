import unittest
from selenium_actions import Actions
from automation_challenge_page import ChallengePage
from experian_page import ExperianPage


class TCSTests(unittest.TestCase):
    def setUp(self):
        self.actions = Actions()
        self.challenge_page = ChallengePage(self.actions)
        self.experian_page = ExperianPage(self.actions)
        self.actions.go_to_site("https://surveyrc.taxcreditco.com/automation-challenge")

    def test_exercise(self):
        self.challenge_page.fill_all_text_fields("Joe", "Sample", "mail@test.com", "Main st", "LA", "91210")
        print("Fill all text fields")
        self.challenge_page.click_next()
        print("Clck next button")
        self.challenge_page.answer_no_to_all_questions()
        print("Answer no to all questions")
        self.challenge_page.click_next()
        print("Click next button")
        self.challenge_page.click_submit_button()
        print("Click Submit button")
        self.assertTrue(self.experian_page.is_banner_present(), "Banner is not present")
        print("Page loaded correctly")
        self.assertIn("https://www.experian.com/employer-services", self.experian_page.get_url(), "URL is incorrect")
        print("URL is correct")

    def tearDown(self):
        self.actions.close_browser()


if __name__ == '__main__':
    unittest.main()
