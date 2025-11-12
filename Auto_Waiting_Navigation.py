from playwright.sync_api import sync_playwright
from time import perf_counter
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
    print("Page Loading")
    start = perf_counter()
    #There are basically 4 events for autoloading, load,domcontentloaded,networkidle & commit.
    page.goto("https://bootswatch.com/",wait_until='load') #here you can set any event as your preference
    time_taken = perf_counter() - start
    print(f"Page loaded in {round(time_taken,2)}s")
    browser.close()
"""

1. commit-->which gets called, when we have received response from server.
2. domcontentloade--> Which gets called when the HTML is parsed and displayed in the website.
3. load-->which is called when all the resources along with the html documents get loaded.
4. networkidle--> which gets called when all the networks ins and outs are finished in our browser.
"""