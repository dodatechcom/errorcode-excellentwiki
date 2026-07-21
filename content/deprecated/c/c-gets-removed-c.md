---
title: "[Solution] Deprecated Function Migration: gets() to fgets() in C"
description: "Migrate from removed gets() to fgets() for safe string input in C."
deprecated_function: "gets()"
replacement_function: "fgets()"
languages: ["c"]
deprecated_since: "C11 removed"
---

# [Solution] Deprecated Function Migration: gets() to fgets() in C

The `gets()` has been deprecated in favor of `fgets()`.

## Migration Guide

gets() was removed from C11 because it has no way to limit input.

## Before (Deprecated)

```c
#include <stdio.h>

char buffer[100];
gets(buffer);  // DANGEROUS
```

## After (Modern)

```c
#include <stdio.h>

char buffer[100];
if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
    buffer[strcspn(buffer, "\n")] = '\0';
    printf("You entered: %s\n", buffer);
}
```

## Key Differences

- gets() is removed from C11
- fgets() takes a size parameter
- fgets includes the newline character
- Use strcspn to remove trailing newline
