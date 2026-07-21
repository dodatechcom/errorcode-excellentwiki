---
title: "[Solution] Deprecated Function Migration: io/ioutil to io and os packages"
description: "Migrate from deprecated io/ioutil to io and os packages in Go."
deprecated_function: "io/ioutil"
replacement_function: "io / os"
languages: ["go"]
deprecated_since: "Go 1.16+"
---

# [Solution] Deprecated Function Migration: io/ioutil to io and os packages

The `io/ioutil` has been deprecated in favor of `io / os`.

## Migration Guide

The io/ioutil package was deprecated in Go 1.16. Its functions were moved to io and os.

## Before (Deprecated)

```go
import "io/ioutil"

data, err := ioutil.ReadFile("file.txt")
ioutil.WriteFile("out.txt", data, 0644)
resp, err := ioutil.ReadAll(resp.Body)
```

## After (Modern)

```go
import (
    "io"
    "os"
)

data, err := os.ReadFile("file.txt")
os.WriteFile("out.txt", data, 0644)
resp, err := io.ReadAll(resp.Body)
```

## Key Differences

- ioutil.ReadFile -> os.ReadFile
- ioutil.WriteFile -> os.WriteFile
- ioutil.ReadAll -> io.ReadAll
- ioutil.TempDir -> os.MkdirTemp
