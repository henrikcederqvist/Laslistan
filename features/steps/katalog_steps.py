"""
features/steps/katalog_steps.py
Stegdefinitioner för katalog.feature
"""

from behave import when, then



@then("ska jag se minst en bok i listan")
def step_see_at_least_one_book(context):
    count = context.katalog.get_book_count()
    assert count > 0, f"Förväntade minst 1 bok, hittade {count}"


@then("ska varje bok ha en synlig titel")
def step_every_book_has_title(context):
    books = context.katalog.get_books()
    assert len(books) > 0
    for i in range(len(books)):
        title = context.katalog.get_book_title(i)
        assert title.strip() != "", f"Bok {i} saknar titel"


@then("ska varje bok ha en synlig författare")
def step_every_book_has_author(context):
    books = context.katalog.get_books()
    assert len(books) > 0
    for i in range(len(books)):
        author = context.katalog.get_book_author(i)
        assert author.strip() != "", f"Bok {i} saknar författare"


@when("jag klickar på favoritknappen för den första boken")
def step_click_favorite_first(context):
    context.katalog.click_favorite_button(0)


@when("jag klickar på favoritknappen för den första boken igen")
def step_click_favorite_first_again(context):
    context.katalog.click_favorite_button(0)


@then("ska den första boken vara markerad som favorit")
def step_first_book_is_marked_favorite(context):
    assert context.katalog.is_favorite(0), \
        "Förväntade att första boken är markerad som favorit"


@then("ska den första boken inte längre vara markerad som favorit")
def step_first_book_not_favorite(context):
    assert not context.katalog.is_favorite(0), \
        "Förväntade att första boken INTE är markerad som favorit"


@when("jag favoritmarkerar bok nummer {nummer:d}")
def step_toggle_book_n(context, nummer):
    index = nummer - 1
    context.katalog.toggle_favorite(index)
    context.toggled_index = index


@then("ska bok nummer {nummer:d} vara markerad som favorit")
def step_book_n_is_favorite(context, nummer):
    index = nummer - 1
    assert context.katalog.is_favorite(index), \
        f"Förväntade att bok {nummer} är favorit"


@then("ska övriga böcker inte vara påverkade")
def step_other_books_not_affected(context):
    books = context.katalog.get_books()
    toggled = context.toggled_index
    for i in range(len(books)):
        if i != toggled:
            assert not context.katalog.is_favorite(i), \
                f"Bok {i + 1} ska inte vara favorit men är det"
