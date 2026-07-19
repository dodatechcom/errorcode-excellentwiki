---
title: "[Solution] Fetch Invalid Content-Type — Response Body Parsing Error"
description: "Fix errors when parsing fetch response with wrong Content-Type. Check response.ok and parse based on content type."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Invalid Content-Type Response

```javascript
// BUG — parsing HTML as JSON
const res = await fetch('/login');
const data = await res.json(); // Unexpected token '<' in JSON

// Fix — check status and content type
const res = await fetch('/api');
if (!res.ok) throw new Error(`HTTP ${res.status}`);
const contentType = res.headers.get('content-type');
if (contentType?.includes('application/json')) {
  return await res.json();
} else {
  return await res.text();
}
```
