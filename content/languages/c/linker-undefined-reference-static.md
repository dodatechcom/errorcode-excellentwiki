---
title: "[Solution] C UNDEFINED_REFERENCE_STATIC — Undefined reference in static library"
description: "Fix C undefined reference errors with static libraries by fixing library order, using --start-group/--end-group, and object file order. Copy-paste solutions with code examples."
languages: ["c"]
severities: ["error"]
error-types: ["linker-error"]
weight: 806
---

# C UNDEFINED_REFERENCE_STATIC — Undefined reference in static library

When linking with static libraries (`.a` files), the linker processes them left to right. If library A depends on symbols from library B, but A appears before B on the command line, the linker will have already skipped A's unresolved symbols by the time it processes B.

## Common Causes

```bash
# Cause 1: Wrong library order
# libA.a depends on symbols in libB.a
gcc main.o -lA -lB -o app
# Linker processes libA first, finds unresolved refs to libB, skips them
# Then processes libB but no one needs its symbols anymore
```

```c
// Cause 2: Circular dependencies between static libraries
// libA.a calls functions in libB.a
// libB.a calls functions in libA.a
// No linear order can resolve this
```

```bash
# Cause 3: Object file containing needed symbols not in the archive
# libfoo.a contains foo.o and bar.o but not baz.o
# baz.o was never added to the archive
gcc main.o -lfoo  // undefined reference to baz_func
```

```c
// Cause 4: Weak symbols not resolving correctly
// Library A provides a weak definition, library B provides a strong one
// Order affects which one the linker picks
```

```bash
# Cause 5: Static library built from C++ without proper linkage
# ar rcs libfoo.a foo.o  // foo.o was compiled from .cpp file
# Linker looking for C symbol names but finds mangled C++ names
```

## How to Fix

### Fix 1: Reorder libraries so dependents come before dependencies

```bash
# WRONG: libA depends on libB but comes first
gcc main.o -lA -lB -o app

# CORRECT: libA depends on libB, so libB comes after
gcc main.o -lB -lA -o app

# General rule: list libraries from most dependent to least dependent
```

### Fix 2: Use --start-group and --end-group for circular dependencies

```bash
# For circular dependencies between static libraries
gcc main.o -Wl,--start-group -lA -lB -lC -Wl,--end-group -o app

# The linker will repeatedly scan the group until all symbols resolve
# This is slower but handles any dependency order
```

### Fix 3: Repeat libraries on the command line

```bash
# Simple alternative to --start-group for A ↔ B circular dependency
gcc main.o -lA -lB -lA -o app

# Second -lA picks up symbols that libB needed from libA
```

### Fix 4: Verify the static library contains needed symbols

```bash
# List all symbols in the archive
nm libfoo.a

# Check if specific symbol exists
nm libfoo.a | grep my_function

# If missing, ensure the object file was included when creating the archive
ar t libfoo.a           # list object files in archive
ar rcs libfoo.a foo.o bar.o  # add object files
```

### Fix 5: Extract and relink object files directly

```bash
# Instead of using the archive, extract all .o files and link them directly
mkdir tmp && cd tmp
ar x ../libA.a
ar x ../libB.a
gcc main.o *.o -o app
cd .. && rm -rf tmp
```

## Examples

```c
// Real-world scenario: project with circular library dependencies
// mathlib.c defines: double fast_sin(double x);
// applib.c calls: fast_sin()  and defines: void process(double);
// main.c calls: process()

// libmath.a contains: mathlib.o
// libapp.a contains: applib.o

// WRONG: gcc main.o -lapp -lmath
// main.o needs process() → found in libapp.a ✓
// libapp.a needs fast_sin() → libapp is processed, but libmath not yet seen ✗

// CORRECT: gcc main.o -lmath -lapp
// main.o needs process() → not in libmath, skip unresolved
// libapp.a needs fast_sin() → found in libmath ✓
// Now go back: main.o needs process() → found in libapp ✓
// OR: gcc main.o -Wl,--start-group -lapp -lmath -Wl,--end-group
```

```bash
# Debugging: trace linker resolution
gcc -Wl,--trace main.o -lA -lB -o app 2>&1 | head -50
# Shows which archive the linker is searching and what symbols it resolves

# Check what symbols are still undefined after partial linking
gcc -r main.o -lA -o partial.o
nm partial.o | grep ' U '  # undefined symbols
```

## Related Errors

- [C UNDEFINED_REFERENCE](/languages/c/linker-undefined-reference) — Undefined reference to symbol
- [C MULTIPLE_DEFINITION](/languages/c/linker-multiple-definition) — Multiple definition of symbol
- [C CANNOT_FIND_LIBRARY](/languages/c/linker-cannot-find-library) — Cannot find -l
