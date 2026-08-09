from pathlib import Path
from playwright.sync_api import sync_playwright

roll = input("Enter Roll Number: ")
reg = input("Enter Registration Number: ")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.educationboardresults.gov.bd/v2/home")

    page.get_by_label("Name of Board").select_option("dhaka")
    page.get_by_label("Name of Examination").select_option("ssc")
    page.get_by_label("Year of Examination").select_option("2018")
    page.get_by_label("Type of Result").select_option("1")

    page.get_by_role("spinbutton", name="Roll Number of Examinee").fill(roll)
    page.get_by_role("spinbutton", name="Registration Number of").fill(reg)

    # Refresh CAPTCHA and wait until it actually changes
    old_src = page.locator("#captcha_img").get_attribute("src")
    page.locator("#captcha_reload").click()

    page.wait_for_function(
        "(old) => document.querySelector('#captcha_img').getAttribute('src') !== old",
        arg=old_src
    )

    # Download the refreshed CAPTCHA image
    captcha_src = page.locator("#captcha_img").get_attribute("src")
    image_bytes = page.context.request.get(
        f"https://www.educationboardresults.gov.bd{captcha_src}"
    ).body()

    with open("captcha.png", "wb") as f:
        f.write(image_bytes)

    print("CAPTCHA saved as captcha.png")
    captcha_text = input("Enter CAPTCHA from captcha.png: ")

    page.get_by_role("spinbutton", name="Robot Prevention Technique (").fill(captcha_text)

    page.get_by_role("button", name="View Result").click()

    # Wait for result
    try:
        page.wait_for_selector(".table-container table", timeout=10000)
    except Exception:
        print("Incorrect CAPTCHA or result not found.")
        browser.close()
        raise SystemExit

    # ---------------- Student Information ----------------
    rows = page.locator(".table-container table").first.locator("tbody tr")
    info = {}

    for i in range(rows.count()):
        cells = rows.nth(i).locator("td")
        values = [cells.nth(j).inner_text().strip() for j in range(cells.count())]

        if len(values) == 4:
            info[values[0]] = values[1]
            info[values[2]] = values[3]
        elif len(values) == 2:
            info[values[0]] = values[1]

    # ---------------- Subject Tables ----------------
    tables = page.locator(".table-container table")

    main_subjects = []
    continuous_subjects = []

    # Main subjects
    main_rows = tables.nth(1).locator("tbody tr")
    for i in range(main_rows.count()):
        tds = main_rows.nth(i).locator("td")
        main_subjects.append({
            "code": tds.nth(0).inner_text().strip(),
            "subject": tds.nth(1).inner_text().strip(),
            "grade": tds.nth(2).inner_text().strip()
        })

    # Continuous assessment subjects
    if tables.count() >= 3:
        ca_rows = tables.nth(2).locator("tbody tr")
        for i in range(ca_rows.count()):
            tds = ca_rows.nth(i).locator("td")
            continuous_subjects.append({
                "code": tds.nth(0).inner_text().strip(),
                "subject": tds.nth(1).inner_text().strip(),
                "grade": tds.nth(2).inner_text().strip()
            })

    # ---------------- Check if all subjects are A+ ----------------
    all_grades = [s["grade"] for s in main_subjects + continuous_subjects]
    all_a_plus = all(g.upper() == "A+" for g in all_grades)

    # ---------------- Pretty Print ----------------
    print("\n" + "=" * 80)
    print("                          SSC RESULT SUMMARY")
    print("=" * 80)

    summary_order = [
        ("Name of Student", "Student"),
        ("Father's Name", "Father"),
        ("Mother's Name", "Mother"),
        ("Roll No", "Roll"),
        ("Registration No", "Registration"),
        ("Board", "Board"),
        ("Session", "Session"),
        ("Group", "Group"),
        ("Result", "Result"),
        ("Date of Birth", "Date of Birth"),
        ("Name of Institute", "Institute"),
    ]

    for key, label in summary_order:
        if key in info:
            print(f"{label:<16}: {info[key]}")

    print("-" * 80)
    print(f"{'Code':<8}{'Subject':<55}{'Grade'}")
    print("-" * 80)

    for s in main_subjects:
        print(f"{s['code']:<8}{s['subject']:<55}{s['grade']}")

    if continuous_subjects:
        print("-" * 80)
        print("Continuous Assessment")
        print("-" * 80)
        for s in continuous_subjects:
            print(f"{s['code']:<8}{s['subject']:<55}{s['grade']}")

    print("=" * 80)

    if all_a_plus:
        print("PERFECT RESULT: Every subject has A+")
    else:
        non_a = [
            f"{s['subject']} ({s['grade']})"
            for s in main_subjects + continuous_subjects
            if s['grade'].upper() != "A+"
        ]
        print("Subjects not A+: " + (", ".join(non_a) if non_a else "None"))

    print("=" * 80)

    # ---------------- Print Result to PDF ----------------
    # ---------------- Print Result to PDF ----------------
    pdf_path = Path(f"SSC_Result_{info.get('Roll No', 'result')}.pdf")

    # Generate PDF directly from the result page
    page.pdf(
        path=str(pdf_path),
        format="A4",
        print_background=True,
        margin={
            "top": "10mm",
            "bottom": "10mm",
            "left": "10mm",
            "right": "10mm"
        }
    )

    print(f"PDF saved: {pdf_path.resolve()}")
    browser.close()

    browser.close()