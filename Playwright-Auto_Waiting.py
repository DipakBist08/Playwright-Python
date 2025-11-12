from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser =p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto("https://bootswatch.com/")
    link = page.locator("a.dropdown-item").first
    #a.dropdown-item  is inside the dropdown so not visible so it will throw a time-out error but if you click on dropdown it will work.
    link.click()
    browser.close()

    """Basically the scene behind is first playwright wait until finished browser's spanning and waits untill elements visible,enable, and stable"""