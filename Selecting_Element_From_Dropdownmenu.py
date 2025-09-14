import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=400)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    Dropdown_Menu = page.locator("button#btnGroupDrop1")
    Dropdown_Menu.click()
    time.sleep(2)
    # Dropdown_group = page.locator("div.dropdown-menu:visible a:text('Dropdown link')").highlight()
    time.sleep(2)
    Select_Element = page.locator("div.dropdown-menu:visible a:text('Dropdown link')").first
    Select_Element.click()
    time.sleep(2)
    page.locator("button#btnGroupDrop4").click()
    time.sleep(2)
    page.locator("div.dropdown-menu:visible a:text('Dropdown link')").highlight()
    time.sleep(3)
    Dropdown_Element_Select = page.locator("div.dropdown-menu:visible a:text('Dropdown link')").last
    time.sleep(3)
    Dropdown_Element_Select.click()
    time.sleep(3)



    browser.close()