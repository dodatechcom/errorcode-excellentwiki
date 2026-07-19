---
title: "[Solution] IndexedDB Version Error — Upgrade Blocked Fix"
description: "Fix IndexedDB version change error when onupgradeneeded fails or version mismatch occurs."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# IndexedDB Version Error

```javascript
const request = indexedDB.open('myDB', 2);

request.onupgradeneeded = (e) => {
  const db = e.target.result;
  // Handle schema migration carefully
  if (!db.objectStoreNames.contains('users')) {
    db.createObjectStore('users', { keyPath: 'id' });
  }
};

request.onerror = (e) => {
  console.error('Version error:', e.target.error);
};
```
