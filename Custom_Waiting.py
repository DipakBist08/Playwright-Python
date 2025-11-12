from time import perf_counter
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page=browser.new_page()

    page.goto("https://www.scrapethissite.com/pages/ajax-javascript")
    link = page.get_by_role("link",name='2015')
    link.click()
    print("2015 Oscer listed movies are loading...")
    start = perf_counter()
    first_table_data = page.locator("td.film-title").first
    first_table_data.wait_for(state="visible")  # This wait_for() method waits until loader finished.
    time_taken = perf_counter()-start
    print(f"The movies loaded in {round(time_taken,2)}s")
    browser.close()


"""Inside wait_for() method you can pass different states like 'enable','visible'
ig wait_for(state=visible)

"""