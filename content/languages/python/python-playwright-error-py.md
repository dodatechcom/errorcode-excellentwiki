---
title: "[Solution] Python Playwright Browser Automation Error — How to Fix"
description: "Fix Python Playwright browser automation errors. Resolve navigation failures, element timeouts, and browser context issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python Playwright Browser Automation Error

A `playwright._impl._errors.Error` or `TimeoutError` occurs when Playwright fails to navigate to a URL, locate elements within the timeout, or when browser contexts are misconfigured.

## Why It Happens

Playwright automates browsers with auto-waiting and web-first assertions. Errors arise when selectors do not match any elements, when navigation times out due to slow responses, when browser contexts lack required permissions, or when pages have not finished loading.

## Common Error Messages

- `TimeoutError: Timeout 30000ms exceeded during page.goto`
- `Error: locator.click: Target page closed`
- `Error: page.waitForSelector: Timeout 30000ms exceeded`
- `Error: Navigation failed because page was closed`

## How to Fix It

### Fix 1: Use proper selectors and auto-waiting

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")

    # Use specific locator with auto-wait
    page.locator("button.primary").click()

    # Wait for navigation
    with page.expect_navigation():
        page.locator("a.next-page").click()

    browser.close()
```

### Fix 2: Handle timeouts explicitly

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(timeout=60000)

    # Set per-operation timeout
    page.goto("https://example.com", timeout=30000)

    # Use expect for reliable element waiting
    page.locator("#content").wait_for(state="visible", timeout=10000)

    # Retry with custom timeout
    try:
        page.locator("button.submit").click(timeout=5000)
    except TimeoutError:
        page.locator("button.submit").scroll_into_view_if_needed()
        page.locator("button.submit").click()

    browser.close()
```

### Fix 3: Manage browser contexts correctly

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()

    # Create isolated context for each test
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        user_agent="Mozilla/5.0 Custom",
        locale="en-US",
    )
    page = context.new_page()

    # Add authentication
    page.goto("https://example.com/login")
    page.fill("#username", "user")
    page.fill("#password", "pass")
    page.locator("button.login").click()

    # Use storage state for reuse
    context.storage_state(path="state.json")
    context.close()

    # Reuse authentication
    new_context = browser.new_context(storage_state="state.json")
    new_page = new_context.new_page()

    browser.close()
```

### Fix 4: Handle network and page events

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    # Intercept network requests
    def handle_route(route):
        if "analytics" in route.request.url:
            route.abort()
        else:
            route.continue_()

    page.route("**/*", handle_route)

    # Handle dialogs
    page.on("dialog", lambda dialog: dialog.accept())

    # Handle page crashes
    page.on("crash", lambda: print("Page crashed"))

    page.goto("https://example.com")
    page.locator("button.action").click()

    browser.close()
```

## Common Scenarios

- **Element not found** — The page uses dynamic rendering and the element is not yet in the DOM when the selector runs.
- **Navigation timeout** — The target page takes longer than the configured timeout to load.
- **Context closed** — The browser context or page is closed while an operation is still in progress.

## Prevent It

- Always use `locator()` instead of deprecated `find_element()` methods for better auto-waiting behavior.
- Set appropriate timeouts at both the browser context and individual operation levels.
- Use `page.wait_for_load_state("networkidle")` after navigation to ensure all resources are loaded.

## Related Errors

- [TimeoutError](/languages/python/timeouterror/) — operation timed out
- [PlaywrightError](/languages/python/selenium-error/) — browser automation failure
- [ConnectionError](/languages/python/connectionerror/) — browser connection lost
