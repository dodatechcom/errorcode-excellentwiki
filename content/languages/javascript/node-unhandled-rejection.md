---
title: "Node.js UnhandledPromiseRejectionWarning"
description: "UnhandledPromiseRejectionWarning — Fix unhandled promise rejections in Node.js."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

The `UnhandledPromiseRejectionWarning` occurs when a Promise is rejected but no `.catch()` handler or `await` in a `try/catch` is attached. In Node.js 15+, unhandled rejections crash the process by default.

## Description

Common unhandled rejection messages include:

- `UnhandledPromiseRejectionWarning: Error: something failed` — no catch handler
- `UnhandledPromiseRejectionWarning: [object Object]` — rejected with an object
- `UnhandledPromiseRejectionWarning: TypeError: cannot read property of undefined` — async function throws

## Common Causes

```javascript
// Cause 1: Missing .catch() on promise
fetch("https://api.example.com/data")
  .then((res) => res.json())
  .then((data) => console.log(data));
// No .catch() — network errors become unhandled rejections

// Cause 2: Async function without try/catch
async function getUser(id) {
  const res = await fetch(`/api/users/${id}`);
  return res.json(); // throws if response is not JSON
}

// Cause 3: Fire-and-forget async calls
async function saveData() { /* ... */ }
saveData(); // return value (promise) is ignored

// Cause 4: Event handler throwing in async context
process.on("unhandledRejection", () => {}); // does NOT prevent crash in Node 15+
```

## Solutions

### Fix 1: Add proper error handling

```javascript
// Use .catch() on promise chains
fetch("https://api.example.com/data")
  .then((res) => res.json())
  .then((data) => console.log(data))
  .catch((err) => console.error("Fetch failed:", err.message));

// Use try/catch with async/await
async function fetchData() {
  try {
    const res = await fetch("https://api.example.com/data");
    return await res.json();
  } catch (err) {
    console.error("Fetch failed:", err.message);
    return null;
  }
}
```

### Fix 2: Global unhandled rejection handler

```javascript
process.on("unhandledRejection", (reason, promise) => {
  console.error("Unhandled Rejection at:", promise, "reason:", reason);
  // Log to error reporting service
  // Sentry.captureException(reason);
});

// Note: This does NOT prevent the process from exiting in Node 15+
// Fix the actual unhandled rejection instead
```

### Fix 3: Ensure all async calls are awaited

```javascript
// Bad: fire-and-forget
async function processRequest(req, res) {
  await saveToDatabase(req.body);
  saveAuditLog(req.body); // not awaited — unhandled rejection possible
  res.send("ok");
}

// Good: await or catch all async operations
async function processRequest(req, res) {
  await saveToDatabase(req.body);
  await saveAuditLog(req.body); // or: saveAuditLog(req.body).catch(console.error)
  res.send("ok");
}
```

## Examples

```javascript
// Unhandled rejection: promise returned but never handled
async function riskyOperation() {
  throw new Error("Database connection failed");
}

// Bad — return value is ignored
riskyOperation();

// Good — handled with try/catch
try {
  await riskyOperation();
} catch (err) {
  console.error("Operation failed:", err.message);
}
```

## Related Errors

- [Uncaught Exception]({{< relref "/languages/javascript/uncaught-promise" >}}) — synchronous uncaught exception.
- [ERR_STREAM_DESTROYED]({{< relref "/languages/javascript/err_stream_destroyed" >}}) — stream destroyed before operation completes.
- [InternalError]({{< relref "/languages/javascript/internalerror" >}}) — internal Node.js error.
