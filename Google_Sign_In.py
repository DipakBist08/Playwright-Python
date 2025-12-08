import  os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
load_dotenv()

email = os.getenv('GOOGLE_EMAIL')
password = os.getenv('GOOGLE_PASSWORD')
print(f"EMAIL Loaded: {email}")
print(f"Password loaded: {password}")
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500,args=["--disable-dev-shm-usage","--disable-blink-features=AutomationControlled"])
    page = browser.new_page()
    page.goto("https://accounts.google.com")
    email_phone = page.get_by_label("Email or phone")
    email_phone.clear()
    email_phone.fill(email)
    Next_button = page.get_by_role("button",name="Next")
    Next_button.click()
    Enter_password = page.get_by_label("Enter your password")
    Enter_password.clear()
    Enter_password.fill(password)
    Next_button.click()
