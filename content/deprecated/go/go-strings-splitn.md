---
title: "[Solution] Deprecated Function Migration: strings.Split to strings.Cut"
description: "Migrate from deprecated strings.Split patterns to strings.Cut in Go."
deprecated_function: "strings.SplitN(s, sep, 2)"
replacement_function: "strings.Cut(s, sep)"
languages: ["go"]
deprecated_since: "Go 1.18+"
---

# [Solution] Deprecated Function Migration: strings.Split to strings.Cut

The `strings.SplitN(s, sep, 2)` has been deprecated in favor of `strings.Cut(s, sep)`.

## Migration Guide

strings.Cut is cleaner for splitting a string into exactly two parts.

## Before (Deprecated)

```go
parts := strings.SplitN("key=value", "=", 2)
if len(parts) == 2 {
    key := parts[0]
    value := parts[1]
}
```

## After (Modern)

```go
key, value, ok := strings.Cut("key=value", "=")
if ok {
    fmt.Println(key, value)
}

// Or without checking ok
before, _, _ := strings.Cut("key=value", "=")
```

## Key Differences

- strings.Cut returns (before, after, found)
- Cleaner than SplitN with len check
- Returns empty string for after if not found
- Available since Go 1.18
