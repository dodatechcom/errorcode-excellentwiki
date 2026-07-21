---
title: "[Solution] Deprecated Function Migration: exit() in signal handlers to _exit()"
description: "Migrate from deprecated exit() in signal handlers to _exit()."
deprecated_function: "exit(status)"
replacement_function: "_exit(status)"
languages: ["c"]
deprecated_since: "POSIX"
---

# [Solution] Deprecated Function Migration: exit() in signal handlers to _exit()

The `exit(status)` has been deprecated in favor of `_exit(status)`.

## Migration Guide

exit() is not async-signal-safe

exit() calls atexit handlers which are not async-signal-safe. _exit is safe in signal handlers.

## Before (Deprecated)

```c
void handler(int sig) {
    cleanup();
    exit(1);  // not async-signal-safe
}
```

## After (Modern)

```c
void handler(int sig) {
    // Only async-signal-safe operations here
    _exit(1);  // async-signal-safe
}
```

## Key Differences

- _exit is async-signal-safe
- exit() calls atexit handlers
- Only use async-signal-safe functions in handlers
- Write cleanup code before entering signal handler
