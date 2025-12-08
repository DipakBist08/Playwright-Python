from dotenv import load_dotenv
import os
load_dotenv()
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    context = browser.new_context(storage_state="playwright/.auth/storage_state.json")
    page = context.new_page()
    page = context.new_page()
    page.goto("https://accounts.google.com")
    page.pause()
    context.close()