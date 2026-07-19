---
title: "[Solution] ERR_MODULE_NOT_FOUND — require.resolve Cannot Find Module Fix"
description: "Fix require.resolve() ERR_MODULE_NOT_FOUND when the module is not installed."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_MODULE_NOT_FOUND — require.resolve

```javascript
try {
  const modulePath = require.resolve('non-existent-package');
} catch (err) {
  // MODULE_NOT_FOUND: Cannot find module 'non-existent-package'
  console.error('Module not installed:', err.message);
}
```

## Fix

```bash
npm install <package-name>
```

Verify the package exists in `package.json` and `node_modules/`.
