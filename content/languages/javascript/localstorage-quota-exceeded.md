---
title: "[Solution] QuotaExceededError localStorage — Storage Full Fix"
description: "Fix QuotaExceededError when localStorage exceeds the 5-10MB limit. Clear old data, use IndexedDB, or compress."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# localStorage QuotaExceededError

```javascript
try {
  localStorage.setItem('key', hugeString);
} catch (err) {
  if (err.name === 'QuotaExceededError') {
    // Clear old data
    localStorage.clear();
    // Or use IndexedDB for large data
  }
}
```

## Better Approach: IndexedDB

```javascript
const request = indexedDB.open('myDB', 1);
request.onupgradeneeded = (e) => {
  e.target.result.createObjectStore('data');
};
```
