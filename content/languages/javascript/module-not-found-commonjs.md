---
title: "[Solution] Node.js Module Not Found — CommonJS require() Fix"
description: "Fix Node.js Module not found errors when using require(). Check paths, file extensions, and package installation."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Module Not Found — CommonJS require() Fix

The `Module not found` error occurs when Node.js cannot resolve a module path passed to `require()`.

## Common Causes

- Module is not installed in `node_modules`
- Incorrect relative path (missing `./` prefix)
- Wrong file extension
- Case mismatch on case-sensitive filesystems

```javascript
// Wrong — missing ./ prefix
const utils = require('utils');

// Correct
const utils = require('./utils');
```

## Fix

```bash
npm install <package-name>
```

If using a local file, verify the path resolves correctly:

```javascript
const path = require('path');
const resolved = path.resolve(__dirname, './utils');
console.log(resolved);
```
