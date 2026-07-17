---
title: "Flask-CORS Error"
description: "Flask-CORS raises errors when cross-origin resource sharing configuration is incorrect or headers conflict"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Flask-CORS errors occur when the Cross-Origin Resource Sharing configuration is incorrect, causing browsers to block cross-origin requests. These errors manifest as missing CORS headers, preflight failures, or origin mismatch issues.

## Common Causes

- CORS not initialized on the Flask app
- Origin whitelist does not include the requesting domain
- Headers not exposed to the client
- Methods not allowed in preflight requests
- Credentials not enabled for authenticated cross-origin requests

## How to Fix

Initialize Flask-CORS with proper configuration:

```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://myfrontend.com"])
```

Configure CORS for specific routes:

```python
CORS(app, resources={r"/api/*": {"origins": "https://myfrontend.com"}})
```

Allow credentials and specific headers:

```python
CORS(app, origins=["https://myfrontend.com"], supports_credentials=True,
     allow_headers=["Content-Type", "Authorization"])
```

Configure per-route CORS:

```python
from flask_cors import cross_origin

@app.route('/api/data')
@cross_origin(origin='https://myfrontend.com', headers=['Content-Type', 'Authorization'])
def get_data():
    return jsonify({'data': 'value'})
```

## Examples

```python
app = Flask(__name__)
# Missing: CORS(app)

@app.route('/api/data')
def data():
    return jsonify({'value': 42})
```

```text
Access to XMLHttpRequest at 'http://localhost:5000/api/data' from origin
'http://localhost:3000' has been blocked by CORS policy
```

## Related Errors

- [RESTful API error]({{< relref "/frameworks/flask/flask-restful-error" >}})
- [Configuration error]({{< relref "/frameworks/flask/config-error" >}})
