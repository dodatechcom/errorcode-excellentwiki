---
title: "[Solution] C++ Valgrind - memory error detected"
description: "Fix C++ Valgrind memory errors. Detect and fix memory leaks and access errors."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Valgrind - memory error detected

Valgrind's Memcheck tool detects memory errors including leaks, invalid reads/writes, and use of uninitialized memory.

## Common Causes

```cpp
// Cause 1: Memory leak
void func() {
    int* p = new int[100];
    // forgot delete[]
}

// Cause 2: Invalid read
int* p = new int(42);
delete p;
printf("%d", *p); // invalid read

// Cause 3: Uninitialized value
int x;
printf("%d", x); // use of uninitialized value
```

## How to Fix

### Fix 1: Run Valgrind

```bash
g++ -g -o prog prog.cpp
valgrind --leak-check=full ./prog
```

### Fix 2: Fix reported leaks

```cpp
int* p = new int[100];
// ... use p ...
delete[] p; // free memory
```

### Fix 3: Fix invalid access

```cpp
int* p = new int(42);
int val = *p; // read before delete
delete p;
// don't access p after this
```

## Related Errors

- [AddressSanitizer]({{< relref "/languages/cpp/sanitizers-address" >}}) — faster detection.
- [MemorySanitizer]({{< relref "/languages/cpp/sanitizers-memory" >}}) — uninitialized memory.
- [C: Memory leak]({{< relref "/languages/c/memory-leak-valgrind" >}}) — memory leaks.
