---
title: "[Solution] Deprecated Function Migration: sprintf to snprintf"
description: "Migrate from deprecated sprintf to snprintf."
deprecated_function: "sprintf(buf, fmt, ...)"
replacement_function: "snprintf(buf, size, fmt, ...)"
languages: ["c"]
deprecated_since: "C99"
---

# [Solution] Deprecated Function Migration: sprintf to snprintf

The `sprintf(buf, fmt, ...)` has been deprecated in favor of `snprintf(buf, size, fmt, ...)`.

## Migration Guide

snprintf has bounds checking

sprintf has no bounds checking.

## Before (Deprecated)

```c
char buf[10];
sprintf(buf, "%d", num);
```

## After (Modern)

```c
char buf[10];
int r = snprintf(buf, sizeof(buf), "%d", num);
if (r >= sizeof(buf)) { /* truncated */ }
```

## Key Differences

- Always pass sizeof(buf) as size
- snprintf returns chars that would be written
