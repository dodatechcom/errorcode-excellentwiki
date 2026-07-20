---
title: "[Solution] C RELOCATION_ERROR — Relocation truncated to fit"
description: "Fix C relocation truncated to fit errors by using -mcmodel=medium, checking data alignment, and handling large arrays. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["linker-error"]
weight: 805
---

# C RELOCATION_ERROR — Relocation truncated to fit

The linker cannot fit a relocation into the available address space. This typically happens on x86-64 when code or data exceeds the 32-bit displacement range used by default, often due to large static arrays or very large code sections.

## Common Causes

```c
// Cause 1: Large static array in a single translation unit
static char huge_buffer[2 * 1024 * 1024];  // 2MB static array
// On x86-64 with small code model, the 32-bit displacement cannot reach it
```

```c
// Cause 2: Building a very large executable (>2GB)
// Thousands of functions or large code sections push the text segment beyond 2GB
int func0001(void) { return 1; }
int func0002(void) { return 2; }
// ... repeated thousands of times
```

```c
// Cause 3: Position-dependent code with large address space
// Compiled without -fPIC but placed at a high address by the linker
void __attribute__((section(".text.high"))) high_func(void) { }
```

```c
// Cause 4: Large read-only data segment
static const char data[] = "..."  // many megabytes of string data
```

```c
// Cause 5: Linker script placing sections at addresses beyond 32-bit range
// custom.ld: . = 0x100000000;  (4GB+ address)
```

## How to Fix

### Fix 1: Use the medium or large code model

```bash
# Medium code model: data up to 2GB, code can be anywhere
gcc -mcmodel=medium main.c -o app

# Large code model: no restrictions (slightly slower)
gcc -mcmodel=large main.c -o app

# Small code model (default): everything within 2GB of the binary
gcc -mcmodel=small main.c -o app
```

### Fix 2: Move large arrays to the heap

```c
// Instead of a large static array:
// static char buffer[4 * 1024 * 1024];  // causes relocation error

// Use dynamic allocation:
#include <stdlib.h>
char *buffer = malloc(4 * 1024 * 1024);
if (buffer == NULL) {
    return 1;
}
// ... use buffer ...
free(buffer);
```

### Fix 3: Split large translation units into smaller files

```c
// Instead of one giant file with 100,000 functions:
// split_into_files.c → func_group_1.c, func_group_2.c, etc.
// Each file is compiled separately, keeping individual object files small
```

### Fix 4: Use position-independent code for shared libraries

```bash
# Compile with -fPIC for shared libraries
gcc -fPIC -shared -o libfoo.so foo.c

# For executables that might be loaded at arbitrary addresses
gcc -fPIE -pie main.c -o app
```

### Fix 5: Check and fix linker scripts

```bash
# If using a custom linker script, ensure sections are within range
# Remove overly high address assignments
# OR use -Ttext-segment to set a reachable base address
gcc -Wl,-Ttext-segment=0x400000 main.c -o app
```

## Examples

```c
// Real-world: embedded system with large lookup table
#include <stdlib.h>

// This causes relocation truncated to fit:
// static uint8_t lookup_table[3 * 1024 * 1024];

// Fix: allocate dynamically at runtime
static uint8_t *lookup_table = NULL;

int init_table(void) {
    lookup_table = malloc(3 * 1024 * 1024);
    if (!lookup_table) return -1;
    // populate table...
    return 0;
}
```

```bash
# Diagnosing: find which symbols are too far
gcc -Wl,--no-relax main.o large.o -o app 2>&1
# The error message tells you which symbol has the truncated relocation

# Check section sizes
size app
#   text    data     bss     dec     hex filename
# 2500000  100000 3000000 5600000  557320 app

readelf -S app | grep -E '\.text|\.data|\.bss'
```

## Related Errors

- [C STRICT_ALIASING_VIOLATION](/languages/c/strict-aliasing-violation) — Strict aliasing violation
- [C SIGNED_INTEGER_OVERFLOW](/languages/c/signed-integer-overflow-ub) — Signed integer overflow UB
- [C SHIFT_TOO_WIDE](/languages/c/shift-too-wide) — Shift count >= width of type
