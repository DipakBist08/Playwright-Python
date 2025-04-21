from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto("https://dev.figsflow.com")
    forgot_password=page.get_by_role('link',name="Forgot password?")
    forgot_password.click()
    forgot_password.clear()
    browser.close()
"""-----Locators in Playwright------
-------------------------------------
1. page.get_by_role()
2. page.get_by_text()
3. page.get_by_label()
4. page.get_by_label()
5. page.get_by_title()
6. page.get_by_placeholder()
7. page.get_by_alt_text()
8.page.get_by_test_id()
9. page.get_by_attribute()
"""