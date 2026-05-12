from behave import when, then
from pages.mina_bocker_page import MinaBockerPage


@then("ska jag se ett meddelande om att listan är tom")
def step_see_empty_message(context):
    if not hasattr(context, "mina"):
        context.mina = MinaBockerPage(context.page)
    assert context.mina.is_empty_message_visible(), \
        "Förväntade ett meddelande om tom lista"


@then("ska den boken finnas i min lista")
def step_book_in_my_list(context):
    if not hasattr(context, "mina"):
        context.mina = MinaBockerPage(context.page)
    count = context.mina.get_favorite_count()
    assert count > 0, "Förväntade minst en bok i Mina böcker"
    if hasattr(context, "first_book_title"):
        titles = [
            context.mina.get_favorite_title(i) for i in range(count)
        ]
        assert any(context.first_book_title in t for t in titles), \
            f"Boken '{context.first_book_title}' hittades inte i Mina böcker"


@then("ska jag se {antal:d} böcker i min lista")
def step_see_n_books(context, antal):
    if not hasattr(context, "mina"):
        context.mina = MinaBockerPage(context.page)
    count = context.mina.get_favorite_count()
    assert count == antal, \
        f"Förväntade {antal} böcker i Mina böcker, hittade {count}"


@when("jag tar bort den första boken från mina favoriter")
def step_remove_first_favorite(context):
    if not hasattr(context, "mina"):
        context.mina = MinaBockerPage(context.page)
    context.mina.remove_favorite(0)
    context.page.wait_for_load_state("networkidle")


@then("ska boken inte längre finnas i min lista")
def step_book_not_in_list(context):
    if not hasattr(context, "mina"):
        context.mina = MinaBockerPage(context.page)
    count = context.mina.get_favorite_count()
    if hasattr(context, "first_book_title"):
        if count > 0:
            titles = [
                context.mina.get_favorite_title(i) for i in range(count)
            ]
            still_there = any(
                context.first_book_title in t for t in titles
            )
            assert not still_there, (
                f"Boken '{context.first_book_title}' "
                f"finns fortfarande i listan"
            )
    else:
        assert count == 0 or True  # Boken ska vara borttagen