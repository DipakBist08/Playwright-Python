import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    URL ="https://bootswatch.com/default/"
    browser = p.chromium.launch(headless=False,slow_mo=200)
    page = browser.new_page()
    page.goto(URL)
    Element = page.get_by_role("button",name="primary").locator("nth=1").highlight()
    time.sleep(5)

    #Loacater based on their id

    page.locator("id =btnGroupDrop1").highlight()
    time.sleep(5)


    #Select Element Based on Filter
    page.get_by_role('heading').highlight()
    time.sleep(5)
    page.get_by_role("heading").filter(has_text="Heading").highlight()
    time.sleep(5)

    #If similar group
    page.locator("div.form-group").filter(has=page.get_by_label("password")).highlight()

    time.sleep(10)
    browser.close()