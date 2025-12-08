
import os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
load_dotenv()
email = os.getenv('GOOGLE_EMAIL')
password = os.getenv('GOOGLE_PASSWORD')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500,args=["--disable-dev-shm-usage","--disable-blink-features=AutomationControlled"])
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://accounts.google.com")
    email_input = page.get_by_label("Email or phone")
    email_input.clear()
    email_input.fill(email)
    Next_button = page.get_by_role("button",name="Next")
    Next_button.click()
    password_input = page.get_by_label("Enter your password")
    password_input.clear()
    password_input.fill(password)

    Next_button.click()
    page.pause()

    #save authentication state
    context.storage_state(path="playwright/.auth/storage_state.json")
    context.close()

#



