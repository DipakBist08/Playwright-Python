from playwright.sync_api import sync_playwright
def on_load(page):
    print("page Loaded:",page)
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.on("load",on_load) # page.on() you can pass events like 'load','request','response','domcontentloaded'
    page.goto("https://bootswatch.com/default")

    browser.close()

