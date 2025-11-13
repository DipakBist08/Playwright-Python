from playwright.sync_api import sync_playwright
def alert_1(dialog):
    dialog.accept()
    print("Alert-1 Dialog accepted",dialog)

def alert_2(dialog):
    dialog.accept()
    print("Alert-2 Dialog confirmed.",dialog)

def alert_3(dialog):
    dialog.accept("Playwright is cool")
    print("Alert-3 prompt inputted.",dialog)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    page = browser.new_page()
    page.goto("https://testpages.herokuapp.com/pages/basics/alerts-javascript/")
    page.once("dialog",alert_1)
    #Alert 1 web element
    alert1_Element = page.get_by_text("Show alert box")
    alert1_Element.click()

    #Alert2 web element
    alert_2_Element = page.get_by_text("Show confirm box")
    alert_2_Element.click()

    #Alert 3 web element

    alert_3_Element = page.get_by_text("Show prompt box")
    alert_3_Element.click()



    browser.close()