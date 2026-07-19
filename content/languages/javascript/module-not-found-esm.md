---
title: "[Solution] ESM Module Not Found — ERR_MODULE_NOT_FOUND Fix"
description: "Fix ERR_MODULE_NOT_FOUND in ES modules. Add file extensions, use import assertions, and check package.json type field."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_MODULE_NOT_FOUND — ES Module Fix

ES modules require explicit file extensions in import paths.

## Common Causes

- Missing `.js` extension in import path
- `package.json` missing `"type": "module"`
- Importing a directory without an `index.js`

```javascript
// Wrong
import { foo } from './utils';

// Correct
import { foo } from './utils.js';
```

## Fix

Ensure your `package.json` has:

```json
{ "type": "module" }
```

And always use full file extensions in relative imports.
