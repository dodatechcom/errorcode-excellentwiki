---
title: "[Solution] Deprecated Function Migration: urllib/urllib2 to requests"
description: "Migrate from deprecated urllib/urllib2 to the requests library in Python for simpler HTTP requests."
deprecated_function: "urllib/urllib2"
replacement_function: "requests"
languages: ["python"]
deprecated_since: "Python 3.0"
---

# [Solution] Deprecated Function Migration: urllib/urllib2 to requests

The `urllib/urllib2` has been deprecated in favor of `requests`.

## Migration Guide

Python's urllib and urllib2 are cumbersome and low-level. The requests library provides a human-friendly API. Install: pip install requests

## Before (Deprecated)

```python
import urllib2
import urllib

response = urllib2.urlopen("https://api.example.com/data")
data = response.read()

params = urllib.urlencode({"key": "value"})
req = urllib2.Request("https://api.example.com/post", data=params)
response = urllib2.urlopen(req)
```

## After (Modern)

```python
import requests

response = requests.get("https://api.example.com/data")
data = response.json()

response = requests.post("https://api.example.com/post", json={"key": "value"})

try:
    response.raise_for_status()
except requests.HTTPError as e:
    print(e.response.status_code)
```

## Key Differences

- requests.get/post/put/delete replace urllib2.Request + urlopen
- response.json() parses JSON automatically
- raise_for_status() raises exception for 4xx/5xx
- Session objects persist cookies
