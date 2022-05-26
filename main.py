from playwright.sync_api import sync_playwright
import json

# url_test = "https://www.fl.ru/projects/#/"
# url_test = "https://media.5ka.ru/special_offers"
# url_test = "https://www.championat.com/stat/football/#2022-05-26"
# url_test = "https://www.championat.com/stat/tournament/search/"
url_test = "https://adidas.com/terrex"


def test_json(response, results):
    try:
        results.append(
            {
                'url': response.url,
                'data': response.json(),
            }
        )
    except:
        pass


def run(playwright):
    results = []
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    page = browser.new_page()

    # Subscribe to "request" and "response" events
    # page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: test_json(response, results))
    page.goto(url_test)
    browser.close()
    return results


with sync_playwright() as playwright:
    data = run(playwright)
    with open('results.json5', 'w') as f:
        json.dump(data, f)


