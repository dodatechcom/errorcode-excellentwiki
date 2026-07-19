---
title: "[Solution] npm WARN Circular Dependency — Module Loop Fix"
description: "Fix npm circular dependency warnings. Restructure modules to break the dependency cycle."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# npm Circular Dependency

```
npm WARN circular dependency detected:
a → b → c → a
```

## Fix

1. Extract shared code to a third module
2. Use dependency injection
3. Lazy-load the circular dependency

```javascript
// Instead of direct import, use lazy require
let dep;
function getDep() {
  if (!dep) dep = require('./circular-dep');
  return dep;
}
```
