import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
  browser = p.chromium.launch(headless=False,slow_mo=500)
  page = browser.new_page()
  page.goto("https://bootswatch.com/default/")
  Home_Navbar = page.locator("nav.bg-dark a.nav-link.active").highlight()
  time.sleep(5)



  """Here We have to select first parent locator then inside child selectors 
  [navbar navbar-expand-lg bg-dark]--. parent selector
  
  The main point is that class name is like nav-lin [space]
  
  [<a class="nav-link active" href="#">Home
                          <span class="visually-hidden">(current)</span>
                        </a>] --> Child selector
   active-link then that active link should be the class so you can select that link.
  """

  another_locator = page.locator("nav.bg-primary a.active").highlight()
  time.sleep(5)
  another_locator_1 = page.locator("nav.bg-primary a.dropdown-toggle").highlight()
  time.sleep(3)
  browser.close()