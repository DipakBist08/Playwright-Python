from playwright.sync_api import sync_playwright

from Launching_browser import browser

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    page = browser.new_page()
    page.goto("https://dev.figsflow.com/signin")
    SignIn_Button = page.get_by_role("button",name="Sign In")
    SignIn_Button.click()
    SignUP_Click = page.get_by_role("link",name="Sign Up Now")
    SignUP_Click.click()
    print("SignUp URL:",page.url)

    browser.close()
