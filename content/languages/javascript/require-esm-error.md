---
title: "[Solution] ERR_REQUIRE_ESM — Cannot Load ES Module with require()"
description: "Fix ERR_REQUIRE_ESM when trying to require() an ES module package. Use dynamic import() or upgrade Node.js."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_REQUIRE_ESM — Cannot Load ES Module

You cannot `require()` an ES module. Node.js throws `ERR_REQUIRE_ESM` when a CommonJS script tries to require a package that uses `"type": "module"`.

## Fix

### Option 1: Use dynamic import()

```javascript
const mod = await import('package-name');
```

### Option 2: Use createRequire

```javascript
import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const pkg = require('package-name');
```
