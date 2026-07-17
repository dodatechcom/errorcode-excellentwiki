---
title: "[Solution] JavaScript RangeError: Maximum call stack size exceeded Fix"
description: "Fix JavaScript RangeError: Maximum call stack size exceeded. Diagnose infinite recursion, circular references, and prevent stack overflows in JS code."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# RangeError: Maximum call stack size exceeded

A `RangeError: Maximum call stack size exceeded` (or `Maximum recursive depth exceeded` in some engines) is thrown when a function calls itself or triggers a chain of calls that exceeds the JavaScript engine's call stack limit. This is the JavaScript equivalent of a stack overflow.

## Description

JavaScript uses a call stack to track function execution. Each function call pushes a frame onto the stack. When the stack fills up (typically 10,000-25,000 frames depending on the engine), the engine throws a RangeError. Common causes include infinite recursion, circular references in serialization, and deep object cloning.

Common variants:

- `RangeError: Maximum call stack size exceeded`
- `RangeError: Maximum recursion depth exceeded`
- `InternalError: too much recursion` (Firefox)

## Common Causes

```javascript
// Cause 1: Infinite recursion
function recurse() {
    return recurse();  // RangeError: Maximum call stack size exceeded
}
recurse();

// Cause 2: Circular reference in JSON.stringify
const a = {};
const b = { ref: a };
a.ref = b;
JSON.stringify(a);  // RangeError

// Cause 3: Circular prototype chain
class Node {
    constructor() {
        this.child = new Node();  // Infinite constructor recursion
    }
}

// Cause 4: Infinite event listener chain
element.addEventListener("click", () => {
    element.click();  // Triggers the listener again → infinite loop
});

// Cause 5: Deep recursion in tree traversal without base case
function traverse(node) {
    process(node);
    traverse(node);  // Same node, no base case
}
```

## How to Fix

### Fix 1: Add a base case to recursive functions

```javascript
// Wrong — no base case
function factorial(n) {
    return n * factorial(n - 1);
}

// Correct
function factorial(n) {
    if (n <= 1) return 1;  // base case
    return n * factorial(n - 1);
}
```

### Fix 2: Convert recursion to iteration

```javascript
// Wrong — recursive Fibonacci
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Correct — iterative
function fibonacci(n) {
    if (n <= 1) return n;
    let a = 0, b = 1;
    for (let i = 2; i <= n; i++) {
        [a, b] = [b, a + b];
    }
    return b;
}
```

### Fix 3: Handle circular references in serialization

```javascript
// Wrong — circular reference causes stack overflow
const obj = { name: "self" };
obj.self = obj;
JSON.stringify(obj);  // RangeError

// Correct — use a seen set to detect cycles
function safeStringify(obj, seen = new WeakSet()) {
    if (typeof obj !== "object" || obj === null) {
        return JSON.stringify(obj);
    }
    if (seen.has(obj)) {
        return '"[Circular]"';
    }
    seen.add(obj);
    const result = Array.isArray(obj)
        ? `[${obj.map(item => safeStringify(item, seen)).join(",")}]`
        : `{${Object.entries(obj)
            .map(([k, v]) => `${JSON.stringify(k)}:${safeStringify(v, seen)}`)
            .join(",")}}`;
    seen.delete(obj);
    return result;
}
```

### Fix 4: Use structuredClone for deep copying

```javascript
// Wrong — recursive deep copy
function deepCopy(obj) {
    const copy = {};
    for (const key in obj) {
        copy[key] = typeof obj[key] === "object" ? deepCopy(obj[key]) : obj[key];
    }
    return copy;
}

// Correct — use structuredClone (modern browsers/Node.js)
const copy = structuredClone(obj);

// Or use JSON (won't handle circular refs)
const copy = JSON.parse(JSON.stringify(obj));
```

### Fix 5: Add depth limits to recursive tree traversal

```javascript
// Wrong — no depth limit
function traverse(node, depth = 0) {
    process(node);
    for (const child of node.children) {
        traverse(child, depth + 1);
    }
}

// Correct — add a safety limit
function traverse(node, depth = 0, maxDepth = 1000) {
    if (depth > maxDepth) {
        console.warn("Max recursion depth reached");
        return;
    }
    process(node);
    for (const child of node.children) {
        traverse(child, depth + 1, maxDepth);
    }
}
```

## Examples

This error commonly occurs when:

- A `toString()` or `toJSON()` method calls itself recursively
- An event handler triggers the same event it's listening for
- A `Vue` or `React` component re-renders infinitely due to state changes in render
- `JSON.stringify` encounters a circular object reference

## Related Errors

- [TypeError: Cannot read properties of undefined](typeerror-cannot-read) — related to recursion failing
- [Uncaught (in promise) TypeError](uncaught-promise) — unhandled rejection from stack overflow
- [DOMException](dom-exception) — related to DOM state issues
