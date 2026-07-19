---
title: "[Solution] DEP0106 — Deprecation Warning: url.parse() Fix"
description: "Fix DEP0106 deprecation warning for url.parse(). Migrate to the WHATWG URL API."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# DEP0106 — url.parse() Deprecated

```javascript
// Deprecated
const url = require('url');
const parsed = url.parse('https://example.com/path?q=1');

// Modern
const parsed = new URL('https://example.com/path?q=1');
console.log(parsed.hostname);  // example.com
console.log(parsed.pathname); // /path
console.log(parsed.searchParams.get('q')); // 1
```
