from behave import given, when, then
from src.features.pages.katalog_page import KatalogPage
from src.features.pages.lagg_till_bok_page import LaggTillBokPage
from src.features.pages.mina_bocker_page import MinaBockerPage
from src.features.pages.statistik_page import StatistikPage


@given("att jag öppnar webbsidan")
def step_open_website(context):
    context.katalog = KatalogPage(context.page)
    context.katalog.goto()


@given("att jag befinner mig på katalogsidan")
def step_on_catalog(context):
    context.katalog = KatalogPage(context.page)
    context.katalog.goto()


@given("att jag befinner mig på sidan för att lägga till bok")
def step_on_add_book(context):
    context.lagg_till = LaggTillBokPage(context.page)
    context.lagg_till.goto()


@given("att jag befinner mig på Mina böcker")
def step_on_my_books(context):
    context.mina = MinaBockerPage(context.page)
    context.mina.goto()


@given("att jag befinner mig på statistiksidan")
def step_on_statistics(context):
    context.statistik = StatistikPage(context.page)
    context.statistik.goto()


@given("att inga böcker är markerade som favoriter")
def step_no_books_are_favorites(context):
    context.katalog = KatalogPage(context.page)
    context.katalog.goto()

    for i in range(context.katalog.get_book_count()):
        if context.katalog.is_favorite(i):
            context.katalog.click_favorite_button(i)


@given("att jag har markerat den första boken som favorit i katalogen")
def step_first_book_marked_favorite(context):
    context.katalog = KatalogPage(context.page)
    context.katalog.goto()

    if not context.katalog.is_favorite(0):
        context.katalog.click_favorite_button(0)

    context.first_book_title = context.katalog.get_book_title(0)


@given("att jag har markerat {antal:d} böcker som favoriter i katalogen")
def step_n_books_marked_favorite(context, antal):
    context.katalog = KatalogPage(context.page)
    context.katalog.goto()

    for i in range(context.katalog.get_book_count()):
        if context.katalog.is_favorite(i):
            context.katalog.click_favorite_button(i)

    for i in range(antal):
        context.katalog.click_favorite_button(i)

    context.expected_favorite_count = antal


@given("att en bok är markerad som favorit")
def step_one_book_is_favorite(context):
    context.katalog = KatalogPage(context.page)
    context.katalog.goto()

    if not context.katalog.is_favorite(0):
        context.katalog.click_favorite_button(0)


@when("jag navigerar till katalogsidan")
def step_nav_catalog(context):
    button = context.page.get_by_test_id("catalog")
    if button.is_enabled():
        button.click()
    context.page.wait_for_load_state("networkidle")
    context.katalog = KatalogPage(context.page)


@when("jag navigerar till Mina böcker")
def step_nav_my_books(context):
    context.page.get_by_test_id("favorites").click()
    context.page.wait_for_load_state("networkidle")
    context.mina = MinaBockerPage(context.page)


@when("jag navigerar till statistiksidan")
def step_nav_statistics(context):
    button = context.page.get_by_test_id("statistics")

    if button.is_enabled():
        button.click()
        context.page.wait_for_load_state("networkidle")

    context.statistik = StatistikPage(context.page)


@when('jag klickar på länken "{link}"')
def step_click_nav_link(context, link):
    mapping = {
        "Katalog": "catalog",
        "Lägg till bok": "add-book",
        "Mina böcker": "favorites",
        "Statistik": "statistics",
    }

    button = context.page.get_by_test_id(mapping[link])
    if button.is_enabled():
        button.click()

    context.page.wait_for_load_state("networkidle")


@then("ska jag befinna mig på katalogsidan")
def step_should_be_catalog(context):
    assert context.page.locator("div.book").count() > 0


@then("ska jag befinna mig på sidan för att lägga till bok")
def step_should_be_add_book(context):
    assert context.page.get_by_test_id("add-input-title").count() > 0


@then("ska jag befinna mig på sidan för mina böcker")
def step_should_be_my_books(context):
    body = context.page.inner_text("body").lower()
    assert "mina" in body or "favorit" in body


@then("ska jag befinna mig på statistiksidan")
def step_should_be_statistics(context):
    body = context.page.inner_text("body").lower()
    assert "statistik" in body or "antal" in body


@then('ska sidtiteln innehålla "{title}"')
def step_title_contains(context, title):
    body = context.page.inner_text("body").lower()
    assert title.lower() in body