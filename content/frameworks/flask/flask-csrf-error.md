---
title: "[Solution] Flask CSRF Protection Error"
description: "Fix Flask CSRF protection errors when forms or API requests are rejected by CSRF validation."
frameworks: ["flask"]
error-types: ["security-error"]
severities: ["error"]
---

CSRF protection errors in Flask-WTF occur when the CSRF token is missing, invalid, or the session has been invalidated.

## Common Causes

- CSRF token not included in HTML form
- AJAX request missing CSRF token header
- Session cookie expired or was deleted
- Multiple tabs with different sessions
- CSRF protection enabled on API endpoints that need exemption

## How to Fix

### Include CSRF Token in Forms

```html
<form method="POST" action="/submit">
    {{ form.hidden_tag() }}
    <input type="text" name="data"/>
    <button type="submit">Submit</button>
</form>
```

### Add CSRF Token to JavaScript

```javascript
function getCSRFToken() {
    return document.querySelector('meta[name="csrf-token"]').content;
}

fetch("/api/submit", {
    method: "POST",
    headers: {
        "X-CSRFToken": getCSRFToken(),
        "Content-Type": "application/json",
    },
    body: JSON.stringify({data: "value"}),
});
```

### Exempt API Endpoints

```python
from flask_wtf.csrf import CSRF, csrf_exempt

csrf = CSRF(app)

@app.route("/api/webhook", methods=["POST"])
@csrf_exempt
def webhook():
    return {"status": "ok"}
```

## Examples

```python
from flask import Flask
from flask_wtf.csrf import CSRF

app = Flask(__name__)
csrf = CSRF(app)

# Bug -- CSRF token missing in AJAX
@app.route("/api/data", methods=["POST"])
def api_data():
    return {"status": "ok"}

# Fix -- add CSRF token to headers
# In HTML: <meta name="csrf-token" content="{{ csrf_token() }}">
# In JS: headers["X-CSRFToken"] = document.querySelector('meta[name="csrf-token"]').content
```
