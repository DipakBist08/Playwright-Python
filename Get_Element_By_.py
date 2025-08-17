from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto("https://dev.figsflow.com/signin")

    Email_Address=page.get_by_placeholder("Enter email")
    Email_Address.fill("test@gmail.com")
    Password = page.get_by_placeholder("Enter password")
    Password.fill("test@pass121#")


    Login_button = page.get_by_role("button",name="Sign In")
    Login_button.click()

    browser.close()