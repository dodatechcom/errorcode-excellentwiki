---
title: "[Solution] Go go.sum Mismatch Error Fix"
description: "Fix Go go.sum mismatch error. Delete and regenerate go.sum, verify module integrity, and understand checksum database."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["go", "mod", "sum", "checksum", "integrity", "runtime"]
weight: 5
---

# go.sum Mismatch Error Fix

The `go.sum mismatch` error occurs when the checksums in `go.sum` don't match the downloaded module contents.

## Description

Go's module system uses `go.sum` to verify that downloaded modules haven't been tampered with. Each module version has an expected hash. When a module's contents don't match the stored hash, Go refuses to proceed. The Go checksum database (`sum.golang.org`) provides authoritative hashes.

Common scenarios:

- **Corrupted download** — network issue during module download.
- **Module republished** — author re-tagged the same version with different content.
- **Manual go.sum edit** — someone modified go.sum incorrectly.
- **Proxy inconsistency** — module proxy serves different content than origin.
- **Private module with wrong sum** — internal module with stale checksum.

## Common Causes

```bash
# Cause 1: Corrupted module cache
go mod download
# go.sum mismatch

# Cause 2: Module content changed after tag
# Author force-pushed a tag
go mod tidy
# go.sum mismatch for module@v1.2.3

# Cause 3: Manual go.sum edit
# Someone removed or modified entries in go.sum
go build
# go.sum mismatch

# Cause 4: Private module proxy issues
GONOSUMCHECK=private.company.com go mod download
# Still gets mismatch if local cache is stale
```

## How to Fix

### Fix 1: Delete and regenerate go.sum

```bash
rm go.sum
go mod tidy
```

### Fix 2: Clear module cache

```bash
go clean -modcache
go mod download
```

### Fix 3: Use GONOSUMDB for private modules

```bash
# Skip checksum database for private modules
export GONOSUMDB=private.company.com
export GONOSUMCHECK=private.company.com
go mod tidy
```

### Fix 4: Use GONOSUMCHECK for specific modules

```bash
# Skip sum check for specific module
GONOSUMCHECK=github.com/myorg/mymodule go mod tidy
```

## Examples

```bash
# This triggers: go: go.sum mismatch
# (after manually editing go.sum or corrupted cache)
echo "invalid" > go.sum
go build ./...
# go.sum has unexpected content
```

## Related Errors

- [go-mod-not-found]({{< relref "/languages/go/go-mod-not-found" >}}) — go.mod file not found.
- [go-mod-version]({{< relref "/languages/go/go-mod-version" >}}) — go.mod requires newer Go version.
- [package-not-found]({{< relref "/languages/go/package-not-found" >}}) — required module provides no package.
