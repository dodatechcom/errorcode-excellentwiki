---
title: "[Solution] ENOTDIR — Not a Directory Error in Node.js"
description: "Fix ENOTDIR when a path component is not a directory. Check path construction and ensure correct path separators."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ENOTDIR — Not a Directory

A path component was expected to be a directory but is actually a file.

```javascript
const path = require('path');
const fs = require('fs');

// If 'config' is a file, not a directory:
fs.readdirSync('config/other'); // ENOTDIR
```

## Fix

Verify path components before operations.
