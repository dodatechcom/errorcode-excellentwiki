---
title: "[Solution] C++ MemorySanitizer - uninitialized memory read"
description: "Fix C++ MemorySanitizer uninitialized memory read errors. Initialize all variables."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# MemorySanitizer - uninitialized memory read

MemorySanitizer (MSan) detects reads from uninitialized memory. This catches bugs where variables are used before being assigned.

## Common Causes

```cpp
// Cause 1: Uninitialized variable
int x;
if (condition) x = 5;
printf("%d", x); // MSan: use-of-uninitialized-value

// Cause 2: Uninitialized struct member
struct Point { int x, y; };
Point p;
p.x = 1;
process(p.y); // uninitialized

// Cause 3: Uninitialized memory from malloc
int* p = (int*)malloc(sizeof(int));
printf("%d", *p); // uninitialized
```

## How to Fix

### Fix 1: Compile with MSan

```bash
clang++ -fsanitize=memory -g -o prog prog.cpp
./prog
```

### Fix 2: Initialize all variables

```cpp
int x = 0; // initialize
if (condition) x = 5;
printf("%d", x); // safe
```

### Fix 3: Use calloc instead of malloc

```cpp
int* p = (int*)calloc(1, sizeof(int)); // zero-initialized
```

## Related Errors

- [AddressSanitizer]({{< relref "/languages/cpp/sanitizers-address" >}}) — memory errors.
- [UndefinedBehaviorSanitizer]({{< relref "/languages/cpp/sanitizers-undefined" >}}) — UB detection.
- [C: Uninitialized variable]({{< relref "/languages/c/uninitialized-variable" >}}) — uninitialized variable.
