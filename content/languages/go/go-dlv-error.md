---
title: "[Solution] Delve Debug Error Fix"
description: "Fix Delve debugger errors. Handle breakpoint issues, symbol resolution, and remote debugging."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Delve Debug Error

The Delve debugger (`dlv`) fails when the binary is not compiled with debug symbols, the Go version is unsupported, the debuggee is optimized (compiled with `-ldflags="-s -w"`), or the target process exits unexpectedly. Delve requires unoptimized binaries for line-level debugging.

## Common Causes

```go
// Cause 1: Binary compiled with optimization flags
// go build -ldflags="-s -w" -o app
// could not open debug info — stripped binary

// Cause 2: Race detector conflicts with Delve
// go build -race -o app
// Some race detector behaviors interfere with breakpoints

// Cause 3: Wrong Go version
// Delve v1.21+ requires Go 1.21+
// dlv: Unsupported Go version

// Cause 4: Remote debugging connection refused
// dlv connect :2345
// Could not connect to debug server

// Cause 5: Binary architecture mismatch
// Compiled on amd64, debugging on arm64
// dlv: ELF executable not found
```

## How to Fix

### Fix 1: Build binary without optimization

```bash
# Build with debug symbols
go build -gcflags="all=-N -l" -o app ./cmd/server

# Or use make with debug target
make debug
```

### Fix 2: Start Delve correctly for local debugging

```bash
# Debug main package
dlv debug ./cmd/server

# Debug test
dlv test ./pkg/handler

# Debug running process
dlv attach <pid>

# Start headless server for remote debugging
dlv exec ./app --headless --listen=:2345 --api-version=2

# Connect from another terminal
dlv connect :2345
```

### Fix 3: Use Delve API programmatically

```go
import (
    "github.com/go-delve/delve/service"
    "github.com/go-delve/delve/service/dap"
)

func startDebugger(path string) error {
    // Start DAP server for VS Code integration
    server := dap.NewServer(&service.Config{
        ExecutablePath: path,
        Headless:       true,
        Listen:         "127.0.0.1:40000",
    })
    return server.Serve()
}
```

## Examples

```bash
# Install Delve
go install github.com/go-delve/delve/cmd/dlv@latest

# Debug a Go program
dlv debug ./cmd/server

# In Delve debugger:
(dlv) break main.main
(dlv) continue
(dlv) next
(dlv) print variableName
(dlv) locals
(dlv) goroutines
(dlv) stack
```

## Related Errors

- [go-build-error]({{< relref "/languages/go/go-build-error" >}}) — compilation issues before debugging
- [panic]({{< relref "/languages/go/invalid-memory-address" >}}) — crashes during debug session
- [goroutine-stack-overflow]({{< relref "/languages/go/goroutine-stack-overflow" >}}) — stack overflow visible in Delve
