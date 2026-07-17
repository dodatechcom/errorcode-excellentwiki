---
title: "[Solution] C++ GDB - debugging error"
description: "Fix C++ GDB debugging errors. Debug crash and assertion failures with GDB."
languages: ["cpp"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# GDB - debugging error

GDB (GNU Debugger) is used to analyze crashes, segfaults, and assertion failures in C++ programs.

## Common Causes

```cpp
// Cause 1: Segmentation fault
int* p = nullptr;
*p = 10; // crash

// Cause 2: Assertion failure
assert(x > 0); // fails if x <= 0

// Cause 3: Abort from exception
throw std::runtime_error("fatal");
// not caught — std::terminate called
```

## How to Fix

### Fix 1: Compile with debug symbols

```bash
g++ -g -o prog prog.cpp
```

### Fix 2: Run under GDB

```bash
gdb ./prog
(gdb) run
# When it crashes:
(gdb) bt
(gdb) print variable
```

### Fix 3: Generate core dump

```bash
ulimit -c unlimited
./prog  # crashes, generates core
gdb ./prog core
(gdb) bt
```

## Related Errors

- [LLDB - debugging error]({{< relref "/languages/cpp/lldb-error" >}}) — LLDB errors.
- [AddressSanitizer]({{< relref "/languages/cpp/sanitizers-address" >}}) — runtime errors.
- [C: Segmentation fault]({{< relref "/languages/c/segmentation-fault-null" >}}) — segfault.
