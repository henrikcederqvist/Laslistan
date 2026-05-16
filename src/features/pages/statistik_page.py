from src.features.pages.base_page import (
    BasePage,
    BASE_URL,
)


class StatistikPage(BasePage):

    def goto(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("networkidle")
        self.navigate_to_statistics()

    def _get_int(self, test_id: str) -> int:
        element = self.page.get_by_test_id(test_id)

        element.wait_for(state="visible")

        text = element.inner_text().strip()

        digits = "".join(
            ch for ch in text if ch.isdigit()
        )

        return int(digits) if digits else 0

    def get_total_books(self) -> int:
        return self._get_int("book-count")

    def get_favorite_count(self) -> int:
        return self._get_int("stars-count")