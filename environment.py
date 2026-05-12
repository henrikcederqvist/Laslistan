"""
environment.py
Behave hooks – startar och stänger Playwright-browser för varje scenario.
"""

import os
from playwright.sync_api import sync_playwright


def before_all(context):
    headless = os.environ.get("HEADLESS", "false").lower() == "true"
    context._playwright = sync_playwright().start()
    context._browser = context._playwright.chromium.launch(headless=headless)


def before_scenario(context, scenario):
    context.browser_context = context._browser.new_context()
    context.page = context.browser_context.new_page()


def after_scenario(context, scenario):
    context.browser_context.close()


def after_all(context):
    context._browser.close()
    context._playwright.stop()
