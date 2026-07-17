---
title: "[Solution] C++ LLDB - debugging error"
description: "Fix C++ LLDB debugging errors. Debug crash and assertion failures with LLDB."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# LLDB - debugging error

LLDB is the LLVM debugger, used to analyze crashes and assertion failures in C++ programs on macOS and Linux.

## Common Causes

```cpp
// Cause 1: Null pointer dereference
int* p = nullptr;
*p = 10; // crash

// Cause 2: Out of bounds access
std::vector<int> v = {1, 2, 3};
int x = v[10]; // crash (if debug iterators)

// Cause 3: Use after free
int* p = new int(42);
delete p;
*p = 10; // crash
```

## How to Fix

### Fix 1: Compile with debug symbols

```bash
clang++ -g -o prog prog.cpp
```

### Fix 2: Run under LLDB

```bash
lldb ./prog
(lldb) run
# When it crashes:
(lldb) bt
(lldb) frame variable
```

### Fix 3: Set breakpoints

```bash
(lldb) breakpoint set --name main
(lldb) run
```

## Related Errors

- [GDB - debugging error]({{< relref "/languages/cpp/gdb-error" >}}) — GDB errors.
- [AddressSanitizer]({{< relref "/languages/cpp/sanitizers-address" >}}) — runtime errors.
- [UndefinedBehaviorSanitizer]({{< relref "/languages/cpp/sanitizers-undefined" >}}) — UB detection.
