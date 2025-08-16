from playwright.sync_api import sync_playwright
#playwright=sync_playwright().start()or
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False,slow_mo=800) #slow_mo is used to see how you are interacting visually
    #create a new page
    page =browser.new_page()
    page.goto("https://playwright.dev/python") #playwright website
    #get URL
    print("Docs:",page.url)
    browser.close()
