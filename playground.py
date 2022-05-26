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

# ==================================================================
# Taking snapshots + href from whole webpage

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
    # Taking all the href links from page if used "body"
    page.on("response", lambda response: print("<<", response.url, response.body))
    # Taking all the info from page if put "body()" instead of just "body"
    # page.on("response", lambda response: print("<<", response.url, response.body()))
    page.goto(url_test)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


from playwright.sync_api import sync_playwright
import json

# url_test = "https://www.fl.ru/projects/#/"
# url_test = "https://media.5ka.ru/special_offers"
url_test = "https://www.championat.com/stat/football/#2022-05-26"
# url_test = "https://www.championat.com/stat/tournament/search/"



# def test_json(response, results):
#     try:
#         results.append(
#             {
#                 'url': response.url,
#                 'data': response.json(),
#             }
#         )
#     except:
#         pass
#
#
# def run(playwright):
#     results = []
#     chromium = playwright.chromium
#     browser = chromium.launch()
#     page = browser.new_page()
#
#     # Subscribe to "request" and "response" events
#     # page.on("request", lambda request: print(">>", request.method, request.url))
#     page.on("response", lambda response: test_json(response, results))
#     page.goto(url_test)
#     browser.close()
#     return results
#
#
# with sync_playwright() as playwright:
#     data = run(playwright)
#     with open('results.json5', 'w') as f:
#         json.dump(data, f)

with open('results.json5') as file:
    data = json.load(file)

for item in data[6]['data']['matches']['football']['tournaments']:
    print(item)

print(data[6]['data'])