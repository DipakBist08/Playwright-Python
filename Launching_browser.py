from playwright.sync_api import sync_playwright
#playwright=sync_playwright().start()or
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False,slow_mo=800)
    #create a new page
    page =browser.new_page()
    page.goto("https://playwright.dev/python") #playwright website
    browser.close()
