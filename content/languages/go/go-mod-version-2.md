---
title: "[Solution] Go go.mod Version Mismatch Fix"
description: "Fix Go go.mod requires go >= X error. Update your Go installation, downgrade the go directive, or use toolchain directives."
languages: ["go"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# go.mod Version Mismatch Error Fix

The `go.mod requires go >= X` error occurs when the `go` directive in `go.mod` specifies a version higher than the installed Go toolchain.

## Description

The `go.mod` file contains a `go` directive specifying the minimum Go version required by the module. When you run Go commands with an older toolchain, it refuses to build because it may not support features used by the module. Go 1.21+ added the `toolchain` directive for automatic toolchain downloading.

Common scenarios:

- **Newer go.mod on older machine** — teammate uses Go 1.22, you have Go 1.20.
- **CI/CD environment outdated** — build server has older Go installed.
- **Toolchain directive present** — go.mod specifies a specific toolchain.
- **Feature gating** — code uses generics or other version-specific features.

## Common Causes

```bash
# Cause 1: go.mod requires newer version
# go.mod has: go 1.22
go build ./...
# go: go.mod requires go >= 1.22.0 (running go 1.21.0)

# Cause 2: toolchain directive specifies newer version
# go.mod has: toolchain go1.22.1
go build ./...
# go: go.mod requires toolchain go1.22.1

# Cause 3: Minor version mismatch
# go.mod has: go 1.21.5
# Installed: go 1.21.0
go build ./...
# go: go.mod requires go >= 1.21.5

# Cause 4: GOTOOLCHAIN set to local
export GOTOOLCHAIN=local
go build ./... # fails instead of downloading
```

## How to Fix

### Fix 1: Update Go to the required version

```bash
# Check current version
go version

# Download from https://go.dev/dl/
# Or use Go install script
go install golang.org/dl/go1.22.0@latest
```

### Fix 2: Downgrade go.mod directive (if features allow)

```go
// go.mod — change:
// go 1.22
// to:
// go 1.20
```

### Fix 3: Allow automatic toolchain download

```bash
# Let Go download the required toolchain automatically
export GOTOOLCHAIN=auto

# Or in go.mod, specify a toolchain
// go.mod
// go 1.20
// toolchain go1.22.0
```

### Fix 4: Use GOTOOLCHAIN environment

```bash
# Force a specific toolchain
GOTOOLCHAIN=go1.22.0 go build ./...

# Use local only
GOTOOLCHAIN=local go build ./...
```

## Examples

```bash
# This triggers: go: go.mod requires go >= 1.22.0 (running go 1.21.0)
# go.mod contains: go 1.22
go version  # go1.21.0
go build ./...
```

## Related Errors

- [go-mod-not-found]({{< relref "/languages/go/go-mod-not-found" >}}) — go.mod file not found.
- [go-sum-mismatch]({{< relref "/languages/go/go-sum-mismatch" >}}) — go.sum checksum mismatch.
- [package-not-found]({{< relref "/languages/go/package-not-found" >}}) — required module provides no package.
