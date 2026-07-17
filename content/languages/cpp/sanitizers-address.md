---
title: "[Solution] C++ AddressSanitizer - use-after-free detected"
description: "Fix C++ AddressSanitizer use-after-free errors. Prevent accessing freed memory."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# AddressSanitizer - use-after-free detected

AddressSanitizer (ASan) detects use-after-free, buffer overflows, and other memory errors at runtime.

## Common Causes

```cpp
// Cause 1: Use after free
int* p = new int(42);
delete p;
*p = 10; // ASan: heap-use-after-free

// Cause 2: Stack buffer overflow
char buf[10];
buf[20] = 'x'; // ASan: stack-buffer-overflow

// Cause 3: Double free
int* p = new int(42);
delete p;
delete p; // ASan: double-free
```

## How to Fix

### Fix 1: Compile with ASan

```bash
g++ -fsanitize=address -g -o prog prog.cpp
./prog
```

### Fix 2: Read the report

```
==12345==ERROR: AddressSanitizer: heap-use-after-free on address ...
    #0 0x... in main prog.cpp:5
```

### Fix 3: Fix the memory error

```cpp
int* p = new int(42);
delete p;
p = nullptr; // prevent use-after-free
```

## Related Errors

- [UndefinedBehaviorSanitizer]({{< relref "/languages/cpp/sanitizers-undefined" >}}) — UB detection.
- [MemorySanitizer]({{< relref "/languages/cpp/sanitizers-memory" >}}) — uninitialized memory.
- [Valgrind - memory error]({{< relref "/languages/cpp/valgrind-error" >}}) — memory errors.
