import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto("https://dev.figsflow.com")


    SignIn_Button = page.locator("button[type='submit']")
    SignIn_Button.hover()
    time.sleep(3)

    SignIn_Button.click()
    time.sleep(3)



    """
    combine clicks with keyboard modifiers (like Control, Shift, Alt, Meta)
    """

    # Ctrl + Click
    SignIn_Button.click(modifiers=["Control"])
    time.sleep(3)
    #shift + click
    SignIn_Button.click(modifiers=["Shift"])
    time.sleep(3)
    SignIn_Button.click(modifiers=["Alt"])
    time.sleep(3)
    # Meta + Click (⌘ on Mac, Windows key on Windows/Linux)
    SignIn_Button.click(modifiers=["Meta"])
    time.sleep(3)

    #Right/Left Click()
    SignIn_Button.click(button="right")
    time.sleep(3)
    SignIn_Button.click(button="left")
    time.sleep(3)
    browser.close()
