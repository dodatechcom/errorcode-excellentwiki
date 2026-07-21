---
title: "[Solution] Deprecated Function Migration: ioutil.Discard to io.Discard"
description: "Migrate from deprecated ioutil.Discard to io.Discard."
deprecated_function: "ioutil.Discard"
replacement_function: "io.Discard"
languages: ["go"]
deprecated_since: "Go 1.16+"
---

# [Solution] Deprecated Function Migration: ioutil.Discard to io.Discard

The `ioutil.Discard` has been deprecated in favor of `io.Discard`.

## Migration Guide

io.Discard is the standard.

## Before (Deprecated)

```go
io.Copy(ioutil.Discard, r)
```

## After (Modern)

```go
io.Copy(io.Discard, r)
```

## Key Differences

- io.Discard is the standard
