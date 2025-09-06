""".1 fill() --> to input value inside input field.
    2. input_value() --> get a value form input field.
    3. clear()--> Used to clear input field.

"""
import time

from  playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=200)
    page = browser.new_page()
    page.goto("https://dev.figsflow.com")
    Email_Address = page.get_by_placeholder("Enter email")
    Email_Address.fill("example@gmail.com")
    time.sleep(3)
    Email_Address.clear()

    time.sleep(3)
    #To input text in Type style/format in input text field
    Email_Address.type("hellodeepak@gmail.com",delay=200)
    time.sleep(5)

    #To get value form input text field
    Extract_Value= Email_Address.input_value()
    print(Extract_Value)
    time.sleep(5)
    browser.close()




