import time

from playwright.sync_api import sync_playwright

from Launching_browser import browser

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")

    element = page.locator("div.bs-component > ul.list-group").nth(0).locator("li").nth(0)

    print(element.inner_text())
    time.sleep(20)
    browser.close()