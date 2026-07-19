---
title: "[Solution] Service Worker Registration Failed — SW Error Fix"
description: "Fix Service Worker registration errors. Ensure correct scope, HTTPS, and handle update conflicts."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Service Worker Registration Error

```javascript
if ('serviceWorker' in navigator) {
  try {
    const reg = await navigator.serviceWorker.register('/sw.js', {
      scope: '/'
    });
    reg.addEventListener('updatefound', () => {
      console.log('New SW installing');
    });
  } catch (err) {
    console.error('SW registration failed:', err);
  }
}
```

## Common Issues

1. Page must be served over HTTPS (or localhost)
2. Scope cannot be above the SW script's directory
3. Multiple pages may conflict on registration
