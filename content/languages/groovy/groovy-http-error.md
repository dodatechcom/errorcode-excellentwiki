---
title: "[Solution] Groovy HTTP Error"
description: "HTTP client errors (HTTPBuilder)."
languages: ["groovy"]
error-types: ["language-error"]
severities: ["error"]
---

# Groovy HTTP Error

HTTP client errors (HTTPBuilder).

### Common Causes
Wrong URL; auth; timeout

### How to Fix
```groovy
import groovyx.net.http.HTTPBuilder
import static groovyx.net.http.ContentType.*

def http = new HTTPBuilder('https://api.example.com')
http.get(path: '/data') { resp, json ->
    println json
}
```

### Examples
```groovy
import groovyx.net.http.RESTClient

def client = new RESTClient('https://api.example.com/')
def resp = client.get(path: 'data')
```
