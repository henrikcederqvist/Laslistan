"""
pages/mina_bocker_page.py
Page Object för vyn Mina böcker.
"""

from pages.base_page import BasePage, BASE_URL


class MinaBockerPage(BasePage):

    def goto(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("networkidle")
        self.navigate_to_my_books()

    # ── Favoritlista ────────────────────────────────────────

    def get_favorite_books(self):
        return self.page.get_by_test_id("favorite-item").all()

    def get_favorite_count(self) -> int:
        return len(self.get_favorite_books())

    def get_favorite_title(self, index: int) -> str:
        books = self.get_favorite_books()
        return books[index].get_by_test_id("book-title").inner_text()

    def remove_favorite(self, index: int):
        """Klicka på ta-bort-knappen för favorit med givet index."""
        books = self.get_favorite_books()
        books[index].get_by_test_id("remove-favorite").click()

    # ── Tom lista ───────────────────────────────────────────

    def is_empty_message_visible(self) -> bool:
        """Returnera True om ett 'tom lista'-meddelande är synligt."""
        msg = self.page.get_by_test_id("empty-favorites")
        if msg.count() > 0:
            return msg.is_visible()
        # Fallback: leta efter text
        return self.page.get_by_text("inga", exact=False).count() > 0
