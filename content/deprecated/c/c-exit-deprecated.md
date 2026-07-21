---
title: "[Solution] Deprecated Function Migration: exit() to return from main"
description: "Migrate from deprecated exit() to return from main."
deprecated_function: "exit(1)"
replacement_function: "return 1"
languages: ["c"]
deprecated_since: "Best Practice"
---

# [Solution] Deprecated Function Migration: exit() to return from main

The `exit(1)` has been deprecated in favor of `return 1`.

## Migration Guide

return from main is cleaner.

## Before (Deprecated)

```c
int main() {
    if (error) exit(1);
}
```

## After (Modern)

```c
int main() {
    if (error) return 1;
}
```

## Key Differences

- return from main is cleaner
