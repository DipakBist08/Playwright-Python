import time
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default")
    """<abbr title="attribute">attr</abbr>
    this type of elements contain inside <abbar>
    """


    element = page.get_by_title("attribute").highlight()
    time.sleep(5)
    browser.close()

