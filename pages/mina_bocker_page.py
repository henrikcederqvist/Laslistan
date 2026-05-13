from pages.base_page import BasePage, BASE_URL


class MinaBockerPage(BasePage):

    def goto(self):
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("networkidle")
        self.navigate_to_my_books()

    def get_favorite_books(self):
        return self.page.get_by_test_id("favorite-item")

    def get_favorite_count(self):
        return self.get_favorite_books().count()

    def get_favorite_title(self, index):
        return self.get_favorite_books().nth(index).get_by_test_id(
            "book-title"
        ).inner_text()

    def remove_favorite(self, index):
        self.get_favorite_books().nth(index).get_by_test_id(
            "remove-favorite"
        ).click()
        self.page.wait_for_load_state("networkidle")

    def is_empty_message_visible(self):
        msg = self.page.get_by_test_id("empty-favorites")
        return msg.count() > 0 and msg.is_visible()