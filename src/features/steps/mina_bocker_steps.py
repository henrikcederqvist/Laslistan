from behave import given, then

from src.features.pages.mina_bocker_page import MinaBockerPage


@given("jag befinner mig på Mina böcker")
def step_given_my_books(context):
    context.mina = MinaBockerPage(context.page)
    context.mina.goto()


@then("ska jag se ett meddelande om att listan är tom")
def step_empty_message(context):
    assert context.mina.is_empty_message_visible(), (
        "Förväntade tom favoritlista eller meddelande om tom lista"
    )


@then("ska den boken finnas i min lista")
def step_book_exists_in_my_list(context):
    assert context.mina.get_favorite_count() > 0, (
        "Förväntade att minst en favoritbok skulle visas i Mina böcker"
    )


@then("ska jag se {antal:d} böcker i min lista")
def step_see_number_of_books(context, antal):
    count = context.mina.get_favorite_count()

    assert count == antal, (
        f"Förväntade {antal} böcker i Mina böcker, fick {count}"
    )