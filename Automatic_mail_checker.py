from playwright.sync_api import  sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        storage_state="playwright/.auth/storage_state.json"
    )
    page = context.new_page()

    page.goto("https://mail.google.com")


    unread_emails = []

# Each email row
    rows = page.locator("tr.zA")

    for i in range(rows.count()):
        row = rows.nth(i)

    # UNREAD emails have span.zF (sender)
        if row.locator("span.zF").count() > 0:
            subject = row.locator("span.bqe").first.inner_text()
            preview = row.locator("span.y2").first.inner_text()

            unread_emails.append({
                "subject": subject,
                "preview": preview
        })

    print(f"\nUnread Emails Count: {len(unread_emails)}\n")

    for idx, email in enumerate(unread_emails, start=1):
        print(f"{idx}. {email['subject']}")
        print(f"   Preview: {email['preview']}\n")

    browser.close()

