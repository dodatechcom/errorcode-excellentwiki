---
title: "[Solution] Deprecated Function Migration: json.Marshal to json.NewEncoder"
description: "Migrate from deprecated json.Marshal for streaming to json.NewEncoder."
deprecated_function: "json.Marshal(v)"
replacement_function: "json.NewEncoder(w).Encode(v)"
languages: ["go"]
deprecated_since: "Go 1.0+"
---

# [Solution] Deprecated Function Migration: json.Marshal to json.NewEncoder

The `json.Marshal(v)` has been deprecated in favor of `json.NewEncoder(w).Encode(v)`.

## Migration Guide

json.NewEncoder handles streaming.

## Before (Deprecated)

```go
data, err := json.Marshal(v)
w.Write(data)
```

## After (Modern)

```go
err := json.NewEncoder(w).Encode(v)
```

## Key Differences

- json.NewEncoder handles streaming
