---
title: "[Solution] Deprecated Function Migration: scanf to fgets + sscanf for safety"
description: "Migrate from deprecated scanf for buffer safety to fgets + sscanf."
deprecated_function: "scanf with unchecked buffer"
replacement_function: "fgets(buf, size, stdin); sscanf(buf, ...)"
languages: ["c"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: scanf to fgets + sscanf for safety

The `scanf("%s", buf)` has been deprecated in favor of `fgets(buf, size, stdin); sscanf(buf, ...)`.

## Migration Guide

scanf has no buffer limit.

## Before (Deprecated)

```c
scanf("%s", buf);
```

## After (Modern)

```c
fgets(buf, sizeof(buf), stdin);
sscanf(buf, "%s", parsed);
```

## Key Differences

- fgets prevents buffer overflow
