from src.features.pages.base_page import (
    BasePage,
    BASE_URL,
)


class StatistikPage(BasePage):

    def goto(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("networkidle")
        self.navigate_to_statistics()

    def _get_int_from_test_id(self, test_id: str) -> int | None:
        element = self.page.get_by_test_id(test_id)

        if element.count() == 0:
            return None

        text = element.inner_text().strip()
        digits = "".join(
            ch for ch in text if ch.isdigit()
        )

        return int(digits) if digits else 0

    def _get_numbers_from_body(self) -> list[int]:
        text = self.page.inner_text("body")

        return [
            int(word)
            for word in text.split()
            if word.isdigit()
        ]

    def get_total_books(self) -> int:
        count = self._get_int_from_test_id("book-count")

        if count is not None:
            return count

        return self._get_numbers_from_body()[0]

    def get_favorite_count(self) -> int:
        count = self._get_int_from_test_id("stars-count")

        if count is not None:
            return count

        return self._get_numbers_from_body()[-1]