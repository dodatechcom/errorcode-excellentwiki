---
title: "[Solution] RangeError Maximum Call Stack Size Exceeded — Infinite Recursion Fix"
description: "Fix RangeError: Maximum call stack size exceeded caused by infinite recursion or very deep recursion."
languages: ["javascript"]
severities: ["error"]
error_types: ["runtime"]
weight: 50
---

# Maximum Call Stack Size Exceeded

```javascript
// Infinite recursion
function recurse() {
  return recurse();
}
recurse(); // RangeError

// Mutual recursion
function a() { return b(); }
function b() { return a(); }
a(); // RangeError
```

## Fix

Add a base case:

```javascript
function factorial(n) {
  if (n <= 1) return 1;  // base case
  return n * factorial(n - 1);
}
```
