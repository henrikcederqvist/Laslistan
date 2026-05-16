from src.features.pages.base_page import (
    BasePage,
    BASE_URL,
)


class KatalogPage(BasePage):

    def goto(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("networkidle")

    def get_books(self):
        return self.page.locator("div.book")

    def get_book_count(self) -> int:
        return self.get_books().count()

    def get_book_text(self, index: int) -> str:
        return self.get_books().nth(index).inner_text()

    def get_book_title(self, index: int) -> str:
        text = self.get_book_text(index)

        return (
            text.split(",")[0]
            .replace('"', "")
            .strip()
        )

    def get_book_author(self, index: int) -> str:
        text = self.get_book_text(index)
        parts = text.split(",")

        return parts[1].strip() if len(parts) > 1 else ""

    def _get_star(self, index: int):
        book = self.get_books().nth(index)
        return book.locator("div.star")

    def click_favorite_button(self, index: int):
        self._get_star(index).click()
        self.page.wait_for_timeout(100)

    def toggle_favorite(self, index: int):
        self.click_favorite_button(index)

    def is_favorite(self, index: int) -> bool:
        cls = self._get_star(index).get_attribute("class") or ""

        return (
            "active" in cls
            or "selected" in cls
        )