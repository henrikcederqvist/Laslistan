from pages.base_page import BasePage, BASE_URL


class StatistikPage(BasePage):

    def goto(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("networkidle")
        self.navigate_to_statistics()

    # -----------------------
    # TOTAL BOOKS
    # -----------------------

    def get_total_books(self) -> int:
        # försök flera vanliga selectors (robust mot olika implementationer)
        locators = [
            self.page.locator("[data-testid='stat-total-books']"),
            self.page.locator("text=/totalt/i"),
            self.page.locator("text=/böcker/i"),
        ]

        for loc in locators:
            if loc.count() > 0:
                text = loc.first.inner_text()
                digits = "".join(c for c in text if c.isdigit())
                return int(digits) if digits else 0

        return 0

    # -----------------------
    # FAVORITES COUNT
    # -----------------------

    def get_favorite_count(self) -> int:
        locators = [
            self.page.locator("[data-testid='stat-favorites']"),
            self.page.locator("[data-testid='stat-favorite-count']"),
            self.page.locator("text=/favorit/i"),
        ]

        for loc in locators:
            if loc.count() > 0:
                text = loc.first.inner_text()
                digits = "".join(c for c in text if c.isdigit())
                return int(digits) if digits else 0

        return 0