---
title: "[Solution] DEP0040 — Deprecation Warning: domain Module"
description: "Fix DEP0040 deprecation warning. Replace domain module with async_hooks or proper error handling."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# DEP0040 — domain Module Deprecated

The `domain` module is deprecated.

## Migration

Replace domains with:
1. `try/catch` with async/await
2. `process.on('uncaughtException')`
3. `async_hooks` for context tracking

```javascript
// Instead of domain
try {
  await asyncOperation();
} catch (err) {
  console.error('Caught:', err);
}
```
