---
title: "[Solution] Deprecated Function Migration: ioutil.ReadAll(req.Body) to io.ReadAll"
description: "Migrate from deprecated ioutil.ReadAll(req.Body) to io.ReadAll."
deprecated_function: "ioutil.ReadAll(req.Body)"
replacement_function: "io.ReadAll(req.Body)"
languages: ["go"]
deprecated_since: "Go 1.16+"
---

# [Solution] Deprecated Function Migration: ioutil.ReadAll(req.Body) to io.ReadAll

The `ioutil.ReadAll(req.Body)` has been deprecated in favor of `io.ReadAll(req.Body)`.

## Migration Guide

io.ReadAll is the standard.

## Before (Deprecated)

```go
body, err := ioutil.ReadAll(req.Body)
```

## After (Modern)

```go
body, err := io.ReadAll(req.Body)
```

## Key Differences

- io.ReadAll is the standard
