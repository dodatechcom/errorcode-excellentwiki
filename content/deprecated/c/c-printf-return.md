---
title: "[Solution] Deprecated Function Migration: unchecked printf return to checked"
description: "Migrate from deprecated unchecked printf return to checked."
deprecated_function: "printf with unchecked return"
replacement_function: "checked printf return value"
languages: ["c"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: unchecked printf return to checked

The `printf("%s", str)` has been deprecated in favor of `if (printf("%s", str) < 0) { }`.

## Migration Guide

printf can fail.

## Before (Deprecated)

```c
printf("%s", str);
```

## After (Modern)

```c
if (printf("%s", str) < 0) {
    perror("printf failed");
}
```

## Key Differences

- Always check printf return
