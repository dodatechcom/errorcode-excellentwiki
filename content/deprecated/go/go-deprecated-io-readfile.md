---
title: "[Solution] Deprecated Function Migration: ioutil.ReadFile to os.ReadFile"
description: "Migrate from deprecated ioutil.ReadFile to os.ReadFile."
deprecated_function: "ioutil.ReadFile(path)"
replacement_function: "os.ReadFile(path)"
languages: ["go"]
deprecated_since: "Go 1.16+"
---

# [Solution] Deprecated Function Migration: ioutil.ReadFile to os.ReadFile

The `ioutil.ReadFile(path)` has been deprecated in favor of `os.ReadFile(path)`.

## Migration Guide

os.ReadFile is the standard.

## Before (Deprecated)

```go
data, err := ioutil.ReadFile(path)
```

## After (Modern)

```go
data, err := os.ReadFile(path)
```

## Key Differences

- os.ReadFile is the standard
