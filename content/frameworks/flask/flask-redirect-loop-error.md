---
title: "[Solution] Flask Redirect Loop Error"
description: "Fix Flask redirect loop errors when requests cycle endlessly between redirect endpoints."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
---

Redirect loops occur when two or more endpoints redirect to each other endlessly, causing the browser to display a "too many redirects" error.

## Common Causes

- Two endpoints redirect to each other
- Login page redirects to itself when authentication check fails
- Middleware redirects to a page that triggers the same middleware
- URL without trailing slash redirects to URL with trailing slash and back
- Authentication decorator redirects to login which redirects back

## How to Fix

### Add Conditional Redirect Logic

```python
from flask import Flask, redirect, request, url_for

app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
    if not is_authenticated():
        # Only redirect if not already on login page
        if request.endpoint != "login":
            return redirect(url_for("login"))
    return "Dashboard"

@app.route("/login")
def login():
    if is_authenticated():
        return redirect(url_for("dashboard"))
    return "Login form"
```

### Use Proper URL Routing

```python
# Avoid duplicate routes that cause loops
@app.route("/home")
@app.route("/home/")
def home():
    return "Home"
```

### Set Maximum Redirect Count

```python
import requests

response = requests.get(url, allow_redirects=False)
if response.status_code in (301, 302):
    print(f"Redirected to: {response.headers['Location']}")
```

## Examples

```python
from flask import Flask, redirect, url_for

app = Flask(__name__)

# Bug -- redirect loop
@app.route("/page-a")
def page_a():
    return redirect(url_for("page_b"))

@app.route("/page-b")
def page_b():
    return redirect(url_for("page_a"))

# Fix -- add condition
@app.route("/page-a-fixed")
def page_a_fixed():
    if needs_redirect():
        return redirect(url_for("page_b_fixed"))
    return "Page A"

@app.route("/page-b-fixed")
def page_b_fixed():
    return "Page B"
```
