---
title: "[Solution] Groovy REST Client"
description: "REST client errors."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy REST Client

REST client errors.

### Common Causes
Wrong method; missing headers; auth

### How to Fix
```groovy
import groovyx.net.http.RESTClient
def client = new RESTClient('https://api.example.com/')
def resp = client.post(
    path: 'users',
    body: [name: 'John'],
    requestContentType: JSON
)
```

### Examples
```groovy
client.headers['Authorization'] = 'Bearer token'
def resp = client.get(path: 'users')
```
