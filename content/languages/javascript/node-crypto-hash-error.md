---
title: "[Solution] Node.js crypto Hash Error — Algorithm Not Supported Fix"
description: "Fix crypto hash errors when using unsupported algorithms or invalid data in Node.js."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Node.js crypto Hash Error

```javascript
const crypto = require('crypto');

try {
  // Supported: md5, sha1, sha256, sha384, sha512, etc.
  const hash = crypto.createHash('unsupported-algo');
} catch (err) {
  console.error('Hash error:', err.message);
}
```

```javascript
// Verify algorithm is in crypto.getHashes()
console.log(crypto.getHashes());
```
