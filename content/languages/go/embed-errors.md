---
title: "[Solution] Go embed: errors — Embedding Error Fix"
description: "Fix Go embed directive errors."
languages: ["go"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# embed errors

The `//go:embed` directive can fail with invalid patterns, missing files, or using `..` in paths.

## Common Causes

- **File not found** — pattern doesn't match any files
- **Using `..`** — `//go:embed ../file` is not allowed
- **Large files** — embedded file exceeds 100MB default

## How to Fix

### Fix 1: Ensure files exist

```go
//go:embed static/
var staticFS embed.FS
```

### Fix 2: Use valid patterns

```go
//go:embed *.html
templateFS embed.FS
```

## Related Errors

- [file-not-found]({{< relref "/languages/go/file-not-found" >}}) — file not found.
- [permission-denied]({{< relref "/languages/go/permission-denied" >}}) — permission denied.
