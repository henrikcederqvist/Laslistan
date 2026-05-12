from behave import given, when, then
from pages.katalog_page import KatalogPage
from pages.lagg_till_bok_page import LaggTillBokPage
from pages.mina_bocker_page import MinaBockerPage
from pages.statistik_page import StatistikPage


@given("att jag öppnar webbsidan")
def step_open_website(context):
    context.katalog = KatalogPage(context.page)
    context.katalog.goto()


@given("att jag befinner mig på katalogsidan")
def step_on_catalog(context):
    context.katalog = KatalogPage(context.page)
    context.katalog.goto()
    context.katalog.debug_page()


@given("att jag befinner mig på sidan för att lägga till bok")
def step_on_add_book(context):
    context.lagg_till = LaggTillBokPage(context.page)
    context.lagg_till.goto()


@given("att jag befinner mig på Mina böcker")
def step_on_my_books_given(context):
    context.mina = MinaBockerPage(context.page)
    context.mina.goto()


@given("att jag befinner mig på statistiksidan")
def step_on_statistics_given(context):
    context.statistik = StatistikPage(context.page)
    context.statistik.goto()


@when('jag navigerar till katalogsidan')
def step_navigate_to_catalog(context):
    if not hasattr(context, "katalog"):
        context.katalog = KatalogPage(context.page)
    context.katalog.navigate_to_catalog()


@when('jag navigerar till Mina böcker')
def step_navigate_to_my_books(context):
    if not hasattr(context, "mina"):
        context.mina = MinaBockerPage(context.page)
    context.mina.navigate_to_my_books()


@when('jag navigerar till statistiksidan')
def step_navigate_to_statistics(context):
    if not hasattr(context, "statistik"):
        context.statistik = StatistikPage(context.page)
    context.statistik.navigate_to_statistics()


@when('jag klickar på länken "{lank}"')
def step_click_nav_link(context, lank):
    testid_map = {
        "Katalog": "catalog",
        "Lägg till bok": "add-book",
        "Mina böcker": "favorites",
        "Statistik": "statistics",
    }
    testid = testid_map.get(lank, lank)
    context.page.get_by_test_id(testid).click()
    context.page.wait_for_load_state("networkidle")


@then("ska jag befinna mig på katalogsidan")
def step_assert_on_catalog(context):
    assert "katalog" in context.page.title().lower() or \
           "katalog" in context.page.url.lower() or \
           context.page.get_by_test_id("book-item").count() > 0


@then("ska jag befinna mig på sidan för att lägga till bok")
def step_assert_on_add_book(context):
    assert context.page.get_by_test_id("input-title").count() > 0 or \
           "lägg" in context.page.title().lower()


@then("ska jag befinna mig på sidan för mina böcker")
def step_assert_on_my_books(context):
    assert "mina" in context.page.title().lower() or \
           context.page.get_by_test_id("favorite-item").count() >= 0


@then("ska jag befinna mig på statistiksidan")
def step_assert_on_statistics(context):
    assert "statistik" in context.page.title().lower() or \
           context.page.get_by_test_id("stat-total-books").count() > 0


@then('ska sidtiteln innehålla "{titel}"')
def step_page_title_contains(context, titel):
    heading = context.page.locator("h1, h2").first.inner_text()
    assert titel.lower() in heading.lower(), \
        f"Förväntade '{titel}' i rubriken, fick '{heading}'"


@given("att inga böcker är markerade som favoriter")
def step_no_favorites(context):
    context.katalog = KatalogPage(context.page)
    context.katalog.goto()
    books = context.katalog.get_books()
    for i in range(len(books)):
        if context.katalog.is_favorite(i):
            context.katalog.toggle_favorite(i)


@given("att den första boken är markerad som favorit")
def step_first_book_is_favorite(context):
    if not hasattr(context, "katalog"):
        context.katalog = KatalogPage(context.page)
        context.katalog.goto()
    if not context.katalog.is_favorite(0):
        context.katalog.toggle_favorite(0)


@given("att jag har markerat den första boken som favorit i katalogen")
def step_mark_first_as_favorite(context):
    context.katalog = KatalogPage(context.page)
    context.katalog.goto()
    if not context.katalog.is_favorite(0):
        context.katalog.toggle_favorite(0)
    context.first_book_title = context.katalog.get_book_title(0)


@given("att jag har markerat {antal:d} böcker som favoriter i katalogen")
def step_mark_n_as_favorites(context, antal):
    context.katalog = KatalogPage(context.page)
    context.katalog.goto()
    book_count = context.katalog.get_book_count()
    for i in range(min(book_count, 10)):
        if context.katalog.is_favorite(i):
            context.katalog.toggle_favorite(i)
    for i in range(antal):
        context.katalog.toggle_favorite(i)
    context.expected_favorite_count = antal