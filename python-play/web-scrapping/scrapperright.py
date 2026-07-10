from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://fojik.site/movie/the-furious-2026/", wait_until="domcontentloaded")

    # Click the first Download button
    page.get_by_role("link", name="Download").first.click()

    # page.wait_for_load_state("networkidle")

    # Wait until Continue button appears
    page.locator("#maindownload").click()

    page.wait_for_load_state("networkidle")

    print(page.url)

    input("Press Enter...")