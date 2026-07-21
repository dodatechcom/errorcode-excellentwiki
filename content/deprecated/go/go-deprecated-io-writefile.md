---
title: "[Solution] Deprecated Function Migration: ioutil.WriteFile to os.WriteFile"
description: "Migrate from deprecated ioutil.WriteFile to os.WriteFile."
deprecated_function: "ioutil.WriteFile(path, data, perm)"
replacement_function: "os.WriteFile(path, data, perm)"
languages: ["go"]
deprecated_since: "Go 1.16+"
---

# [Solution] Deprecated Function Migration: ioutil.WriteFile to os.WriteFile

The `ioutil.WriteFile(path, data, perm)` has been deprecated in favor of `os.WriteFile(path, data, perm)`.

## Migration Guide

os.WriteFile is the standard.

## Before (Deprecated)

```go
err := ioutil.WriteFile(path, data, 0644)
```

## After (Modern)

```go
err := os.WriteFile(path, data, 0644)
```

## Key Differences

- os.WriteFile is the standard
