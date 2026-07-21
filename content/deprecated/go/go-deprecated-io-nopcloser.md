---
title: "[Solution] Deprecated Function Migration: ioutil.NopCloser to io.NopCloser"
description: "Migrate from deprecated ioutil.NopCloser to io.NopCloser."
deprecated_function: "ioutil.NopCloser(r)"
replacement_function: "io.NopCloser(r)"
languages: ["go"]
deprecated_since: "Go 1.16+"
---

# [Solution] Deprecated Function Migration: ioutil.NopCloser to io.NopCloser

The `ioutil.NopCloser(r)` has been deprecated in favor of `io.NopCloser(r)`.

## Migration Guide

io.NopCloser is the standard.

## Before (Deprecated)

```go
rc := ioutil.NopCloser(r)
```

## After (Modern)

```go
rc := io.NopCloser(r)
```

## Key Differences

- io.NopCloser is the standard
