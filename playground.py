from playwright.sync_api import sync_playwright
from datetime import datetime

# Time in seconds
dt = datetime.today()
seconds = dt.timestamp()
print(round(seconds))


# Searching title info on webpage
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://yahoo.com")
    print(page.title())
    browser.close()

# Taking snap shot of the webpage
with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    page.goto("http://jhnwr.com")
    page.screenshot(path="images/example.png")
    browser.close()
