---
title: "[Solution] Warning: Promise Rejection — Node.js Deprecation Warning Fix"
description: "Fix Node.js deprecation warning about promise rejection handling. Migrate to proper rejection handlers."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Node.js Promise Rejection Deprecation

Node.js warns when unhandled promise rejections are not caught.

## Fix

```javascript
// Add to top of entry file
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled rejection:', reason);
});

// In async code, always handle rejections
async function safeOperation() {
  try {
    return await riskyOperation();
  } catch (err) {
    console.error('Caught:', err);
    throw err;
  }
}
```
