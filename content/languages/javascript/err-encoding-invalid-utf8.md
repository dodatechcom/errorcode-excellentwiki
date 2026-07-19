---
title: "[Solution] ERR_ENCODING_INVALID_UTF8 — Invalid UTF-8 Sequence Fix"
description: "Fix ERR_ENCODING_INVALID_UTF8 when encountering invalid UTF-8 byte sequences in Node.js."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_ENCODING_INVALID_UTF8

```javascript
const buf = Buffer.from([0xFF, 0xFE]);
buf.toString('utf8'); // may error or produce replacement chars

// Fix — handle errors
try {
  const text = buf.toString('utf8');
} catch (err) {
  // Use latin1 as fallback
  const text = buf.toString('latin1');
}
```
