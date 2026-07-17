---
title: "[Solution] Ruby Capybara Test Error Fix"
description: "Fix Capybara test errors in Rails. Learn why Capybara tests fail and how to configure integration tests properly."
languages: ["ruby"]
severities: ["error"]
error-types: ["test-error"]
tags: ["capybara", "integration-test", "testing", "rails", "ruby"]
weight: 5
---

## What This Error Means

A Capybara test error occurs when integration tests using Capybara fail due to timing issues, element not found, or driver configuration problems. Capybara waits for elements by default but can timeout if elements never appear.

## Common Causes

- Element not found within timeout
- JavaScript not executing
- Wrong test driver configured
- Asynchronous operations not awaited

## How to Fix

```ruby
# WRONG: Element not found immediately
expect(page).to have_css("#dynamic-content")  # Timeout if JS slow

# CORRECT: Capybara waits automatically (default 2s)
# Increase timeout for slow operations
Capybara.default_max_wait_time = 5
expect(page).to have_css("#dynamic-content")
```

```ruby
# WRONG: Testing JavaScript without JS driver
visit "/page"
click_button "Submit"  # No JS execution in default driver

# CORRECT: Use JavaScript driver
describe "JavaScript features", js: true do
  it "submits form" do
    visit "/page"
    click_button "Submit"
    expect(page).to have_content("Submitted")
  end
end
```

```ruby
# WRONG: Using wrong matcher
expect(page).to have_selector("button")  # Too broad

# CORRECT: Be specific
expect(page).to have_button("Submit")
expect(page).to have_link("Home", href: "/")
```

## Examples

```ruby
# Example 1: Basic Capybara test
feature "Homepage" do
  scenario "shows welcome message" do
    visit root_path
    expect(page).to have_content("Welcome")
  end
end

# Example 2: Fill in form
fill_in "Email", with: "test@example.com"
fill_in "Password", with: "password"
click_button "Sign in"

# Example 3: Handle modal
click_button "Open Modal"
within(".modal") do
  click_button "Confirm"
end
```

## Related Errors

- [RSpec expectation failed](rspec-error) — test assertion failure
- [Selenium::WebDriver error](selenium-error-ruby) — WebDriver error
- [ActionView::MissingTemplate](rails-template) — template not found
