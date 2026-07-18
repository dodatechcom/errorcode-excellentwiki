---
title: "[Solution] Go Cross-Compilation Error — How to Fix"
description: "Fix Go cross-compilation errors. Handle GOOS/GOARCH, CGO dependencies, and build constraints."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Cross-Compilation Error

Fix Go cross-compilation errors. Handle GOOS/GOARCH, CGO dependencies, and build constraints.

## Why It Happens

- CGO cannot compile for target platform because of missing cross-compiler
- Build constraints exclude files for the target platform
- System dependencies like SQLite cannot be cross-compiled without CGO_ENABLED=0
- Go version differences cause different compilation results

## Common Error Messages

```
go build: cgo required
```
```
go build: build constraints exclude all Go files
```
```
go build: unknown architecture
```
```
go build: unknown operating system
```

## How to Fix It

### Solution 1: Cross-compile without CGO

```bash
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o myapp-linux-amd64
CGO_ENABLED=0 GOOS=darwin GOARCH=arm64 go build -o myapp-darwin-arm64
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build -o myapp.exe
```

### Solution 2: Use build constraints

```go
//go:build linux && amd64
package main

func init() { runtime.GOMAXPROCS(4) }
```

### Solution 3: Cross-compile with CGO

```bash
# Install cross-compiler
apt install gcc-aarch64-linux-gnu
# Build
CGO_ENABLED=1 CC=aarch64-linux-gnu-gcc GOOS=linux GOARCH=arm64 go build
```

### Solution 4: Use GoReleaser for multi-platform builds

```yaml
# .goreleaser.yml
builds:
  - goos:
      - linux
      - darwin
      - windows
    goarch:
      - amd64
      - arm64
    env:
      - CGO_ENABLED=0
```

## Common Scenarios

- Cross-compilation fails because CGO is required but cross-compiler is not available
- Build fails because build constraints exclude all files for the target platform
- Cross-compiled binary does not run because of wrong GOARCH

## Prevent It

- Use CGO_ENABLED=0 for pure Go binaries that need cross-compilation
- Install cross-compiler toolchains for CGO cross-compilation
- Use build tags to handle platform-specific code
