# check_playwright.py
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browsers = [p.chromium, p.firefox, p.webkit]
    for browser_type in browsers:
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto("https://facebook.com")
        print(f"{browser_type.name} working: {page.title()}")
        browser.close()
