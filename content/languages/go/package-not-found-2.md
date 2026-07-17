---
title: "[Solution] Go Package Not Found Error Fix"
description: "Fix Go no required module provides package error. Add missing dependencies, verify import paths, and use go mod tidy."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# Package Not Found Error Fix

The `no required module provides package` error occurs when Go cannot find a module that provides an imported package.

## Description

When Go encounters an `import` statement, it looks for the package in the module cache, vendor directory, and standard library. If the package isn't found in any location, Go reports which package is missing. This often happens after adding a new import without running `go mod tidy`.

Common scenarios:

- **New import not in go.mod** — added `import "github.com/foo/bar"` but forgot to add the dependency.
- **Typo in import path** — misspelled module or package name.
- **Module removed from registry** — dependency was deleted from GitHub.
- **Vendor out of sync** — vendor directory doesn't contain all dependencies.
- **Indirect dependency needed** — package used by a dependency but not directly imported.

## Common Causes

```go
// Cause 1: Import added but not in go.mod
import "github.com/redis/go-redis/v9"

// go.mod doesn't have github.com/redis/go-redis/v9
// Error: no required module provides package github.com/redis/go-redis/v9

// Cause 2: Typo in import path
import "github.com/sirupsen/loggrus" // should be logrus

// Cause 3: Wrong major version
import "github.com/gin-gonic/gin/v3" // doesn't exist

// Cause 4: Module not in go.sum
// Import is correct but go.sum is missing entry
```

## How to Fix

### Fix 1: Run go mod tidy

```bash
go mod tidy
# Automatically adds missing dependencies and removes unused ones
```

### Fix 2: Explicitly add the dependency

```bash
go get github.com/redis/go-redis/v9@latest
```

### Fix 3: Verify import path is correct

```go
// Check the module's documentation for correct import path
// Common mistakes:
// - Wrong version suffix (v2 vs v3)
// - Missing /v2 when module uses major version suffix
// - Case sensitivity in path
```

### Fix 4: Use vendor mode with updated vendor

```bash
go mod vendor
go build -mod=vendor ./...
```

## Examples

```bash
# This triggers: no required module provides package github.com/example/missing
# After adding import "github.com/example/missing" to a .go file:
go build ./...
# Output: no required module provides package github.com/example/missing
```

## Related Errors

- [go-mod-not-found]({{< relref "/languages/go/go-mod-not-found" >}}) — go.mod file not found.
- [go-mod-version]({{< relref "/languages/go/go-mod-version" >}}) — go.mod requires newer Go version.
- [go-sum-mismatch]({{< relref "/languages/go/go-sum-mismatch" >}}) — go.sum checksum mismatch.
