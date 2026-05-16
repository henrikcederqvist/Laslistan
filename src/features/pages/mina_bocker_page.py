from src.features.pages.base_page import (
    BasePage,
    BASE_URL,
)


class MinaBockerPage(BasePage):

    def goto(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("networkidle")
        self.navigate_to_my_books()

    def get_favorite_books(self):
        return self.page.locator(
            '[data-testid="book-list"] .book'
        )

    def get_favorite_count(self) -> int:
        return self.get_favorite_books().count()

    def get_favorite_title(self, index: int) -> str:
        text = (
            self.get_favorite_books()
            .nth(index)
            .inner_text()
        )

        return (
            text.split(",")[0]
            .replace('"', "")
            .strip()
        )

    def is_empty(self) -> bool:
        return self.get_favorite_count() == 0

    def is_empty_message_visible(self) -> bool:
        body = self.page.inner_text("body").lower()

        return (
            self.is_empty()
            or "inga" in body
            or "tom" in body
        )