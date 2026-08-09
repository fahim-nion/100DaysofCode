from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://example.com")
    page.get_by_role("link", name="More information...").click()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)