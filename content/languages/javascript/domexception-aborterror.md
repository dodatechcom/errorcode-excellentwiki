---
title: "[Solution] DOMException AbortError — User Aborted Request Fix"
description: "Fix DOMException AbortError when users cancel operations. Handle the AbortController abort signal properly."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# DOMException AbortError

```javascript
try {
  const controller = new AbortController();
  document.addEventListener('click', () => controller.abort(), { once: true });
  await fetch('/long-request', { signal: controller.signal });
} catch (err) {
  if (err instanceof DOMException && err.name === 'AbortError') {
    console.log('User cancelled');
  }
}
```
