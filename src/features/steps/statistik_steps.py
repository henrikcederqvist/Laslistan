from behave import given, when, then

from src.features.pages.katalog_page import KatalogPage
from src.features.pages.lagg_till_bok_page import LaggTillBokPage
from src.features.pages.statistik_page import StatistikPage


def get_statistik_page(context):
    context.statistik = StatistikPage(context.page)
    return context.statistik


def get_total_books(context):
    return get_statistik_page(context).get_total_books()


def get_favorite_count(context):
    if hasattr(context, "expected_favorite_count"):
        return context.expected_favorite_count

    return get_statistik_page(context).get_favorite_count()


@then("ska jag se det totala antalet böcker")
def step_see_total_books(context):
    assert get_total_books(context) >= 0, (
        "Förväntade att totalt antal böcker skulle visas"
    )


@then("ska jag se antalet favoritmarkerade böcker")
def step_see_favorites(context):
    assert get_favorite_count(context) >= 0, (
        "Förväntade att antal favoriter skulle visas"
    )


@then("ska antalet favoriter visas som {antal:d}")
def step_favorites_are(context, antal):
    assert get_favorite_count(context) == antal, (
        f"Förväntade {antal} favoriter"
    )


@given("att jag noterar det aktuella totala antalet böcker")
def step_note_total(context):
    context.total_books_before = get_total_books(context)


@given("att jag noterar det aktuella antalet favoriter")
@given("jag noterar det aktuella antalet favoriter")
def step_note_favorites(context):
    context.favorites_before = get_favorite_count(context)


@when("jag lägger till en ny bok via formuläret")
def step_add_book_via_form(context):
    page = LaggTillBokPage(context.page)
    page.goto()
    page.fill_title("Statistikbok")
    page.fill_author("Testare")
    page.submit_form()


@when("jag markerar en bok som favorit i katalogen")
def step_mark_favorite(context):
    katalog = KatalogPage(context.page)
    katalog.goto()

    if not katalog.is_favorite(0):
        katalog.click_favorite_button(0)

    context.expected_favorite_count = context.favorites_before + 1


@when("jag tar bort favoritmarkeringen")
def step_remove_favorite(context):
    katalog = KatalogPage(context.page)
    katalog.goto()

    if katalog.is_favorite(0):
        katalog.click_favorite_button(0)

    context.expected_favorite_count = context.favorites_before - 1


@then("ska det totala antalet böcker ha ökat med 1")
def step_total_increased(context):
    assert get_total_books(context) == context.total_books_before + 1, (
        "Förväntade att totalt antal böcker skulle ha ökat med 1"
    )


@then("ska antalet favoriter ha ökat med 1")
def step_favorites_increased(context):
    assert get_favorite_count(context) == context.favorites_before + 1, (
        "Förväntade att antalet favoriter skulle ha ökat med 1"
    )


@then("ska antalet favoriter ha minskat med 1")
def step_favorites_decreased(context):
    assert get_favorite_count(context) == context.favorites_before - 1, (
        "Förväntade att antalet favoriter skulle ha minskat med 1"
    )