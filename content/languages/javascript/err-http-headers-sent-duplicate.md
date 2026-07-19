---
title: "[Solution] ERR_HTTP_HEADERS_SENT — Headers Already Sent Fix"
description: "Fix ERR_HTTP_HEADERS_SENT when trying to set headers after they've already been sent in Node.js HTTP response."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_HTTP_HEADERS_SENT — Duplicate Headers

Headers were set after `response.writeHead()` or after data was sent.

```javascript
// Wrong
res.writeHead(200);
res.writeHead(404); // ERR_HTTP_HEADERS_SENT

// Fix — check if headers sent
if (!res.headersSent) {
  res.writeHead(200);
}
```

## Pattern

```javascript
app.use((err, req, res, next) => {
  if (res.headersSent) return next(err);
  res.status(500).json({ error: err.message });
});
```
