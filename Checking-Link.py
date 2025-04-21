from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto("https://dev.figsflow.com")
    forgot_password=page.get_by_role('link',name="Forgot password?")
    forgot_password.click()
    forgot_password.clear()

    browser.close()
