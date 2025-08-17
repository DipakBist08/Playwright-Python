 #You can run the script by using terminal which is called REPEL feature in python-playwright
"""Steps:
1. Open terminal ctrl+alt+t in linux
2.you must have to install playwright by your terminal if you are start from beaning.--> playwright install
2. After successful install Type python3 and hit enter
3.Import playwright --> form playwright.sync_api from sync_playwright
4. Start Playwright ---> playwright = sync_playwright.start()
5.Launch Browser--> browser = playwright.chromium.launch(headless=False,slow_mo=500) 
6. See browser info --> input browser and hit inter
7. Create new page --> page=browser.new_page()
8. Provide website URL--> page.goto("https://dev.figsflow.com/signin")
9. Get Element --> signin_button = page.get_by_role("button",name="Sign In")
10. Click or Highlight Element --> signin_button.click() or signin_button.highlight()
11. Close browser --> browser.closer() 
"""

from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False,slow_mo=1000)

page = browser.new_page()
page.goto("https://dev.figsflow.com/signin")

signin_button = page.get_by_role("button",name="Sign In")
signin_button.highlight()
signin_button.click()
browser.close()