import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    """Launch a browser"""
    browser = p.chromium.launch(headless=False,slow_mo=500)
    """Create a new page"""
    page=browser.new_page()
    """Visit the website"""
    page.goto("https://dev.figsflow.com")
    browser.close()



