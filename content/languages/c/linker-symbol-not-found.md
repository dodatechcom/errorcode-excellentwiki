---
title: "[Solution] C SYMBOL_NOT_FOUND — Symbol(s) not found"
description: "Fix C symbol not found errors by checking visibility, static vs shared libraries, and -fvisibility flags. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["linker-error"]
weight: 804
---

# C SYMBOL_NOT_FOUND — Symbol(s) not found

The linker reports that certain symbols could not be found during linking. This differs from a simple undefined reference — it often relates to symbol visibility in shared libraries, ABI mismatches, or stripping of symbols.

## Common Causes

```c
// Cause 1: Function hidden with -fvisibility=hidden but not exported
// compiled with: gcc -fvisibility=hidden -shared -o libfoo.so foo.c
void public_api(void) { /* ... */ }
// Symbol is hidden — linker cannot find it when loading the shared library
```

```c
// Cause 2: Static library does not contain the symbol
// libbar.a was compiled from an empty source or the symbol was in a file not included
```

```c
// Cause 3: Stripped shared library
// strip libfoo.so removed all symbols
// nm libfoo.so shows no entries
```

```c
// Cause 4: C++ mangled names when loading with dlsym
// void my_func() compiled as C++ → symbol is _Z7my_funcv
// dlsym(handle, "my_func") → symbol not found
```

```c
// Cause 5: ABI incompatibility between compiled code and library
// Library built with different struct layout or calling convention
```

## How to Fix

### Fix 1: Export symbols with visibility attributes

```c
// Compile with -fvisibility=hidden but explicitly export what you need
__attribute__((visibility("default")))
void public_api(void) {
    // This symbol will be visible in the shared library
}

// Or use a version script
// exports.map:
// { global: public_api; local: *; };
// gcc -shared -Wl,--version-script=exports.map -o libfoo.so foo.c
```

### Fix 2: Verify symbol existence with nm and objdump

```bash
# Check if symbol exists in the library
nm -D libfoo.so | grep public_api
nm libfoo.a | grep public_api

# Check dynamic symbols
objdump -T libfoo.so | grep public_api

# Detailed symbol info
readelf -s libfoo.so | grep public_api
```

### Fix 3: Use the correct name mangling for C++ interop

```c
// For dlsym with C++ compiled code
extern "C" void my_func(void) { /* ... */ }

// Or search for the mangled name
// dlsym(handle, "_Z7my_funcv");
```

### Fix 4: Rebuild shared libraries with symbols intact

```bash
# Do not strip if you need symbols for debugging or linking
gcc -shared -o libfoo.so foo.c

# If stripping is needed for release, keep a debug version
gcc -shared -g -o libfoo_debug.so foo.c
gcc -shared -o libfoo.so foo.c && strip --strip-debug libfoo.so
```

### Fix 5: Ensure consistent ABI between build and library

```bash
# Check library ABI
nm -D /usr/lib/libfoo.so | grep version

# Ensure headers match the library version
dpkg -l | grep libfoo-dev

# Rebuild both the library and your code with the same toolchain
```

## Examples

```c
// Building a shared library with explicit symbol exports
// mylib.h
#ifndef MYLIB_H
#define MYLIB_H

#ifdef BUILDING_MYLIB
#define MYLIB_API __attribute__((visibility("default")))
#else
#define MYLIB_API
#endif

MYLIB_API int mylib_init(void);
MYLIB_API void mylib_cleanup(void);

// Internal function — not exported
void internal_helper(void);

#endif

// mylib.c
#include "mylib.h"

void internal_helper(void) { /* hidden from outside */ }

MYLIB_API int mylib_init(void) { return 0; }
MYLIB_API void mylib_cleanup(void) { }
```

```bash
# Building with version script
# libmap.map
{ global: mylib_init; mylib_cleanup; local: *; };

gcc -shared -fPIC -Wl,--version-script=libmap.map -o libmylib.so mylib.c

# Verify
nm -D libmylib.so | grep mylib
# Should show: T mylib_init, T mylib_cleanup — no internal_helper
```

## Related Errors

- [C UNDEFINED_REFERENCE](/languages/c/linker-undefined-reference) — Undefined reference to symbol
- [C CANNOT_FIND_LIBRARY](/languages/c/linker-cannot-find-library) — Cannot find -l
- [C UNDEFINED_REFERENCE_STATIC](/languages/c/linker-undefined-reference-static) — Undefined reference in static library
