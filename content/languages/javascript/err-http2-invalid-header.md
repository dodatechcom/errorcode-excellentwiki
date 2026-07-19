---
title: "[Solution] ERR_HTTP2_INVALID_HEADER — HTTP/2 Invalid Header Error Fix"
description: "Fix ERR_HTTP2_INVALID_HEADER when HTTP/2 headers contain invalid characters or empty values."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_HTTP2_INVALID_HEADER

HTTP/2 is strict about headers — no uppercase names, no invalid characters.

## Fix

```javascript
// HTTP/2 requires lowercase header names
// Wrong
headers: { 'Content-Type': 'text/html' }

// Correct
headers: { 'content-type': 'text/html' }
```

All header names must be lowercase in HTTP/2.
