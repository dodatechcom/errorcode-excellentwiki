---
title: "[Solution] Async/Await Unhandled Error — Missing Try-Catch Fix"
description: "Fix unhandled errors when using async/await without proper try-catch blocks. Handle errors in async functions."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Async/Await Unhandled Errors

```javascript
// BUG — no error handling
async function fetchData() {
  const res = await fetch('/api');
  const data = await res.json();
  return data;
}

// Fix
async function fetchData() {
  try {
    const res = await fetch('/api');
    if (!res.ok) throw new Error(res.statusText);
    return await res.json();
  } catch (err) {
    console.error('Fetch failed:', err);
    throw err;
  }
}
```
