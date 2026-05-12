"""
pages/base_page.py
Basklass för alla page objects.
"""

BASE_URL = "https://tap-ht25-testverktyg.github.io/exam/"


class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self):
        raise NotImplementedError

    def navigate_to_catalog(self):
        self.page.get_by_test_id("catalog").click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_add_book(self):
        self.page.get_by_test_id("add-book").click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_my_books(self):
        self.page.get_by_test_id("favorites").click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_statistics(self):
        self.page.get_by_test_id("statistics").click()
        self.page.wait_for_load_state("networkidle")

    def click_nav_button(self, testid: str):
        self.page.get_by_test_id(testid).click()
        self.page.wait_for_load_state("networkidle")

    def get_page_title(self) -> str:
        heading = self.page.locator("h1, h2").first
        return heading.inner_text()