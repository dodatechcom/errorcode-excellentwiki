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

ioutil is deprecated

ioutil.ReadAll was deprecated in Go 1.16.

## Before (Deprecated)

```go
import "io/ioutil"
data, err := ioutil.ReadAll(resp.Body)
```

## After (Modern)

```go
import "io"
data, err := io.ReadAll(resp.Body)
```

## Key Differences

- io.ReadAll is the direct replacement
- import io instead of io/ioutil
