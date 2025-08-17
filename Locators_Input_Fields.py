from playwright.sync_api import sync_playwright

from Get_Element_By_ import Email_Address

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto("https://dev.figsflow.com")

    Email_Address = page.get_by_placeholder("Enter email").fill("testemail@gmail.com")
    Password = page.get_by_placeholder("Enter password").fill("FakePassword@121#")

    Login_button = page.get_by_text("Sign In")
    Login_button.click()

    browser.close()
