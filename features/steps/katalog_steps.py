from behave import given, when, then


@then("ska jag se minst en bok i listan")
def step_see_at_least_one_book(context):
    assert context.katalog.get_book_count() > 0


@then("ska varje bok ha en synlig titel")
def step_every_book_has_title(context):
    for i in range(context.katalog.get_book_count()):
        assert context.katalog.get_book_title(i) != ""


@then("ska varje bok ha en synlig författare")
def step_every_book_has_author(context):
    for i in range(context.katalog.get_book_count()):
        assert context.katalog.get_book_author(i) != ""


@when("jag klickar på favoritknappen för den första boken")
def step_click_first_favorite(context):
    context.katalog.click_favorite_button(0)


@when("jag klickar på favoritknappen för den första boken igen")
def step_click_first_favorite_again(context):
    context.katalog.click_favorite_button(0)


@given("att den första boken är markerad som favorit")
def step_first_book_is_favorite(context):
    if not context.katalog.is_favorite(0):
        context.katalog.click_favorite_button(0)


@then("ska den första boken vara markerad som favorit")
def step_first_book_should_be_favorite(context):
    assert context.katalog.is_favorite(0)


@then("ska den första boken inte längre vara markerad som favorit")
def step_first_book_should_not_be_favorite(context):
    assert not context.katalog.is_favorite(0)


@when("jag favoritmarkerar bok nummer {nummer:d}")
def step_favorite_book_number(context, nummer):
    index = nummer - 1
    context.katalog.click_favorite_button(index)
    context.toggled_index = index


@then("ska bok nummer {nummer:d} vara markerad som favorit")
def step_book_number_should_be_favorite(context, nummer):
    index = nummer - 1
    assert context.katalog.is_favorite(index)


@then("ska övriga böcker inte vara påverkade")
def step_other_books_not_affected(context):
    for i in range(context.katalog.get_book_count()):
        if i != context.toggled_index:
            assert not context.katalog.is_favorite(i)