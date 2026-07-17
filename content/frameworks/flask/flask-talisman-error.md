---
title: "Flask-Talisman Security Error"
description: "Flask-Talisman raises errors when Content Security Policy or HTTPS enforcement fails"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["talisman", "security", "csp", "https", "flask"]
weight: 5
---

## What This Error Means

Flask-Talisman errors occur when security headers like Content Security Policy (CSP) are violated, HTTPS enforcement blocks requests, or security configurations conflict with application behavior. These errors can block resources or break functionality.

## Common Causes

- CSP policy blocking inline scripts or styles
- Mixed content (HTTP resources on HTTPS page)
- External CDN not whitelisted in CSP
- HTTPS redirect interfering with API calls
- Strict CSP blocking third-party resources

## How to Fix

Configure Flask-Talisman:

```python
from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
talisman = Talisman(
    app,
    content_security_policy={
        'default-src': "'self'",
        'script-src': "'self' 'unsafe-inline' cdn.jsdelivr.net",
        'style-src': "'self' 'unsafe-inline' fonts.googleapis.com",
        'img-src': "'self' data:",
    },
    content_security_policy_nonce_in=['script-src'],
    force_https=False  # Disable for development
)
```

Use nonce for inline scripts:

```html
<script nonce="{{ csp_nonce() }}">
    console.log('This script is allowed by CSP');
</script>
```

Whitelist external resources:

```python
content_security_policy={
    'default-src': "'self'",
    'script-src': [
        "'self'",
        'https://cdn.jsdelivr.net',
        'https://unpkg.com',
    ],
    'style-src': [
        "'self'",
        'https://fonts.googleapis.com',
    ],
    'font-src': [
        "'self'",
        'https://fonts.gstatic.com',
    ],
}
```

Disable Talisman for specific routes:

```python
@app.route('/api/external')
@talisman(
    content_security_policy={'default-src': "'self' *'},
    force_https=False
)
def external_api():
    return jsonify({'data': 'value'})
```

## Examples

```python
talisman = Talisman(app, force_https=True)
```

```text
flask_talisman.Talisman: Refused to load the script 'https://example.com/script.js'
because it violates the following Content Security Policy directive
```

## Related Errors

- [Configuration error]({{< relref "/frameworks/flask/config-error" >}})
- [CORS error]({{< relref "/frameworks/flask/flask-cors-error" >}})
