---
title: "[Solution] ERR_NO_CWD — Cannot Access Current Working Directory"
description: "Fix ERR_NO_CWD when Node.js cannot access the current working directory."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# ERR_NO_CWD — Cannot Access CWD

```javascript
// Check if CWD is accessible
try {
  process.cwd();
} catch (err) {
  console.error('Cannot access CWD:', err.message);
  // Set a fallback directory
  process.chdir('/tmp');
}
```

## Causes

- Directory was deleted while process is running
- Permission revoked
- NFS mount disconnected
