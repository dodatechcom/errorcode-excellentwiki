---
title: "[Solution] JavaScript Uncaught (in promise) TypeError Fix"
description: "Fix JavaScript Uncaught (in promise) TypeError: rejected promise without catch handler. Add .catch(), use try/catch with async/await, and handle errors properly."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# Uncaught (in promise) TypeError

An `Uncaught (in promise) TypeError` occurs when a Promise rejects and no `.catch()` handler or `try/catch` block catches the rejection. In modern browsers and Node.js, unhandled promise rejections are logged as errors and may eventually crash the process.

## Description

When a Promise rejects, the rejection must be handled with `.catch()` or a `try/catch` around `await`. If neither is present, the JavaScript engine logs the error as an unhandled rejection. The error message includes the original error that caused the rejection.

Common patterns:

- `Uncaught (in promise) TypeError: Failed to fetch` — network error
- `Uncaught (in promise) TypeError: Cannot read properties of undefined` — data error
- `Uncaught (in promise) SyntaxError: Unexpected token` — JSON parse error

## Common Causes

```javascript
// Cause 1: Missing .catch() on promise chain
fetch("/api/data")
    .then(res => res.json())
    .then(data => console.log(data));
    // No .catch() — network error causes unhandled rejection

// Cause 2: await without try/catch
async function loadData() {
    const response = await fetch("/api/data");  // No try/catch
    const data = await response.json();
}

// Cause 3: Throwing inside async function without handling
async function process() {
    throw new Error("Something went wrong");
    // If caller doesn't catch, it's an unhandled rejection
}

// Cause 4: Parallel promises where one rejects
const results = await Promise.all([
    fetch("/api/users"),
    fetch("/api/posts"),  // This rejects — unhandled
]);
```

## How to Fix

### Fix 1: Add .catch() to promise chains

```javascript
// Wrong — no error handling
fetch("/api/data")
    .then(res => res.json())
    .then(data => console.log(data));

// Correct
fetch("/api/data")
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error("Failed to load data:", err));
```

### Fix 2: Use try/catch with async/await

```javascript
// Wrong
async function loadData() {
    const response = await fetch("/api/data");
    const data = await response.json();
    return data;
}

// Correct
async function loadData() {
    try {
        const response = await fetch("/api/data");
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (err) {
        console.error("Failed to load data:", err);
        return null;
    }
}
```

### Fix 3: Handle all Promise.all rejections

```javascript
// Wrong — one failure crashes all
const results = await Promise.all([
    fetch("/api/users"),
    fetch("/api/posts"),
]);

// Correct — handle individual failures
const [usersResult, postsResult] = await Promise.allSettled([
    fetch("/api/users").then(r => r.json()),
    fetch("/api/posts").then(r => r.json()),
]);

const users = usersResult.status === "fulfilled" ? usersResult.value : [];
const posts = postsResult.status === "fulfilled" ? postsResult.value : [];
```

### Fix 4: Add a global unhandled rejection handler

```javascript
// For Node.js
process.on("unhandledRejection", (reason, promise) => {
    console.error("Unhandled Rejection:", reason);
    // Optionally exit or send to error tracking
});

// For browsers
window.addEventListener("unhandledrejection", (event) => {
    console.error("Unhandled rejection:", event.reason);
    event.preventDefault();
});
```

### Fix 5: Wrap fire-and-forget async calls

```javascript
// Wrong — fire-and-forget with no error handling
function init() {
    fetch("/api/config").then(r => r.json()).then(config => {
        applyConfig(config);
    });
}

// Correct — handle errors even in fire-and-forget
function init() {
    fetch("/api/config")
        .then(r => r.json())
        .then(config => applyConfig(config))
        .catch(err => console.error("Config load failed:", err));
}

// Or with async IIFE
async function init() {
    try {
        const config = await fetch("/api/config").then(r => r.json());
        applyConfig(config);
    } catch (err) {
        console.error("Config load failed:", err);
    }
}
```

## Examples

This error commonly occurs when:

- Forgetting `.catch()` on a `fetch()` call
- Not wrapping `await` in `try/catch` inside async functions
- Using `Promise.all()` where one promise rejects
- Event handlers that trigger async operations without error handling

## Related Errors

- [TypeError: Cannot read properties of undefined](typeerror-cannot-read) — the error inside the rejected promise
- [TypeError: Failed to fetch](fetch-network-error) — network failure causing rejection
- [SyntaxError: Unexpected token](syntaxerror-json) — JSON parsing error causing rejection
