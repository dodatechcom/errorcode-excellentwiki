---
title: "[Solution] AbortError Fetch Aborted — Request Cancellation Fix"
description: "Fix AbortError when a fetch request is aborted via AbortController. Handle gracefully in catch blocks."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# AbortError on Fetch

```javascript
const controller = new AbortController();

// Abort after 5 seconds
const timeout = setTimeout(() => controller.abort(), 5000);

try {
  const res = await fetch('/api', { signal: controller.signal });
  clearTimeout(timeout);
  return await res.json();
} catch (err) {
  clearTimeout(timeout);
  if (err.name === 'AbortError') {
    console.log('Request timed out');
  }
  throw err;
}
```
