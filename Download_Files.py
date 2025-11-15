from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    page.goto("https://pixabay.com/photos/nature-forest-landscape-at-night-3194001/")

    Image_download_dropdown = page.get_by_role("button",name="Download")
    Image_download_dropdown.click()

    Download_Options = page.locator("div.downloadItem--xBKyT").last
    Download_Options.click()
    Download_Btn = page.locator('div.buttons--cqw3Y > a:has-text("Download")')
    with page.expect_download() as download_info:
        Download_Btn.click()
        download = download_info.value
        download.save_as("moon1.jpg")

    time.sleep(10)

    browser.close()
