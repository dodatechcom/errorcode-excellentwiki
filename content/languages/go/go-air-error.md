---
title: "[Solution] Air Reload Error Fix"
description: "Fix Air live reload errors. Handle file watching, configuration issues, and process management."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Air Reload Error

The `air` live-reload tool for Go fails to reload when the configuration file is wrong, the watched directory has too many files, the build command produces errors, or the temp directory is not writable. Air monitors file changes and rebuilds the Go binary automatically during development.

## Common Causes

```go
// Cause 1: air.toml configuration wrong
// build.bin = "./tmp/main" but tmp directory does not exist
// build.cmd = "go build -o ./tmp/main" fails silently

// Cause 2: File watcher hits system limit
// inotify watches exhausted on Linux
// too many open files

// Cause 3: Build errors not surfacing
// air rebuilds but binary is stale
// build error log not captured

// Cause 4: Go module vendor issues
// air tries to build but vendor directory is stale
// go mod vendor not run after adding dependencies

// Cause 5: Permission denied on temp directory
// air cannot write to ./tmp/
```

## How to Fix

### Fix 1: Configure air.toml properly

```toml
# .air.toml
root = "."
tmp_dir = "tmp"

[build]
  bin = "./tmp/main"
  cmd = "go build -o ./tmp/main ./cmd/server"
  delay = 1000
  exclude_dir = ["tmp", "vendor", "node_modules"]
  exclude_regex = ["_test.go"]
  include_ext = ["go", "toml", "yaml"]
  kill_delay = "0s"
  send_interrupt = false
  stop_on_error = true

[color]
  build = "yellow"
  main = "magenta"
  runner = "green"
  watcher = "cyan"

[log]
  time = false
```

### Fix 2: Increase inotify watches on Linux

```bash
# Check current limit
cat /proc/sys/fs/inotify/max_user_watches
# Increase limit
echo 524288 | sudo tee /proc/sys/fs/inotify/max_user_watches
```

### Fix 3: Use air with proper error handling

```bash
# Install air
go install github.com/air-verse/air@latest

# Run with verbose output
air -v

# Run with specific config file
air -c .air.toml
```

## Examples

```bash
# Install air
go install github.com/air-verse/air@latest

# Create .air.toml
cat > .air.toml << 'EOF'
root = "."
tmp_dir = "tmp"

[build]
  cmd = "go build -o ./tmp/main ./cmd/server"
  bin = "./tmp/main"
  delay = 1000
  exclude_dir = ["tmp", "vendor"]
  include_ext = ["go"]
EOF

# Run air
air
```

## Related Errors

- [go-build-error]({{< relref "/languages/go/go-build-error" >}}) — Go build failures that air may surface
- [file-exists]({{< relref "/languages/go/file-exists" >}}) — file operation errors during reload
- [go-work-error]({{< relref "/languages/go/go-work-error" >}}) — Go workspace issues affecting builds
