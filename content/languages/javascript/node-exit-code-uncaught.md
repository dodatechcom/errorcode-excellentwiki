---
title: "[Solution] Node.js Exit Code on Uncaught Error — process.exitCode Fix"
description: "Fix process exiting with code 1 on uncaught errors. Set exitCode and handle graceful shutdown."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Node.js Exit Code on Error

```javascript
// Instead of process.exit(1) — which skips pending I/O
process.exitCode = 1;

process.on('uncaughtException', (err) => {
  console.error(err);
  process.exitCode = 1;
  // Allow time for logging/flushing
  setTimeout(() => process.exit(), 1000);
});
```

Exit codes:
- 0: Success
- 1: Uncaught fatal exception
- 2: Fatal error (shell usage)
- 89+: Signal received
