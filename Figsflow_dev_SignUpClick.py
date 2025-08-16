from playwright.sync_api import sync_playwright

from Launching_browser import browser

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    context =browser.new_context(
        viewport={"width":1920,"height":1080}
    )
    page = context.new_page()

    page.goto("https://dev.figsflow.com/signin")
    SignIn_Button = page.get_by_role("button",name="Sign In")
    SignIn_Button.click()
    SignUP_Click = page.get_by_role("link",name="Sign Up Now")
    SignUP_Click.click()
    print("SignUp URL:",page.url)
    page.go_back()
    Forgot_Password_Button = page.get_by_role("link", name="Forgot password?")
    Forgot_Password_Button.click()
    print("Forgot Password:",page.url)
    page.go_back()
    Login_Google = page.get_by_role("button",name="Continue with Google")
    Login_Google.click()
    print("Login With Google: ",page.url)

    browser.close()
