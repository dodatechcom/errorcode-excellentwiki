---
title: "[Solution] C++ UndefinedBehaviorSanitizer - UB detected"
description: "Fix C++ UndefinedBehaviorSanitizer (UBSan) errors. Detect and fix undefined behavior."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# UndefinedBehaviorSanitizer - UB detected

UndefinedBehaviorSanitizer (UBSan) detects undefined behavior such as signed integer overflow, null pointer dereference, and misaligned pointer access.

## Common Causes

```cpp
// Cause 1: Signed integer overflow
int x = INT_MAX;
int y = x + 1; // UBSan: signed integer overflow

// Cause 2: Null pointer dereference
int* p = nullptr;
*p = 10; // UBSan: null pointer use

// Cause 3: Misaligned access
char buf[16];
int* p = reinterpret_cast<int*>(buf + 1);
*p = 42; // UBSan: misaligned address
```

## How to Fix

### Fix 1: Compile with UBSan

```bash
g++ -fsanitize=undefined -g -o prog prog.cpp
./prog
```

### Fix 2: Fix undefined behavior

```cpp
// Fix signed overflow
int x = INT_MAX;
if (x > INT_MAX - 1) {
    // handle overflow
}
int y = x + 1;

// Fix null pointer
if (p != nullptr) {
    *p = 10;
}
```

### Fix 3: Use unsigned for wrapping

```cpp
unsigned int x = UINT_MAX;
unsigned int y = x + 1; // well-defined wrap
```

## Related Errors

- [AddressSanitizer]({{< relref "/languages/cpp/sanitizers-address" >}}) — memory errors.
- [MemorySanitizer]({{< relref "/languages/cpp/sanitizers-memory" >}}) — uninitialized memory.
- [std::overflow_error]({{< relref "/languages/cpp/overflow-error-arithmetic" >}}) — arithmetic overflow.
