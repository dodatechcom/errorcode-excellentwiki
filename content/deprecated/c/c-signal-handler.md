---
title: "[Solution] Deprecated Function Migration: signal() to sigaction() for signal handling"
description: "Migrate from deprecated signal() to sigaction() for portable signal handling."
deprecated_function: "signal(SIGINT, handler)"
replacement_function: "sigaction(SIGINT, &act, NULL)"
languages: ["c"]
deprecated_since: "POSIX"
---

# [Solution] Deprecated Function Migration: signal() to sigaction() for signal handling

The `signal(SIGINT, handler)` has been deprecated in favor of `sigaction(SIGINT, &act, NULL)`.

## Migration Guide

sigaction provides more control and portability

signal() behavior varies between systems. sigaction provides consistent behavior.

## Before (Deprecated)

```c
void handler(int sig) {
    // handle signal
}

signal(SIGINT, handler);  // behavior varies
```

## After (Modern)

```c
void handler(int sig) {
    // handle signal
}

struct sigaction sa;
sa.sa_handler = handler;
sigemptyset(&sa.sa_mask);
sa.sa_flags = 0;
sigaction(SIGINT, &sa, NULL);  // portable
```

## Key Differences

- sigaction is portable across POSIX systems
- signal() behavior varies by platform
- sigaction provides more control
- Always use sigaction for signal handling
