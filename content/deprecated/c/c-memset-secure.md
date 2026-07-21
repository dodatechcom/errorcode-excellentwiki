---
title: "[Solution] Deprecated Function Migration: memset to explicit_bzero for security"
description: "Migrate from deprecated memset for sensitive data to explicit_bzero."
deprecated_function: "memset(buf, 0, len)"
replacement_function: "explicit_bzero(buf, len)"
languages: ["c"]
deprecated_since: "C11 / POSIX"
---

# [Solution] Deprecated Function Migration: memset to explicit_bzero for security

The `memset(buf, 0, len)` has been deprecated in favor of `explicit_bzero(buf, len)`.

## Migration Guide

Compiler may optimize out memset

memset can be optimized away.

## Before (Deprecated)

```c
memset(password, 0, sizeof(password));
```

## After (Modern)

```c
explicit_bzero(password, sizeof(password));
```

## Key Differences

- explicit_bzero is guaranteed to zero
- memset can be optimized out
