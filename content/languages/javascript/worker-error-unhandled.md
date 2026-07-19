---
title: "[Solution] Worker Unhandled Error — Worker Thread Error Handling Fix"
description: "Fix unhandled errors in Web Workers. Add error and message event listeners to worker instances."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Worker Unhandled Error

```javascript
const worker = new Worker('worker.js');

worker.onerror = (e) => {
  console.error('Worker error:', e.message, e.filename, e.lineno);
};

// In worker.js — catch internal errors
self.onerror = (message, source, lineno, colno, error) => {
  self.postMessage({ type: 'error', error: message });
};
```
