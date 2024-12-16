from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright


from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)  # Set headless=False to see the browser
    page = browser.new_page()

    # Navigate to a webpage
    page.goto("https://google.com")

    Close the browser
    browser.close()
