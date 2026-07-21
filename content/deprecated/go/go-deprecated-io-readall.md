---
title: "[Solution] Deprecated Function Migration: ioutil.ReadAll to io.ReadAll"
description: "Migrate from deprecated ioutil.ReadAll to io.ReadAll."
deprecated_function: "ioutil.ReadAll(r)"
replacement_function: "io.ReadAll(r)"
languages: ["go"]
deprecated_since: "Go 1.16+"
---

# [Solution] Deprecated Function Migration: ioutil.ReadAll to io.ReadAll

The `ioutil.ReadAll(r)` has been deprecated in favor of `io.ReadAll(r)`.

## Migration Guide

io.ReadAll is the standard.

## Before (Deprecated)

```go
data, err := ioutil.ReadAll(r)
```

## After (Modern)

```go
data, err := io.ReadAll(r)
```

## Key Differences

- io.ReadAll is the standard
