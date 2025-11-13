from  playwright.sync_api import sync_playwright
def on_dialog(dialog):
    dialog.accept() # dialog.dismiss()
    print("Dialog accepted...")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    page = browser.new_page()
    page.goto("https://testpages.herokuapp.com/pages/basics/alerts-javascript/")
    page.on("dialog",on_dialog)
    # alert1 = page.get_by_text("Show alert box")
    # alert1.click()
    alert2 = page.get_by_text("Show confirm box")
    alert2.click()
    # alert_input = page.get_by_text("Show prompt box")
    # alert_input.click()


    browser.close()

