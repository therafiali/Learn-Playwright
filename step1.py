# pip install playwright
# playwright install
# playwright codegen https://www.google.com/

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_label("Search", exact=True).click()
    page.get_by_label("Search", exact=True).fill("time")
    page.goto("https://www.google.com/search?q=time&sca_esv=b72004035a3299c8&source=hp&ei=9SFpZ8buId7x1sQPoYvayAQ&iflsig=AL9hbdgAAAAAZ2kwBaAkWqIY8wwGcyvwbKmwoZH89fJb&ved=0ahUKEwiGvbSTv72KAxXeuJUCHaGFFkkQ4dUDCA4&uact=5&oq=time&gs_lp=Egdnd3Mtd2l6IgR0aW1lMgsQABiABBixAxiDATIIEAAYgAQYsQMyCBAAGIAEGLEDMggQABiABBixAzILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMg4QABiABBixAxiDARiKBTIOEAAYgAQYsQMYgwEYigUyCBAAGIAEGLEDMggQABiABBixA0j7ClDoA1itCXABeACQAQCYAbUBoAGzBaoBAzAuNLgBA8gBAPgBAZgCBaACxwWoAgrCAgoQABgDGOoCGI8BwgIFEAAYgATCAgsQLhiABBjRAxjHAcICERAuGIAEGLEDGNEDGIMBGMcBmAMH8QW4RKRZtNPBwpIHAzEuNKAHzho&sclient=gws-wiz")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
