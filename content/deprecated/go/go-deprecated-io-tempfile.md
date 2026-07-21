---
title: "[Solution] Deprecated Function Migration: ioutil.TempFile to os.CreateTemp"
description: "Migrate from deprecated ioutil.TempFile to os.CreateTemp."
deprecated_function: "ioutil.TempFile(dir, prefix)"
replacement_function: "os.CreateTemp(dir, prefix)"
languages: ["go"]
deprecated_since: "Go 1.16+"
---

# [Solution] Deprecated Function Migration: ioutil.TempFile to os.CreateTemp

The `ioutil.TempFile(dir, prefix)` has been deprecated in favor of `os.CreateTemp(dir, prefix)`.

## Migration Guide

os.CreateTemp is the standard.

## Before (Deprecated)

```go
f, err := ioutil.TempFile("", "prefix")
```

## After (Modern)

```go
f, err := os.CreateTemp("", "prefix")
```

## Key Differences

- os.CreateTemp is the standard
