import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=300)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    file_input = page.get_by_label("Default file input example")
    file_input.set_input_files("DYC.pdf")
    time.sleep(10)

    """To Choose Multiple File, if software allows"""
    #unfortunetly it doesn't allow multi file selection
    # Multi_fileInput = page.get_by_label("Default file input example")
    # Multi_fileInput.set_input_files("['DYC.pdf'],['DYC1.pdf'],['DYC3.png']")


    """Another Scenario if file chooser not available,
     we can use playwright page object expect file chooser"""
    # with page.expect_file_chooser() as fc_info:
    #     file_input.click()
    #     file_chooser= fc_info.value
    #     file_chooser.set_files("DYC.pdf")
    #     time.sleep(10)


    browser.close()
