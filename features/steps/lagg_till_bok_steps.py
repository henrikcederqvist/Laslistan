from behave import use_step_matcher, when, then
from pages.katalog_page import KatalogPage

use_step_matcher("parse")


@then("ska jag se ett fält för boktitel")
def step_see_title_field(context):
    assert (
        context.lagg_till.page.get_by_test_id(
            "add-input-title"
        ).count() > 0
    ), "Hittade inget fält för boktitel"


@then("ska jag se ett fält för författare")
def step_see_author_field(context):
    assert (
        context.lagg_till.page.get_by_test_id(
            "add-input-author"
        ).count() > 0
    ), "Hittade inget fält för författare"


@when('jag fyller i titeln "{titel}" och författaren "{forfattare}"')
def step_fill_form(context, titel, forfattare):
    context.lagg_till.fill_title(titel)
    context.lagg_till.fill_author(forfattare)
    context.submitted_title = titel


@when("jag skickar in formuläret")
def step_submit_form(context):
    context.lagg_till.submit_form()
    context.page.wait_for_load_state("networkidle")


@when("jag försöker skicka in formuläret")
def step_try_submit_form(context):
    context.lagg_till.submit_form()


@then('ska boken "{titel}" visas i katalogen')
def step_book_visible_in_catalog(context, titel):
    katalog = KatalogPage(context.page)
    katalog.goto()

    titles = [
        katalog.get_book_title(i)
        for i in range(katalog.get_book_count())
    ]

    assert any(
        titel in t for t in titles
    ), f"Boken '{titel}' hittades inte i katalogen"


@then('ska boken "{titel}" finnas i listan')
def step_book_in_list(context, titel):
    katalog = KatalogPage(context.page)

    titles = [
        katalog.get_book_title(i)
        for i in range(katalog.get_book_count())
    ]

    assert any(
        titel in t for t in titles
    ), f"Boken '{titel}' hittades inte i listan"


@then("ska formulärfälten vara tomma")
def step_form_fields_empty(context):
    assert (
        context.lagg_till.is_form_empty()
    ), "Förväntade att formulärfälten är tomma"


@then("ska formuläret inte ha skickats in")
def step_form_not_submitted(context):
    assert (
        context.page.get_by_test_id(
            "add-input-title"
        ).count() > 0
    ), "Formuläret verkar ha skickats in"