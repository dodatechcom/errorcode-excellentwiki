---
title: "[Solution] Unhandled Promise Rejection in Async/Await — Top-Level Error Handling"
description: "Fix unhandled promise rejections when using async/await. Wrap await calls and set up global handlers."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Unhandled Promise Rejection — Async/Await

Even with async/await, unhandled rejections can occur.

## Common Pattern

```javascript
// BUG — missing await
async function getUser() {
  fetchUser();  // unhandled if this rejects
}

// Fix
async function getUser() {
  return await fetchUser();
}
```

## Global Handler

```javascript
process.on('unhandledRejection', (reason, promise) => {
  console.error('Unhandled Rejection:', reason);
});
```
