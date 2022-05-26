from playwright.sync_api import sync_playwright
from datetime import datetime

dt = datetime.today()
seconds = dt.timestamp()
print(round(seconds))

url_test = "https://ria.ru/"

# Taking snap shot of the web page
with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    page.goto(url_test)
    page.screenshot(path=f"images/example-{seconds}.png")
    browser.close()

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()

    # Subscribe to "request" and "response" events
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.url, response.body))
    page.goto(url_test)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
