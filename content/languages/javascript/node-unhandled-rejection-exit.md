---
title: "[Solution] Node.js Unhandled Rejection Exits Process — Default Behavior Fix"
description: "Fix Node.js exiting on unhandled promise rejection. Handle rejections gracefully to prevent process termination."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Unhandled Rejection Process Exit

Node.js exits on unhandled rejections by default.

```javascript
// Prevent crash (but still log)
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection:', reason);
});

// Modern approach — use .catch()
await riskyOperation().catch(err => {
  console.error('Handled:', err);
});
```
