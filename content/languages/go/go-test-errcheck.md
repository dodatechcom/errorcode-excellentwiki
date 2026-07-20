---
title: "[Solution] Go test errcheck error — Testing Error Fix"
description: "Fix Go test error checking."
languages: ["go"]
error-types: ["testing-error"]
severities: ["error"]
weight: 5
---

# Go test errcheck Error

The `errcheck` linter reports unchecked errors in Go code. errstatic analyzes code paths where error return values are ignored, which can lead to silent failures, resource leaks, or security vulnerabilities. This is not a runtime error but a static analysis finding during testing.

## Common Causes

```go
// Cause 1: Ignoring error from os.File operations
file, _ := os.Create("output.txt") // errcheck: error not checked
file.Write(data)

// Cause 2: Ignoring error from fmt.Fprintf
fmt.Fprintf(w, "hello") // errcheck: unchecked error

// Cause 3: Ignoring defer errors
defer file.Close() // Close may return error that is lost

// Cause 4: Ignoring error from sql operations
db.Exec("INSERT INTO users (name) VALUES (?)", "Alice") // error ignored

// Cause 5: Ignoring error from json encoding
json.NewEncoder(w).Encode(data) // encoder error not checked
```

## How to Fix

### Fix 1: Check all errors explicitly

```go
func writeOutput(path string, data []byte) error {
    file, err := os.Create(path)
    if err != nil {
        return fmt.Errorf("create file: %w", err)
    }
    defer file.Close()

    _, err = file.Write(data)
    if err != nil {
        return fmt.Errorf("write data: %w", err)
    }

    return file.Close()
}
```

### Fix 2: Use errcheck with explicit error handling

```go
func handleResponse(w http.ResponseWriter, data interface{}) {
    if err := json.NewEncoder(w).Encode(data); err != nil {
        log.Printf("encode error: %v", err)
        http.Error(w, "internal error", http.StatusInternalServerError)
        return
    }
}
```

### Fix 3: Use errcheck directive for intentional ignores

```go
//nolint:errcheck // error intentionally ignored in cleanup
defer os.Remove(tempFile)
```

### Fix 4: Configure errcheck in golangci-lint

```yaml
# .golangci.yml
linters:
  enable:
    - errcheck
linters-settings:
  errcheck:
    check-type-assertions: true
    check-blank: false
```

## Examples

```go
package main

import (
    "encoding/json"
    "fmt"
    "log"
    "net/http"
)

func main() {
    http.HandleFunc("/users", func(w http.ResponseWriter, r *http.Request) {
        users := []string{"Alice", "Bob"}

        w.Header().Set("Content-Type", "application/json")
        if err := json.NewEncoder(w).Encode(users); err != nil {
            log.Printf("encode error: %v", err)
            http.Error(w, "encoding error", http.StatusInternalServerError)
            return
        }
    })

    log.Fatal(http.ListenAndServe(":8080", nil))
}
```

## Related Errors

- [panic]({{< relref "/languages/go/invalid-memory-address" >}}) — unchecked nil pointer dereference
- [deadlock]({{< relref "/languages/go/deadlock" >}}) — unchecked channel errors cause goroutine leaks
- [go-dlv-error]({{< relref "/languages/go/go-dlv-error" >}}) — debugger issues with error handling
