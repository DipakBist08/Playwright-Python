import time
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    # page.locator("h1:text('Navbars')").highlight() #This is called loose selector because if you change text still it select same.\
    """But if you want to select specific then you have to use --> page.locator("h1:text-is('Navs')") locator."""
    page.locator("h1:text-is('Navs')").highlight()
    time.sleep(10)
    page.locator("h1:text-is('Navs')").highlight()
    time.sleep(10)
    dropdown = page.locator("nav.bg-primary a.dropdown-toggle").click()
    time.sleep(5)

    browser.close()

