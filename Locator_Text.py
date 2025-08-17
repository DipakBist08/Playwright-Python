import time
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto("https://dev.figsflow.com/signin")

    text_locator = page.get_by_text("FigsFlow Login").highlight()

    #you can highlight the specific text from the paragraph. for that, you have to set arguments exact=True/False.
    text_locator_1 = page.get_by_text("FigsFlow!",exact=False).highlight()
    time.sleep(5)
    browser.close()