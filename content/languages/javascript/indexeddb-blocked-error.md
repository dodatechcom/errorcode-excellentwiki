---
title: "[Solution] IndexedDB Blocked — open() Blocked Error Fix"
description: "Fix IndexedDB open() blocked error when database is open in another tab or incognito mode."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# IndexedDB Blocked Error

```javascript
const request = indexedDB.open('myDB', 1);

request.onerror = (e) => {
  console.error('IndexedDB blocked:', e.target.error);
  // Fallback to localStorage or in-memory
};

request.onblocked = () => {
  console.warn('Database blocked — close other tabs');
};
```
