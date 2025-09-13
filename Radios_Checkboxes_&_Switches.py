import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=300)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    #For Radio Button
    radio_option_2 = page.get_by_label("Option two can be something else and selecting it will deselect option one")
    radio_option_2.check()
    time.sleep(3)
    #For Checkboxes
    checkbox = page.get_by_placeholder("                        Default checkbox")
    checkbox.check()
    time.sleep(5)
    checkbox_1 = page.get_by_placeholder("Checked checkbox")
    checkbox_1.uncheck()
    time.sleep(5)
    browser.close()



