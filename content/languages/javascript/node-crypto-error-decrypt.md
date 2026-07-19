---
title: "[Solution] Node.js crypto.decrypt Error — Decryption Failed Fix"
description: "Fix crypto.decrypt errors in Node.js. Handle invalid key, wrong algorithm, and corrupted ciphertext."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Node.js crypto.decrypt Error

```javascript
const crypto = require('crypto');

try {
  const decipher = crypto.createDecipheriv('aes-256-cbc', key, iv);
  let decrypted = decipher.update(encrypted, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
} catch (err) {
  // Wrong key, wrong algorithm, or corrupted data
  console.error('Decryption failed:', err.message);
}
```

## Common Causes

- Wrong key or IV
- Algorithm mismatch with encryption
- Data corrupted during transmission
