import requests
from bs4 import BeautifulSoup
import time

with open("file.html", "r", encoding="utf-8") as f:
    pg_1 = f.read()

soup = BeautifulSoup(pg_1, "html.parser")

forms = soup.select("div.fix-table form")

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://google.com",
    "Origin": "https://fojik.site/"
}

for form in forms:

    action_url = form.get("action")
    fu_val = form.find("input", {"name": "FU"}).get("value")
    fn_val = form.find("input", {"name": "FN"}).get("value")

    print(f"\nProcessing: {fn_val}")

    payload = {
        "FU": fu_val,
        "FN": fn_val
    }

    try:
        # First POST
        response = session.post(action_url, data=payload, headers=headers)

        soup1 = BeautifulSoup(response.text, "html.parser")
        verify_form = soup1.find("form", id="verifying-source")


        if not verify_form:
            print("First verification form not found.")
            continue

        sharelink = verify_form["action"]
        print("Share Link:", sharelink)

        # Open Share Link
        response2 = session.get(sharelink, headers=headers)
        print(response2.status_code)
        print(response2.url)
        print(response2.text[:1000])
        soup2 = BeautifulSoup(response2.text, "html.parser")
        verify_form2 = soup2.find("form", id="verifying-source")


        if not verify_form2:
            print("Second verification form not found.")
            continue

        next_action = verify_form2["action"]
        fu2 = verify_form2.find("input", {"name": "FU2"})["value"]

        print("Next Action:", next_action)

        # Submit second form
        response3 = session.post(
            next_action,
            data={"FU2": fu2},
            headers=headers
        )
        print(response3.status_code)
        print(response3.text[:1500])

        print("Final URL:", response3.url)


    except Exception as e:
        print("Error:", e)

    print("-" * 60)
    time.sleep(2)