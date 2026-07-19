---
title: "[Solution] SyntaxError — Import Assertion Syntax Error Fix"
description: "Fix SyntaxError related to import assertions and import attributes syntax in ES modules."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Import Assertion Syntax Error

```javascript
// Old syntax (deprecated)
import data from './data.json' assert { type: 'json' };

// New syntax (import attributes)
import data from './data.json' with { type: 'json' };

// Check browser/Node support
const data = JSON.parse(
  new TextDecoder().decode(
    new Uint8Array(
      (await import('./data.json', { with: { type: 'json' } })).default
    )
  )
);
```
