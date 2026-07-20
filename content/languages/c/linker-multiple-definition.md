---
title: "[Solution] C MULTIPLE_DEFINITION — Multiple definition of symbol"
description: "Fix C multiple definition errors by using extern, static, or include guards. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["linker-error"]
weight: 802
---

# C MULTIPLE_DEFINITION — Multiple definition of symbol

The linker finds more than one definition of the same global symbol. This occurs when a variable or function is defined in multiple translation units, or when inline functions are not handled correctly.

## Common Causes

```c
// Cause 1: Defining a variable in a header without extern
// config.h
int global_counter = 0;  // every .c file that includes this gets a copy

// main.c and helper.c both include config.h → multiple definition
```

```c
// Cause 2: Inline function defined in a header without static or extern
// utils.h
inline int square(int x) { return x * x; }
// Every translation unit including this header defines square()
```

```c
// Cause 3: Defining the same variable in two .c files
// globals.c
int session_count = 0;

// main.c
int session_count = 0;  // duplicate definition
```

```c
// Cause 4: Macro expanding to a definition
// header.h
#define INIT_VALUE int result = 42

// a.c
#include "header.h"  // int result = 42;

// b.c
#include "header.h"  // int result = 42; — if both are in the same TU or linked together
```

```c
// Cause 5: Forgetting static on file-scope constants
// constants.h
const double PI = 3.14159265358979;  // not static, not extern — defined in every includer
```

## How to Fix

### Fix 1: Use extern for declarations in headers, define in one .c file

```c
// config.h
extern int global_counter;  // declaration only

// config.c
#include "config.h"
int global_counter = 0;  // single definition
```

### Fix 2: Make inline functions static or extern inline

```c
// utils.h — option A: static inline (each TU gets its own copy, no linker error)
static inline int square(int x) { return x * x; }

// utils.h — option B: extern inline (one definition in a .c file)
extern inline int square(int x);

// utils.c
#include "utils.h"
inline int square(int x) { return x * x; }
```

### Fix 3: Use static for file-scope variables that should be private

```c
// helper.c
static int internal_count = 0;  // visible only in this file
```

### Fix 4: Use include guards and ensure definitions appear only once

```c
// constants.h
#ifndef CONSTANTS_H
#define CONSTANTS_H

static const double PI = 3.14159265358979;  // static gives each TU its own copy

#endif
```

### Fix 5: Use -fcommon or -fno-common to control tentative definitions

```bash
# Older GCC defaulted to -fcommon (merged tentative definitions)
# GCC 10+ defaults to -fno-common (rejects them)

# Temporary fix:
gcc -fcommon main.c globals.c -o app

# Proper fix: use extern
```

## Examples

```c
// Real-world: header with multiple global settings
// settings.h
#ifndef SETTINGS_H
#define SETTINGS_H

extern const int MAX_BUFFER_SIZE;
extern const char* APP_NAME;

#endif

// settings.c
#include "settings.h"
const int MAX_BUFFER_SIZE = 4096;
const char* APP_NAME = "MyApp";
```

```c
// Real-world: inline math helpers
// math_inline.h
#ifndef MATH_INLINE_H
#define MATH_INLINE_H

static inline int clamp(int val, int lo, int hi) {
    if (val < lo) return lo;
    if (val > hi) return hi;
    return val;
}

#endif
```

## Related Errors

- [C UNDEFINED_REFERENCE](/languages/c/linker-undefined-reference) — Undefined reference to symbol
- [C IMPLICIT_DECLARATION](/languages/c/gcc-implicit-declaration) — Implicit function declaration
- [C CONFLICTING_TYPES](/languages/c/gcc-conflicting-types) — Conflicting types for function
