from src.features.pages.base_page import BasePage, BASE_URL


class StatistikPage(BasePage):

    def goto(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("networkidle")
        self.navigate_to_statistics()

    def _get_int(self, testid):
        el = self.page.get_by_test_id(testid)
        el.wait_for(state="visible")
        text = el.inner_text().strip()
        digits = "".join(ch for ch in text if ch.isdigit())
        return int(digits) if digits else 0

    def get_total_books(self):
        return self._get_int("stat-total-books")

    def get_favorite_count(self):
        return self._get_int("stat-favorites")