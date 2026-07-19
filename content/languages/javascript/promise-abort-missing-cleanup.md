---
title: "[Solution] Promise Abort — Cleanup After Promise Cancellation Fix"
description: "Fix memory leaks and dangling promises when aborting promises. Clean up resources after abort signals."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Promise Abort Cleanup

```javascript
async function loadData(signal) {
  const controller = new AbortController();
  const combined = AbortSignal.any([signal, controller.signal]);

  try {
    const res = await fetch('/api', { signal: combined });
    return await res.json();
  } catch (err) {
    if (err.name === 'AbortError') {
      console.log('Request cancelled');
      // Clean up resources here
    }
    throw err;
  }
}
```
