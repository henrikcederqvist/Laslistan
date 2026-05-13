"""
pages/katalog_page.py
Page Object för vyn Katalog.
"""

from pages.base_page import BasePage, BASE_URL


class KatalogPage(BasePage):

    def goto(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("networkidle")

    def get_books(self):
        """Returnera en lista med alla bok-element."""
        return self.page.locator("div.book").all()

    def get_book_count(self) -> int:
        return len(self.get_books())

    def get_book_title(self, index: int) -> str:
        books = self.get_books()
        text = books[index].inner_text()
        return text.split(",")[0].strip().strip('"')

    def get_book_author(self, index: int) -> str:
        books = self.get_books()
        text = books[index].inner_text()
        parts = text.split(",")
        return parts[1].strip() if len(parts) > 1 else ""

    def get_star_testid(self, index: int) -> str:
        books = self.get_books()
        star = books[index].locator("div.star")
        return star.get_attribute("data-testid")

    def click_favorite_button(self, index: int):
        books = self.get_books()
        books[index].locator("div.star").click()

    def is_favorite(self, index: int) -> bool:
        books = self.get_books()
        star = books[index].locator("div.star")
        css_class = star.get_attribute("class") or ""
        return "active" in css_class or "selected" in css_class

    def toggle_favorite(self, index: int):
        self.click_favorite_button(index)

    def debug_page(self):
        print(self.page.url)
        print(self.page.content())