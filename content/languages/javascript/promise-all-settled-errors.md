---
title: "[Solution] Promise.allSettled — Handling Individual Rejection Errors"
description: "Fix issues with Promise.allSettled when handling rejected promises. Check status property and extract rejection reasons."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Promise.allSettled Error Handling

```javascript
const results = await Promise.allSettled([
  fetch('/api/a'),
  fetch('/api/b'),
  fetch('/api/c'),
]);

// Check each result
results.forEach((result, i) => {
  if (result.status === 'rejected') {
    console.error(`Request ${i} failed:`, result.reason);
  } else {
    console.log(`Request ${i} succeeded:`, result.value);
  }
});
```
