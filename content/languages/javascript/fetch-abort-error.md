---
title: "[Solution] Fetch AbortError — Operation Aborted Fix"
description: "Fix AbortError when fetch() is cancelled by AbortController. Handle AbortError gracefully in catch blocks."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Fetch AbortError

```javascript
const controller = new AbortController();
setTimeout(() => controller.abort(), 5000);

try {
  const res = await fetch('/api', { signal: controller.signal });
  const data = await res.json();
} catch (err) {
  if (err.name === 'AbortError') {
    console.log('Request timed out');
  } else {
    throw err;
  }
}
```
