---
title: "[Solution] Ruby Selenium::WebDriver Error Fix"
description: "Fix Selenium::WebDriver errors in Ruby. Learn why WebDriver commands fail and how to configure browser automation properly."
languages: ["ruby"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

## What This Error Means

A Selenium::WebDriver error occurs when the WebDriver cannot execute browser automation commands. This can happen due to browser configuration issues, element not found, or session problems.

## Common Causes

- WebDriver binary not installed or wrong version
- Browser not found on system
- Element not found in DOM
- Session timeout or stale element

## How to Fix

```ruby
# WRONG: WebDriver not configured
driver = Selenium::WebDriver.for(:firefox)  # Error if geckodriver not installed

# CORRECT: Install and configure WebDriver
# $ gem install selenium-webdriver
# Download geckodriver for Firefox or chromedriver for Chrome
Selenium::WebDriver::Chrome::Service.driver_path = "/path/to/chromedriver"
```

```ruby
# WRONG: Element not found
element = driver.find_element(:id, "nonexistent")  # NoSuchElementError

# CORRECT: Wait for element
wait = Selenium::WebDriver::Wait.new(timeout: 10)
element = wait.until { driver.find_element(:id, "dynamic-element") }
```

```ruby
# WRONG: Stale element reference
element = driver.find_element(:id, "button")
driver.navigate.refresh
element.click  # StaleElementReferenceError

# CORRECT: Re-find element after navigation
driver.navigate.refresh
element = driver.find_element(:id, "button")
element.click
```

## Examples

```ruby
# Example 1: Basic Selenium usage
require 'selenium-webdriver'
driver = Selenium::WebDriver.for :chrome
driver.get "https://example.com"
puts driver.title

# Example 2: Handle alerts
alert = driver.switch_to.alert
alert.accept

# Example 3: Quit driver
driver.quit
```

## Related Errors

- [Capybara test error](capybara-error) — test framework error
- [Mechanize connection error](mechanize-error) — HTTP request failed
- [LoadError](loaderror-ruby) — cannot load such file
