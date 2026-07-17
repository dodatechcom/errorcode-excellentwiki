---
title: "[Solution] JavaScript ReferenceError: setTimeout is not defined Fix"
description: "Fix JavaScript ReferenceError: setTimeout is not defined. This error occurs in Node.js worker threads, Deno, or non-browser environments missing browser globals."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# ReferenceError: setTimeout is not defined

A `ReferenceError: setTimeout is not defined` is thrown when you try to use `setTimeout()` (or `setInterval()`) in an environment where these browser APIs are not available. This commonly happens in Node.js worker threads, Deno without the `--unstable` flag, or when running browser code in a non-browser context.

## Description

`setTimeout` and `setInterval` are browser global functions provided by the Web APIs. They are not part of the ECMAScript specification. While Node.js provides them in the main thread, some environments do not:

- **Node.js Worker Threads** — `setTimeout` is not on the global scope
- **Deno** — requires importing from standard library or using `Deno.sleep`
- **Web Workers** — some environments may not provide them
- **SSR (Server-Side Rendering)** — running browser code on the server

Common variants:

- `ReferenceError: setTimeout is not defined`
- `ReferenceError: setInterval is not defined`
- `ReferenceError: clearTimeout is not defined`

## Common Causes

```javascript
// Cause 1: Using setTimeout in Node.js worker thread
// worker.js
setTimeout(() => console.log("hello"), 1000);  // ReferenceError

// Cause 2: Using in Deno without import
// Deno code
setTimeout(() => console.log("hello"), 1000);  // ReferenceError in older Deno

// Cause 3: Importing browser code in SSR (Next.js, Nuxt)
// lib/utils.js (designed for browser)
export function delay(ms) {
    setTimeout(() => {}, ms);  // ReferenceError during SSR
}

// Cause 4: Using in module scope at top level in some environments
// Strict mode modules
const timer = setTimeout(() => {}, 1000);  // May fail in certain contexts
```

## How to Fix

### Fix 1: Use Node.js timers in worker threads

```javascript
// worker.js (Node.js)
const { parentPort } = require("worker_threads");

// Wrong
setTimeout(() => parentPort.postMessage("done"), 1000);

// Correct — use setImmediate or import timers
const { setTimeout: sleep } = require("timers/promises");
await sleep(1000);

// Or use the Node.js timer module
const timers = require("timers");
timers.setTimeout(() => parentPort.postMessage("done"), 1000);
```

### Fix 2: Check environment before using browser APIs

```javascript
// Wrong — assumes browser environment
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Correct — check for availability
function delay(ms) {
    if (typeof setTimeout !== "undefined") {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    // Fallback for non-browser environments
    return new Promise(resolve => {
        const start = Date.now();
        while (Date.now() - start < ms) { /* busy wait */ }
        resolve();
    });
}

// Or better — use a proper sleep function for Node.js
import { setTimeout as sleep } from "timers/promises";
```

### Fix 3: Import timers explicitly in Deno

```javascript
// Deno
import { delay } from "https://deno.land/std/async/mod.ts";
await delay(1000);

// Or use Deno's built-in
await new Promise(resolve => setTimeout(resolve, 1000));
```

### Fix 4: Guard SSR code with environment checks

```javascript
// lib/utils.js
export function delay(ms) {
    if (typeof window === "undefined") {
        // Server-side: use Node.js timer
        return new Promise(resolve => require("timers").setTimeout(resolve, ms));
    }
    // Browser-side: use native setTimeout
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Or use Next.js dynamic import
export async function delay(ms) {
    if (typeof window === "undefined") {
        const { setTimeout } = await import("timers");
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    return new Promise(resolve => setTimeout(resolve, ms));
}
```

### Fix 5: Create a cross-environment timer utility

```javascript
// timer-utils.js
export function createTimer() {
    if (typeof globalThis.setTimeout === "function") {
        return {
            setTimeout: globalThis.setTimeout.bind(globalThis),
            clearTimeout: globalThis.clearTimeout.bind(globalThis),
            setInterval: globalThis.setInterval.bind(globalThis),
            clearInterval: globalThis.clearInterval.bind(globalThis),
        };
    }

    // Fallback for environments without timers
    return {
        setTimeout: (fn, ms) => {
            const start = Date.now();
            while (Date.now() - start < ms) {}
            fn();
        },
        clearTimeout: () => {},
        setInterval: () => 0,
        clearInterval: () => {},
    };
}

const { setTimeout, clearTimeout } = createTimer();
```

## Examples

This error commonly occurs when:

- Running a library designed for the browser in a Node.js worker thread
- Server-side rendering code that uses browser APIs
- Testing browser code with Jest or other Node.js test runners
- Deno scripts that don't import the standard library

## Related Errors

- [ReferenceError: window is not defined](#) — similar browser API missing in Node.js
- [ReferenceError: document is not defined](#) — DOM API not available in non-browser
- [ReferenceError: navigator is not defined](#) — browser API not available server-side
