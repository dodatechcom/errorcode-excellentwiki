---
title: "[Solution] Deprecated Function Migration: ioutil.TempDir to os.MkdirTemp"
description: "Migrate from deprecated ioutil.TempDir to os.MkdirTemp."
deprecated_function: "ioutil.TempDir(dir, prefix)"
replacement_function: "os.MkdirTemp(dir, prefix)"
languages: ["go"]
deprecated_since: "Go 1.16+"
---

# [Solution] Deprecated Function Migration: ioutil.TempDir to os.MkdirTemp

The `ioutil.TempDir(dir, prefix)` has been deprecated in favor of `os.MkdirTemp(dir, prefix)`.

## Migration Guide

os.MkdirTemp is the standard.

## Before (Deprecated)

```go
dir, err := ioutil.TempDir("", "prefix")
```

## After (Modern)

```go
dir, err := os.MkdirTemp("", "prefix")
```

## Key Differences

- os.MkdirTemp is the standard
