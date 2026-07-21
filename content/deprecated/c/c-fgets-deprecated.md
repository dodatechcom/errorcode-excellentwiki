---
title: "[Solution] Deprecated Function Migration: gets to fgets with newline removal"
description: "Migrate from deprecated gets to fgets with newline removal."
deprecated_function: "gets(buf)"
replacement_function: "fgets(buf, size, stdin)"
languages: ["c"]
deprecated_since: "C99 / removed C11"
---

# [Solution] Deprecated Function Migration: gets to fgets with newline removal

The `gets(buf)` has been deprecated in favor of `fgets(buf, size, stdin)`.

## Migration Guide

gets was removed from C11.

## Before (Deprecated)

```c
gets(buf);
```

## After (Modern)

```c
fgets(buf, sizeof(buf), stdin);
buf[strcspn(buf, "\n")] = '\0';
```

## Key Differences

- fgets with newline removal
