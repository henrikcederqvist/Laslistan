from playwright.sync_api import sync_playwright


def before_all(context):
    context._playwright = sync_playwright().start()
    context._browser = context._playwright.chromium.launch(headless=True)


def before_scenario(context, scenario):
    context.page = context._browser.new_page()
    context.page.set_viewport_size({"width": 1280, "height": 720})
    context.page.set_default_timeout(10000)


def after_scenario(context, scenario):
    if hasattr(context, "page"):
        context.page.close()


def after_all(context):
    context._browser.close()
    context._playwright.stop()