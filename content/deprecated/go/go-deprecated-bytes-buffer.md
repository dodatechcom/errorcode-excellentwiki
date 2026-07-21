---
title: "[Solution] Deprecated Function Migration: bytes.Buffer to strings.Builder"
description: "Migrate from deprecated bytes.Buffer for string building to strings.Builder."
deprecated_function: "bytes.Buffer"
replacement_function: "strings.Builder"
languages: ["go"]
deprecated_since: "Go 1.10+"
---

# [Solution] Deprecated Function Migration: bytes.Buffer to strings.Builder

The `bytes.Buffer` has been deprecated in favor of `strings.Builder`.

## Migration Guide

strings.Builder is more efficient.

## Before (Deprecated)

```go
var buf bytes.Buffer
buf.WriteString("hello")
result := buf.String()
```

## After (Modern)

```go
var builder strings.Builder
builder.WriteString("hello")
result := builder.String()
```

## Key Differences

- strings.Builder is more efficient
