---
title: "[Solution] ReferenceError require is not defined — Node.js Module Fix"
description: "Fix ReferenceError: require is not defined when using CommonJS require() in browser or ESM."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ReferenceError: require is not defined

```javascript
// Browser doesn't have require()
const fs = require('fs'); // ReferenceError

// Fix — use ES modules
import fs from 'fs';

// Or bundle with webpack/rollup
```
