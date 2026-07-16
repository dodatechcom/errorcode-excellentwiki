---
title: "[Solution] Go go.sum Mismatch Error Fix"
description: "Fix Go go.sum mismatch error. Update go.sum with go mod download, verify module integrity, and handle corrupted downloads."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["go", "sum", "checksum", "module", "verify"]
weight: 5
---

# Go: go.sum Mismatch — Fix

A go.sum mismatch error occurs when the checksum of a downloaded module doesn't match the expected value in `go.sum`.

## Description

Go uses `go.sum` to verify module integrity. Each module and its hash are recorded. If the downloaded module has a different hash — due to corruption, proxy issues, or module tampering — Go refuses to build with a mismatch error.

Common scenarios:

- **Corrupted module cache** — downloaded module is damaged.
- **Proxy serving wrong version** — module proxy returns incorrect content.
- **Module re-published** — author replaced a tag with different code.
- **Network issues** — partial download during module fetch.
- **Manual go.sum edits** — accidentally modified checksum file.

## Common Causes

```bash
# Cause 1: Corrupted module cache
go mod download
# github.com/some/module@v1.0.0: go.sum mismatch

# Cause 2: Module proxy issue
GOPROXY=https://proxy.golang.org,direct go mod download
# Checksum mismatch

# Cause 3: Module re-tagged
# Author published v1.0.0, then re-published with different code
go mod download
# go.sum has old checksum, new download has new checksum

# Cause 4: Manual go.sum edit
# Editing go.sum by hand corrupts the checksums
```

## How to Fix

### Fix 1: Delete go.sum and regenerate

```bash
# Wrong — trying to fix individual checksum
vim go.sum

# Correct — regenerate from scratch
rm go.sum
go mod tidy
```

### Fix 2: Clear module cache and re-download

```bash
# Clear corrupted cache
go clean -modcache

# Re-download all modules
go mod download

# Verify checksums
go mod verify
```

### Fix 3: Use direct download instead of proxy

```bash
# If proxy is serving wrong content
GOPROXY=direct go mod download

# Or use specific proxy
GOPROXY=https://proxy.golang.org,direct go mod download
```

### Fix 4: Pin specific module versions

```go
// go.mod — be explicit about versions
module github.com/username/myproject

go 1.21

require (
    github.com/some/module v1.0.0  // Exact version, not v1.0.x
)
```

### Fix 5: Use GONOSUMCHECK for private modules

```bash
# For private modules that aren't in sum database
GONOSUMCHECK=github.com/private/* go mod download

# Or set GONOSUMDB
GONOSUMDB=github.com/private/* go mod download
```

### Fix 6: Verify module integrity

```bash
# Check all module checksums
go mod verify

# Download and verify specific module
go mod download github.com/some/module@v1.0.0
```

## Examples

```bash
# This triggers: go.sum mismatch
rm go.sum
# Manually create wrong go.sum
echo "wrong checksum" > go.sum
go mod download
# Error: go.sum mismatch
```

## Related Errors

- [go-mod-not-found]({{< relref "/languages/go/go-mod-not-found" >}}) — go.mod file not found.
- [go-mod-version]({{< relref "/languages/go/go-mod-version" >}}) — Go version mismatch.
- [package-not-found]({{< relref "/languages/go/package-not-found" >}}) — required package not found.
