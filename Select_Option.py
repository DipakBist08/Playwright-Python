import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=200)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    #Select by Value

    Select_Element = page.locator("#exampleSelect1")
    Select_Element.select_option("3")
    time.sleep(5)

    # Select by label(Visiable Text)
    Select_Element1 = page.get_by_label("Example select")
    Select_Element1.select_option("4")
    time.sleep(3)

    #Select By Index
    Select_Element2 = page.get_by_label("Example select")
    Select_Element2.select_option(index=1)
    time.sleep(5)
    browser.close()