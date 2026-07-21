---
title: "[Solution] Deprecated Function Migration: ioutil.TempDir to os.MkdirTemp"
description: "Migrate from deprecated ioutil.TempDir to os.MkdirTemp."
deprecated_function: "ioutil.TempDir()"
replacement_function: "os.MkdirTemp()"
languages: ["go"]
deprecated_since: "Go 1.16+"
---

# [Solution] Deprecated Function Migration: ioutil.TempDir to os.MkdirTemp

The `ioutil.TempDir("", "prefix")` has been deprecated in favor of `os.MkdirTemp("", "prefix")`.

## Migration Guide

ioutil functions moved to os

ioutil.TempDir was deprecated in Go 1.16.

## Before (Deprecated)

```go
import "io/ioutil"
dir, err := ioutil.TempDir("", "prefix")
```

## After (Modern)

```go
import "os"
dir, err := os.MkdirTemp("", "prefix")
```

## Key Differences

- os.MkdirTemp is the replacement
- Same signature and behavior
