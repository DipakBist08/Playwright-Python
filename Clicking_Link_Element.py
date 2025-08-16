from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=800)
    page =browser.new_page()
    page.goto("https://playwright.dev/python")
    #select or locate with an element with "Docs"
    docs_button=page.get_by_role('link',name="Docs")
    docs_button.click()
    browser.close()

