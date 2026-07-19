---
title: "[Solution] DEP0128 — Deprecation: Modules._findLookup Fix"
description: "Fix DEP0128 deprecation warning related to module loading internals."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# DEP0128 — Module Lookup Deprecation

This deprecation relates to internal module loading changes.

## Fix

Ensure you're using standard module resolution:

```javascript
// Use require.resolve for path checking
const modulePath = require.resolve('./my-module');
```
