from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    page.goto("https://yahoo.com")
    page.screenshot(path="images/yahoo.jpg")
    browser.close()
