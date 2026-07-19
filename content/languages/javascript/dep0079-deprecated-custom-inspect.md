---
title: "[Solution] DEP0079 — Deprecation Warning: Custom inspection Symbol"
description: "Fix DEP0079 deprecation warning for custom inspect Symbol. Use util.inspect.custom instead."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# DEP0079 — Custom Inspect Symbol Deprecated

## Fix

```javascript
// Deprecated
obj[require('util').inspect.custom] = function() { ... };

// Correct
const { inspect } = require('util');
obj[inspect.custom] = function() {
  return { name: this.name, type: this.type };
};
```
