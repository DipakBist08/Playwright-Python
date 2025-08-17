import time

from playwright.sync_api import sync_playwright

from Launching_browser import browser

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto("https://dev.figsflow.com/signin")
    figsflow_logo =page.get_by_alt_text("logo").highlight()
    time.sleep(5)
    browser.close()