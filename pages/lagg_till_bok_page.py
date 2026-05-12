"""
pages/lagg_till_bok_page.py
Page Object för vyn Lägg till bok.
"""

from pages.base_page import BasePage, BASE_URL


class LaggTillBokPage(BasePage):

    def goto(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("networkidle")
        self.navigate_to_add_book()

    # ── Formulär ────────────────────────────────────────────

    def fill_title(self, title: str):
        self.page.get_by_test_id("input-title").fill(title)

    def fill_author(self, author: str):
        self.page.get_by_test_id("input-author").fill(author)

    def submit_form(self):
        self.page.get_by_test_id("submit-book").click()

    def fill_and_submit(self, title: str, author: str):
        self.fill_title(title)
        self.fill_author(author)
        self.submit_form()

    def get_title_value(self) -> str:
        return self.page.get_by_test_id("input-title").input_value()

    def get_author_value(self) -> str:
        return self.page.get_by_test_id("input-author").input_value()

    def is_form_empty(self) -> bool:
        return self.get_title_value() == "" and self.get_author_value() == ""
