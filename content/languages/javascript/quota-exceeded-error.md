---
title: "[Solution] QuotaExceededError — Storage Limit Exceeded Fix"
description: "Fix QuotaExceededError when localStorage, sessionStorage, or IndexedDB storage quota is exceeded."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# QuotaExceededError

```javascript
try {
  localStorage.setItem('data', largeString);
} catch (err) {
  if (err.name === 'QuotaExceededError') {
    // Clean up old data
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      if (key.startsWith('cache_')) localStorage.removeItem(key);
    }
  }
}
```

## Check Quota

```javascript
if (navigator.storage && navigator.storage.estimate) {
  const { usage, quota } = await navigator.storage.estimate();
  console.log(`Using ${usage} of ${quota} bytes`);
}
```
