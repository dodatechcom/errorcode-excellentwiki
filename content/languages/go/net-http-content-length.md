---
title: "[Solution] Go net/http: Content-Length mismatch — Network Error Fix"
description: "Fix Go Content-Length mismatch error."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# net/http: Content-Length mismatch

The error `net/http: response.ContentLength of X, with Body length Y` occurs when declared and actual lengths differ.

## How to Fix

### Fix 1: Don't set Content-Length manually

```go
// Let Go handle Content-Length automatically
resp, err := http.Post(url, "application/json", bytes.NewReader(data))
```

## Related Errors

- [io-eof]({{< relref "/languages/go/io-eof" >}}) — end of file.
- [unexpected-eof]({{< relref "/languages/go/unexpected-eof" >}}) — unexpected EOF.
