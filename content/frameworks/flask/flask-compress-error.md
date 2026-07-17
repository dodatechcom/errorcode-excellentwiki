---
title: "Flask-Compress Error"
description: "Flask-Compress raises errors when response compression fails or is misconfigured"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

## What This Error Means

Flask-Compress errors occur when response compression fails due to incompatible content types, missing compression libraries, or misconfiguration. These errors can cause responses to be sent uncompressed or with incorrect headers.

## Common Causes

- Compression library (brotli, zlib) not installed
- Content type not included in compressible types list
- Response already compressed (double compression)
- Minimum size threshold not met
- Backend server stripping compression headers

## How to Fix

Configure Flask-Compress:

```python
from flask import Flask
from flask_compress import Compress

app = Flask(__name__)
app.config['COMPRESS_MIMETYPES'] = [
    'text/html', 'text/css', 'text/xml',
    'application/json', 'application/javascript'
]
app.config['COMPRESS_MIN_SIZE'] = 500
app.config['COMPRESS_LEVEL'] = 6  # 1-9, default 6

compress = Compress(app)
```

Ensure compression is applied globally:

```python
compress = Compress()
compress.init_app(app)
```

Handle specific content types:

```python
@app.route('/api/data')
def data():
    response = jsonify({'data': 'large payload here'})
    response.content_type = 'application/json'
    return response  # Automatically compressed
```

Exclude routes from compression:

```python
@app.route('/download')
@compress.except
def download():
    return send_file('large_file.bin')
```

Verify compression headers:

```python
@app.after_request
def check_compression(response):
    if 'Content-Encoding' in response.headers:
        print(f"Response compressed with: {response.headers['Content-Encoding']}")
    return response
```

## Examples

```python
@app.route('/api/large-data')
def large_data():
    return jsonify({'data': 'x' * 10000})
```

```text
ValueError: Unknown compression type: brotli (install flask-compress[brotli])
```

## Related Errors

- [Configuration error]({{< relref "/frameworks/flask/config-error" >}})
- [CORS error]({{< relref "/frameworks/flask/flask-cors-error" >}})
