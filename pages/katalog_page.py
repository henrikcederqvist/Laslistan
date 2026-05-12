"""
pages/katalog_page.py
Page Object för vyn Katalog.
"""

from pages.base_page import BasePage, BASE_URL


class KatalogPage(BasePage):

    def goto(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("networkidle")

    # ── Böcker ──────────────────────────────────────────────

    def get_books(self):
        """Returnera en lista med alla bok-element."""
        return self.page.get_by_test_id("book-item").all()

    def get_book_count(self) -> int:
        return len(self.get_books())

    def get_book_title(self, index: int) -> str:
        books = self.get_books()
        return books[index].get_by_test_id("book-title").inner_text()

    def get_book_author(self, index: int) -> str:
        books = self.get_books()
        return books[index].get_by_test_id("book-author").inner_text()

    # ── Favoriter ───────────────────────────────────────────

    def click_favorite_button(self, index: int):
        """Klicka på favoritknappen för bok med givet index (0-baserat)."""
        books = self.get_books()
        books[index].get_by_test_id("favorite-button").click()

    def is_favorite(self, index: int) -> bool:
        """Returnera True om boken med givet index är favorit."""
        books = self.get_books()
        btn = books[index].get_by_test_id("favorite-button")
        aria = btn.get_attribute("aria-pressed")
        if aria is not None:
            return aria == "true"
        css_class = btn.get_attribute("class") or ""
        return "active" in css_class or "favorite" in css_class

    def toggle_favorite(self, index: int):
        self.click_favorite_button(index)