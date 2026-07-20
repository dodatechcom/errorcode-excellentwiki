---
title: "[Solution] Capybara Assertion — Find, Wait, AJAX, Within Scope Errors"
description: "Fix Capybara assertion errors. Handle find failures, AJAX timing, within scope, and waiting for elements."
date: 2026-07-20T10:00:00+08:00
draft: false
language: "ruby"
tags: ["ruby, capybara, assertion, test, selenium"]
severity: "error"
---

# Capybara Assertion Errors

## Error Message

```
Capybara::ElementNotFound: Unable to find css "#element"
# or
Capybara::ExpectationNotMet: expected to find css ".modal" but there were no matches
# or
Selenium::WebDriver::Error::StaleElementReferenceError
```

## Common Causes

- Element not found because AJAX request hasn't completed
- Element is outside the `within` scope
- Element was removed from DOM after finding (stale element)
- Selector doesn't match the actual element

## Solutions

### Solution 1: Use Built-in Waiting and Retrying

Capybara automatically waits for elements — let it handle timing.

```ruby
# Capybara waits up to default_max_wait_time (2 seconds)
expect(page).to have_css("#loaded-content")

# Find with waiting
find("#dynamic-element", wait: 5)

# Check for element absence
expect(page).not_to have_css("#deleted-element")
```

### Solution 2: Use within for Scoped Queries

Limit selectors to a specific DOM element.

```ruby
within("#user-form") do
  fill_in "Name", with: "Alice"
  click_button "Save"
end

within_frame("iframe-id") do
  expect(page).to have_content("Inside iframe")
end

within_window("popup") do
  expect(page).to have_content("Popup content")
end
```

### Solution 3: Handle AJAX with have_css or have_content

Wait for AJAX responses using content expectations.

```ruby
# BAD: check before AJAX completes
click_button "Load"
expect(page).to have_css("#result")  # may fail

# GOOD: Capybara waits automatically
click_button "Load"
expect(page).to have_css("#result", wait: 10)

# Or use have_content for text assertions
click_button "Submit"
expect(page).to have_content("Success message")
```

### Solution 4: Use have_selector for Complex Assertions

Combine multiple element properties in one assertion.

```ruby
# Check element attributes
expect(page).to have_selector("input[name='email']", value: "alice@example.com")

# Check visible elements
expect(page).to have_selector(".alert", text: "Error", visible: true)

# Check element count
expect(page).to have_css(".list-item", count: 5)

# Use have_css with options
expect(page).to have_css("h1", text: "Welcome", id: "title")
```

## Prevention Tips

- Never use `sleep` — Capybara's `wait` mechanism handles AJAX automatically
- Use `have_css` or `have_content` instead of `find` for assertions
- Increase `default_max_wait_time` for slow applications
- Use `visible: true` to ensure elements are actually displayed

## Related Errors

- [Selenium Error]({{< relref "/languages/ruby/selenium-error-ruby" >}})
- [Capybara Error]({{< relref "/languages/ruby/capybara-error" >}})
- [NoMethodError]({{< relref "/languages/ruby/no-method-error" >}})
