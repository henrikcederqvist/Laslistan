import os

from playwright.sync_api import sync_playwright

from src.features.pages.katalog_page import KatalogPage
from src.features.pages.lagg_till_bok_page import LaggTillBokPage


def before_all(context):
    context._playwright = sync_playwright().start()

    headless = os.getenv(
        "HEADLESS",
        "true"
    ).lower() == "true"

    context._browser = context._playwright.chromium.launch(
        headless=headless
    )


def before_scenario(context, scenario):
    context.page = context._browser.new_page()
    context.page.set_viewport_size({"width": 1280, "height": 720})
    context.page.set_default_timeout(10000)

    context.katalog = KatalogPage(context.page)
    context.lagg_till = LaggTillBokPage(context.page)


def after_scenario(context, scenario):
    context.page.close()


def after_all(context):
    context._browser.close()
    context._playwright.stop()