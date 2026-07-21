---
title: "[Solution] Deprecated Function Migration: gets to fgets in C"
description: "Migrate from deprecated gets to fgets for safe input."
deprecated_function: "gets(buf)"
replacement_function: "fgets(buf, size, stdin)"
languages: ["c"]
deprecated_since: "C11 removed"
---

# [Solution] Deprecated Function Migration: gets to fgets in C

The `gets(buf)` has been deprecated in favor of `fgets(buf, size, stdin)`.

## Migration Guide

gets has no bounds checking

gets was removed from C11. fgets reads with bounds checking.

## Before (Deprecated)

```c
char buf[100];
gets(buf);  // REMOVED in C11
```

## After (Modern)

```c
char buf[100];
if (fgets(buf, sizeof(buf), stdin) != NULL) {
    buf[strcspn(buf, "\n")] = '\0';
}
```

## Key Differences

- fgets takes size parameter
- fgets includes newline
- Use strcspn to remove newline
- gets is removed from C11
