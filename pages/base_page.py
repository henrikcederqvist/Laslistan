"""
pages/base_page.py
Basklass för alla page objects. Innehåller gemensam navigering.
"""

BASE_URL = "https://tap-ht25-testverktyg.github.io/exam/"


class BasePage:
    def __init__(self, page):
        self.page = page

    # ── Navigering ──────────────────────────────────────────

    def goto(self):
        """Navigera till denna sidas URL. Implementeras i subklass."""
        raise NotImplementedError

    def navigate_to_catalog(self):
        self.page.get_by_role("link", name="Katalog").click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_add_book(self):
        self.page.get_by_role("link", name="Lägg till bok").click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_my_books(self):
        self.page.get_by_role("link", name="Mina böcker").click()
        self.page.wait_for_load_state("networkidle")

    def navigate_to_statistics(self):
        self.page.get_by_role("link", name="Statistik").click()
        self.page.wait_for_load_state("networkidle")

    def click_nav_link(self, name: str):
        self.page.get_by_role("link", name=name).click()
        self.page.wait_for_load_state("networkidle")

    # ── Hjälpmetoder ────────────────────────────────────────

    def get_page_title(self) -> str:
        """Returnera synlig sidrubrik (h1 eller h2)."""
        heading = self.page.locator("h1, h2").first
        return heading.inner_text()
