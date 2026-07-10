from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://fojik.site/movie/the-furious-2026/")
    
    page.get_by_role("link", name="Links").click()
    
    with page.expect_popup() as popup:
        page.locator("#link-115015").get_by_role("link", name="Download").click()
        page1 = popup.value

    input("Press Enter to close...")

    browser.close()