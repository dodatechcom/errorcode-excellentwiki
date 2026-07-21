---
title: "[Solution] Deprecated Function Migration: gets() to fgets()"
description: "Migrate from removed gets() to fgets()."
deprecated_function: "gets(buf)"
replacement_function: "fgets(buf, size, stdin)"
languages: ["c"]
deprecated_since: "C11 removed"
---

# [Solution] Deprecated Function Migration: gets() to fgets()

The `gets(buf)` has been deprecated in favor of `fgets(buf, size, stdin)`.

## Migration Guide

gets has no bounds checking

gets was removed from C11.

## Before (Deprecated)

```c
gets(buf);
```

## After (Modern)

```c
fgets(buf, sizeof(buf), stdin);
```

## Key Differences

- fgets takes size parameter
- gets is removed from C11
