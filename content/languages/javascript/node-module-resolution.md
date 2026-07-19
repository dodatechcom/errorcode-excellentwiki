---
title: "[Solution] Node.js Module Resolution Algorithm — How require() Finds Modules"
description: "Understand how Node.js resolves module paths with require(). Learn the resolution algorithm, node_modules lookup, and CORE_MODULES."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Node.js Module Resolution

Node.js resolves modules using a specific algorithm:

1. **Core modules** (fs, path, http) — loaded from built-in
2. **node_modules** — walks up the directory tree
3. **Relative paths** — resolves from current file
4. **NODE_PATH** environment variable

## Troubleshooting

```javascript
// Debug resolution
console.log(require.resolve('my-module'));

// Check which module is loaded
console.log(module.paths);
```
