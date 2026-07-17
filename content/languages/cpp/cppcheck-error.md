---
title: "[Solution] C++ cppcheck - static analysis error"
description: "Fix C++ cppcheck static analysis errors. Address code quality issues found by cppcheck."
languages: ["cpp"]
severities: ["error"]
error-types: ["compile-error"]
tags: ["cppcheck", "static-analysis", "lint", "code-quality", "warning"]
weight: 5
---

# cppcheck - static analysis error

cppcheck is a static analysis tool that finds bugs and dangerous coding patterns. It reports errors without running the code.

## Common Causes

```cpp
// Cause 1: Memory leak
void func() {
    int* p = new int[100];
    if (error) return; // leak
    delete[] p;
}

// Cause 2: Uninitialized variable
void func() {
    int x;
    if (condition) x = 5;
    printf("%d", x); // may be uninitialized
}

// Cause 3: Null pointer dereference
void func(int* p) {
    *p = 10; // may be null
}
```

## How to Fix

### Fix 1: Run cppcheck

```bash
cppcheck --enable=all src/
```

### Fix 2: Fix reported issues

```cpp
// Fix memory leak
void func() {
    int* p = new int[100];
    delete[] p; // always free
}

// Fix uninitialized
void func() {
    int x = 0; // initialize
    if (condition) x = 5;
}
```

### Fix 3: Use inline suppression

```cpp
// cppcheck-suppress memoryLeak
int* p = new int[100]; // intentionally leak for performance
```

## Related Errors

- [clang-tidy - lint error]({{< relref "/languages/cpp/clang-tidy-error" >}}) — clang-tidy errors.
- [Valgrind - memory error]({{< relref "/languages/cpp/valgrind-error" >}}) — memory errors.
- [AddressSanitizer]({{< relref "/languages/cpp/sanitizers-address" >}}) — runtime memory errors.
