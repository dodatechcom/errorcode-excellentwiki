---
title: "[Solution] Deprecated Function Migration: signal() to sigaction()"
description: "Migrate from deprecated signal() to sigaction() for portable signal handling."
deprecated_function: "signal(SIGINT, handler)"
replacement_function: "sigaction(SIGINT, &act, NULL)"
languages: ["c"]
deprecated_since: "POSIX"
---

# [Solution] Deprecated Function Migration: signal() to sigaction()

The `signal(SIGINT, handler)` has been deprecated in favor of `sigaction(SIGINT, &act, NULL)`.

## Migration Guide

sigaction provides more control

signal() behavior varies between systems.

## Before (Deprecated)

```c
signal(SIGINT, handler);
```

## After (Modern)

```c
struct sigaction sa;
sa.sa_handler = handler;
sigemptyset(&sa.sa_mask);
Sa.flags = 0;
sigaction(SIGINT, &sa, NULL);
```

## Key Differences

- sigaction is portable
- signal() behavior varies
