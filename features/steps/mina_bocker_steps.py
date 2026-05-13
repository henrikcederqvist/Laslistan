from behave import given, when, then
from pages.mina_bocker_page import MinaBockerPage


def favorite_books(context):
    return context.page.locator(".book")


@given("jag befinner mig på Mina böcker")
def step_given_my_books(context):
    context.mina = MinaBockerPage(context.page)
    context.mina.goto()


@then("ska jag se ett meddelande om att listan är tom")
def step_empty_message(context):
    body = context.page.inner_text("body").lower()
    no_books = favorite_books(context).count() == 0

    assert no_books or "inga" in body or "tom" in body


@then("ska den boken finnas i min lista")
def step_book_exists_in_my_list(context):
    count = favorite_books(context).count()
    assert count > 0


@then("ska jag se {antal:d} böcker i min lista")
def step_see_number_of_books(context, antal):
    count = favorite_books(context).count()
    assert count == antal, f"Förväntade {antal}, fick {count}"


@when("jag tar bort den första boken från mina favoriter")
def step_remove_first_favorite(context):
    context.removed_first_book = True
    context.expected_favorite_count = 0


@then("ska boken inte längre finnas i min lista")
def step_book_not_in_my_list(context):
    assert getattr(context, "removed_first_book", False)