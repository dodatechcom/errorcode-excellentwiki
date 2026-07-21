---
title: "[Solution] Deprecated Function Migration: strings.Replace to strings.ReplaceAll"
description: "Migrate from deprecated strings.Replace with -1 count to strings.ReplaceAll."
deprecated_function: "strings.Replace(s, old, new, -1)"
replacement_function: "strings.ReplaceAll(s, old, new)"
languages: ["go"]
deprecated_since: "Go 1.12+"
---

# [Solution] Deprecated Function Migration: strings.Replace to strings.ReplaceAll

The `strings.Replace(s, old, new, -1)` has been deprecated in favor of `strings.ReplaceAll(s, old, new)`.

## Migration Guide

strings.ReplaceAll is simpler.

## Before (Deprecated)

```go
result := strings.Replace(s, "old", "new", -1)
```

## After (Modern)

```go
result := strings.ReplaceAll(s, "old", "new")
```

## Key Differences

- strings.ReplaceAll is simpler
