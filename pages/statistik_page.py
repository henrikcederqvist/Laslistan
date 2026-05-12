"""
pages/statistik_page.py
Page Object för vyn Statistik.
"""

from pages.base_page import BasePage, BASE_URL


class StatistikPage(BasePage):

    def goto(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("networkidle")
        self.navigate_to_statistics()

    # ── Statistikvärden ─────────────────────────────────────

    def get_total_books(self) -> int:
        """Returnera det visade totala antalet böcker."""
        el = self.page.get_by_test_id("stat-total-books")
        return int(el.inner_text().strip())

    def get_favorite_count(self) -> int:
        """Returnera det visade antalet favoriter."""
        el = self.page.get_by_test_id("stat-favorites")
        return int(el.inner_text().strip())
