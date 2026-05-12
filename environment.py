from playwright.sync_api import sync_playwright


def before_all(context):
    context._playwright = sync_playwright().start()
    context._browser = context._playwright.chromium.launch(headless=True)


def before_scenario(context, scenario):
    context.page = context._browser.new_page()


def after_scenario(context, scenario):
    context.page.close()


def after_all(context):
    context._browser.close()
    context._playwright.stop()