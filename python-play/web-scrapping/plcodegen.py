import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://fojik.site/movie/the-furious-2026/")
    # page.get_by_role("button", name="Close Notice").click()
    page.get_by_role("link", name="Links").click()
    with page.expect_popup() as page1_info:
        page.locator("#link-115015").get_by_role("link", name="Download").click()
    page1 = page1_info.value
    with page1.expect_popup() as page2_info:
        page1.get_by_role("button", name="Continue to Destination").click()
    page2 = page2_info.value
    page2.close()
    page1.get_by_role("link", name="GDrive").nth(2).wait_for()
    page1.get_by_role("button", name="Continue to Destination").click()
    with page1.expect_popup() as page4_info:
        page1.get_by_role("link", name="Continue to Destination").click()
    page4 = page4_info.value
    page4.close()
    with page1.expect_popup() as page5_info:
        page1.get_by_text("X", exact=True).click()
    page5 = page5_info.value
    page5.close()
    with page1.expect_popup() as page6_info:
        page1.get_by_role("link", name="GDrive").nth(2).click()
    page6 = page6_info.value
    with page6.expect_popup() as page9_info:
        page6.get_by_role("link", name="Download Link").click()
    page9 = page9_info.value
    print("page6:", page6.url)
    print("page9:", page9.url)
    print(page9.url)
    page9.wait_for_load_state("domcontentloaded")
    page9.wait_for_timeout(2000)

    print("page6:", page6.url)
    print("page9:", page9.url)

    print("Download button on page6:",
        page6.get_by_role("button", name="Download Now").count())

    print("Download button on page9:",
        page9.get_by_role("button", name="Download Now").count())

    print("Page9 title:", page9.title())

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
