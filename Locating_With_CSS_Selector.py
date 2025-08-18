import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto("https://dev.figsflow.com/signin")
    """To select CSS Selector you can you page.locator method i.e. --> page.locator("css=h1")
    """
    Email = page.locator("#\\:r0\\:-form-item").fill("testemail@gmail.com")
    Password = page.locator('input[name="password"]').fill("Password@123")
    Login_button = page.locator('button[type="submit"]').click()
    time.sleep(5)
    browser.close()


    #css selector continue