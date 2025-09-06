import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")

    Element = page.locator("xpath=//h1")
    Element.highlight()
    #Selecting Element Based on Attributes
    Element_1 = page.locator("//h1[@id='navbars']")
    Element_1.highlight()
    Email = page.locator('//input [@ type="email"]').highlight()

    time.sleep(5)
    browser.close()