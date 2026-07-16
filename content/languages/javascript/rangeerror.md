---
title: "[Solution] JavaScript RangeError — Value Out of Valid Range Fix"
description: "Fix JavaScript RangeError for invalid array length, maximum call stack, and invalid values. Validate inputs, check recursion depth, and use safe ranges."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
tags: ["rangeerror", "array-length", "recursion", "call-stack"]
weight: 75
---

# RangeError — Value Out of Valid Range Fix

A `RangeError` in JavaScript is thrown when a value is not within the set of allowed values or allowed range. Common triggers include invalid array lengths, numbers beyond `Number.MAX_SAFE_INTEGER`, and exceeding the maximum recursion depth.

## Common Causes

```javascript
// Cause 1: Invalid array length
const arr = new Array(-1);  // RangeError: Invalid array length
const arr2 = new Array(Infinity);  // RangeError: Invalid array length

// Cause 2: Number out of range
const num = Math.pow(2, 1024);  // RangeError: Maximum number size exceeded

// Cause 3: Maximum call stack size exceeded (infinite recursion)
function recurse() {
    return recurse();  // RangeError: Maximum call stack size exceeded
}
recurse();

// Cause 4: Invalid time value
new Date("not-a-date");  // RangeError: Invalid time value

// Cause 5: toPrecision/toFixed with invalid digits
const n = 123;
n.toPrecision(101);  // RangeError: toPrecision() argument must be between 1 and 100
```

## Solutions

### Fix 1: Validate array length before creating arrays

```javascript
// Wrong — no validation
function createBuffer(size) {
    return new Array(size).fill(0);
}
createBuffer(-5);  // RangeError

// Correct — validate the length
function createBuffer(size) {
    if (!Number.isInteger(size) || size < 0 || size > 10_000_000) {
        throw new RangeError(`Invalid buffer size: ${size}`);
    }
    return new Array(size).fill(0);
}
```

### Fix 2: Use iterative approaches instead of deep recursion

```javascript
// Wrong — recursive factorial blows the stack for large n
function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
factorial(100000);  // RangeError: Maximum call stack size exceeded

// Correct — iterative approach
function factorial(n) {
    if (!Number.isInteger(n) || n < 0) {
        throw new RangeError(`Invalid argument: ${n}`);
    }
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

// Also correct — tail-call optimized (only in strict mode, limited support)
function factorialTCO(n, acc = 1) {
    if (n <= 1) return acc;
    return factorialTCO(n - 1, n * acc);
}
```

### Fix 3: Clamp numeric values to safe ranges

```javascript
// Wrong — passes unvalidated value
function setTimer(callback, delay) {
    return setTimeout(callback, delay);
}
setTimer(() => console.log("done"), -1000);  // clamped to 0 by engine

// Correct — clamp to valid range
function setTimer(callback, delay) {
    const SAFE_MIN = 0;
    const SAFE_MAX = 2147483647; // 2^31 - 1, max for setTimeout
    const safeDelay = Math.max(SAFE_MIN, Math.min(SAFE_MAX, Math.floor(delay)));
    return setTimeout(callback, safeDelay);
}
```

### Fix 4: Guard Number methods with range checks

```javascript
// Wrong — unvalidated input
function formatPrice(value, decimals) {
    return value.toFixed(decimals);
}
formatPrice(19.99, 101);  // RangeError

// Correct — validate digits parameter
function formatPrice(value, decimals) {
    if (!Number.isFinite(value)) {
        throw new RangeError(`Invalid price: ${value}`);
    }
    const safeDecimals = Math.max(0, Math.min(20, Math.floor(decimals)));
    return value.toFixed(safeDecimals);
}
```

### Fix 5: Safe recursion with depth limits

```javascript
// Wrong — no depth guard
function traverseTree(node) {
    processNode(node);
    for (const child of node.children) {
        traverseTree(child);  // can overflow for deep trees
    }
}

// Correct — track depth and switch to iterative approach
function traverseTree(node, maxDepth = 1000) {
    const stack = [{ node, depth: 0 }];
    while (stack.length > 0) {
        const { node: current, depth } = stack.pop();
        processNode(current);
        if (depth >= maxDepth) {
            console.warn(`Max depth ${maxDepth} reached, switching to iterative`);
        }
        for (const child of current.children ?? []) {
            stack.push({ node: child, depth: depth + 1 });
        }
    }
}
```

## Prevention Tips

- Always validate numeric inputs before passing them to `Array`, `Number` methods, or recursive functions.
- Prefer iterative algorithms over recursive ones when processing unknown-depth data.
- Use `Number.isFinite()` and `Number.isInteger()` for input validation.
- Set maximum recursion depth guards when recursion is necessary.

## Related Errors

- [TypeError](typeerror) — value is not the expected type.
- [ReferenceError](referenceerror) — variable does not exist in scope.
- [InternalError](internalerror) — engine internal error, often from excessive recursion.
