---
title: "Flask-Limiter Rate Limit Error"
description: "Flask-Limiter raises 429 Too Many Requests when rate limits are exceeded"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["limiter", "rate-limit", "throttle", "429", "flask"]
weight: 5
---

## What This Error Means

Flask-Limiter errors occur when a client exceeds the configured rate limit for an endpoint. The extension returns a `429 Too Many Requests` response with a `Retry-After` header indicating when the client can retry.

## Common Causes

- Client sending too many requests within the time window
- Rate limit configured too restrictively
- Missing rate limit key (IP, user ID, API key)
- Storage backend (Redis) not available for distributed limiting
- Rate limit decorators not applied to all relevant routes

## How to Fix

Configure Flask-Limiter:

```python
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="redis://localhost:6379"
)
```

Apply rate limits to routes:

```python
@app.route('/api/data')
@limiter.limit("10 per minute")
def get_data():
    return jsonify({'data': 'value'})

@app.route('/api/upload')
@limiter.limit("5 per hour")
def upload():
    return jsonify({'status': 'uploaded'})
```

Handle rate limit exceeded responses:

```python
from flask_limiter.errors import RateLimitExceeded

@app.errorhandler(RateLimitExceeded)
def rate_limit_exceeded(e):
    return jsonify({
        'error': 'Rate limit exceeded',
        'message': str(e.description)
    }), 429
```

Use different limits per route:

```python
@app.route('/api/public')
@limiter.limit("100 per hour")
def public_api():
    return jsonify({'public': True})

@app.route('/api/admin')
@limiter.limit("10 per minute")
@login_required
def admin_api():
    return jsonify({'admin': True})
```

## Examples

```python
@app.route('/api/send')
@limiter.limit("3 per minute")
def send():
    return jsonify({'status': 'sent'})
```

```text
429 Too Many Requests: You have exceeded the rate limit. Please try again in 45 seconds.
```

## Related Errors

- [RESTful API error]({{< relref "/frameworks/flask/flask-restful-error" >}})
- [CORS error]({{< relref "/frameworks/flask/flask-cors-error" >}})
