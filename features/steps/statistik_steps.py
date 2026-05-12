from behave import given, when, then
from pages.statistik_page import StatistikPage
from pages.katalog_page import KatalogPage
from pages.lagg_till_bok_page import LaggTillBokPage


@then("ska jag se det totala antalet böcker")
def step_see_total_books(context):
    total = context.statistik.get_total_books()
    assert total >= 0, "Totalt antal böcker saknas eller är negativt"


@then("ska jag se antalet favoritmarkerade böcker")
def step_see_favorite_count(context):
    count = context.statistik.get_favorite_count()
    assert count >= 0, "Antal favoriter saknas eller är negativt"


@then("ska antalet favoriter visas som {antal:d}")
def step_favorites_shown_as(context, antal):
    count = context.statistik.get_favorite_count()
    assert count == antal, (
        f"Förväntade {antal} favoriter i statistik, fick {count}"
    )


@given("att jag noterar det aktuella totala antalet böcker")
def step_note_total_books(context):
    context.statistik = StatistikPage(context.page)
    context.statistik.goto()
    context.total_books_before = context.statistik.get_total_books()


@given("att jag noterar det aktuella antalet favoriter")
def step_note_favorite_count(context):
    if not hasattr(context, "statistik"):
        context.statistik = StatistikPage(context.page)
        context.statistik.goto()
    context.favorites_before = context.statistik.get_favorite_count()


@given("att en bok är markerad som favorit")
def step_ensure_one_favorite(context):
    context.katalog = KatalogPage(context.page)
    context.katalog.goto()
    if not context.katalog.is_favorite(0):
        context.katalog.toggle_favorite(0)


@when("jag lägger till en ny bok via formuläret")
def step_add_book_via_form(context):
    context.lagg_till = LaggTillBokPage(context.page)
    context.lagg_till.goto()
    context.lagg_till.fill_and_submit("Statistikbok", "Stat Fattaren")
    context.page.wait_for_load_state("networkidle")


@when("jag markerar en bok som favorit i katalogen")
def step_mark_book_favorite(context):
    context.katalog = KatalogPage(context.page)
    context.katalog.goto()
    book_count = context.katalog.get_book_count()
    for i in range(book_count):
        if not context.katalog.is_favorite(i):
            context.katalog.toggle_favorite(i)
            break


@when("jag tar bort favoritmarkeringen")
def step_remove_favorite_marking(context):
    context.katalog = KatalogPage(context.page)
    context.katalog.goto()
    for i in range(context.katalog.get_book_count()):
        if context.katalog.is_favorite(i):
            context.katalog.toggle_favorite(i)
            break


@then("ska det totala antalet böcker ha ökat med 1")
def step_total_books_increased(context):
    context.statistik = StatistikPage(context.page)
    new_total = context.statistik.get_total_books()
    assert new_total == context.total_books_before + 1, (
        f"Förväntade {context.total_books_before + 1} böcker, "
        f"fick {new_total}"
    )


@then("ska antalet favoriter ha ökat med 1")
def step_favorites_increased(context):
    context.statistik = StatistikPage(context.page)
    new_count = context.statistik.get_favorite_count()
    assert new_count == context.favorites_before + 1, (
        f"Förväntade {context.favorites_before + 1} favoriter, "
        f"fick {new_count}"
    )


@then("ska antalet favoriter ha minskat med 1")
def step_favorites_decreased(context):
    context.statistik = StatistikPage(context.page)
    new_count = context.statistik.get_favorite_count()
    assert new_count == context.favorites_before - 1, (
        f"Förväntade {context.favorites_before - 1} favoriter, "
        f"fick {new_count}"
    )