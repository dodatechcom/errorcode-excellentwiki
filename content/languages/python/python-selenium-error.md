---
title: "[Solution] Python Selenium Error — WebDriver Automation Failures"
description: "Fix Python Selenium errors like NoSuchElementException, timeout, StaleElementReference, and session errors. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 422
---

# Python Selenium Error — WebDriver Automation Failures

Selenium errors arise when WebDriver cannot locate elements, encounters stale references, times out waiting for conditions, or loses its browser session. These are common in browser automation and testing.

## Common Causes

```python
# NoSuchElementException: element not found on page
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
driver.find_element("id", "nonexistent")

# TimeoutException: waiting for an element that never appears
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 5)
wait.until(EC.element_to_be_clickable((By.ID, "missing-button")))

# StaleElementReferenceException: element no longer in DOM
element = driver.find_element("id", "dynamic-item")
driver.refresh()
element.click()  # element reference is stale

# WebDriverException: browser session lost
driver.quit()
driver.find_element("tag name", "body")  # session already closed

# InvalidArgumentException: invalid locator
driver.find_element("css selector", "")
```

## How to Fix

### Fix 1: Use Explicit Waits Before Element Access
Wait for the element to exist in the DOM before interacting with it.
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "dynamic-item")))
element.click()
```

### Fix 2: Re-find Stale Elements
Re-locate the element after DOM changes instead of reusing old references.
```python
from selenium.webdriver.common.by import By

def click_element(driver, locator):
    element = driver.find_element(*locator)
    element.click()

driver.refresh()
click_element(driver, (By.ID, "dynamic-item"))
```

### Fix 3: Verify Browser Session Is Active
Always check the driver session before performing actions.
```python
if driver.session_id:
    driver.find_element("tag name", "body")
else:
    driver = webdriver.Chrome()
    driver.get("https://example.com")
```

### Fix 4: Use Multiple Locator Strategies
Fall back to alternative locators if the primary one fails.
```python
from selenium.webdriver.common.by import By

try:
    element = driver.find_element(By.ID, "submit-btn")
except:
    element = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
element.click()
```

### Fix 5: Handle iframe Contexts
Switch to an iframe before accessing elements inside it.
```python
from selenium.webdriver.common.by import By

driver.switch_to.frame("iframe-name")
element = driver.find_element(By.ID, "inside-iframe")
driver.switch_to.default_content()
```

## Examples

```python
# Full page automation with waits
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com/login")

username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username.send_keys("user@example.com")

password = driver.find_element(By.NAME, "password")
password.send_keys("securepassword")

submit = wait.until(EC.element_to_be_clickable((By.ID, "login-btn")))
submit.click()
```

## Related Errors

- [Python Requests Error](/languages/python/python-requests-error/)
- [Python httpx Error](/languages/python/python-httpx-error/)
- [Python Scrapy Error](/languages/python/python-scrapy-error/)
