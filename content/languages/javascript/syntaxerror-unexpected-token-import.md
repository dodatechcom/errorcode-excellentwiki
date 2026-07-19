---
title: "[Solution] SyntaxError Unexpected Token import — ES Module in CommonJS Fix"
description: "Fix SyntaxError: Cannot use import statement in a module. Configure package.json type or use require()."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Unexpected Token import

Using ESM syntax in a CommonJS context.

## Fixes

### Option 1: Add to package.json
```json
{ "type": "module" }
```

### Option 2: Rename file to .mjs
```bash
mv script.js script.mjs
```

### Option 3: Use require()
```javascript
const express = require('express');
```
