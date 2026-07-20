---
title: "[Solution] HTTP 500 Internal Server Error Fix"
description: "Fix Go HTTP 500 internal server error. Handle unhandled errors, panics, and proper error responses."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# HTTP 500 Internal Server Error

A Go HTTP server returns 500 when an unexpected error occurs during request processing. This is a catch-all for server-side failures — the server could not complete the request due to a bug, panic, database error, or misconfiguration.

## Common Causes

```go
// Cause 1: Unhandled panic in handler
func handler(w http.ResponseWriter, r *http.Request) {
    data := getUserData() // may return nil
    fmt.Println(data.Name) // nil pointer panic
}

// Cause 2: Database error not handled
func handler(w http.ResponseWriter, r *http.Request) {
    db.QueryRow("SELECT ...").Scan(&result)
    // error ignored — result may be zero value
}

// Cause 3: Missing error return from helper function
func handler(w http.ResponseWriter, r *http.Request) {
    result := processRequest(r) // returns error but not checked
    json.NewEncoder(w).Encode(result)
}

// Cause 4: Panic from nil interface
var svc *Service
svc.HandleRequest() // nil pointer panic

// Cause 5: File system error
data, _ := os.ReadFile("config.json") // file missing
json.Unmarshal(data, &config) // zero value config
```

## How to Fix

### Fix 1: Add panic recovery middleware

```go
func recoveryMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        defer func() {
            if err := recover(); err != nil {
                log.Printf("panic recovered: %v\n%s", err, debug.Stack())
                http.Error(w, "internal server error", http.StatusInternalServerError)
            }
        }()
        next.ServeHTTP(w, r)
    })
}

func main() {
    mux := http.NewServeMux()
    mux.HandleFunc("/api", apiHandler)
    http.ListenAndServe(":8080", recoveryMiddleware(mux))
}
```

### Fix 2: Handle all errors in handlers

```go
func handler(w http.ResponseWriter, r *http.Request) {
    user, err := getUser(r.Context(), r.URL.Query().Get("id"))
    if err != nil {
        log.Printf("getUser error: %v", err)
        http.Error(w, "internal error", http.StatusInternalServerError)
        return
    }

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(user)
}
```

### Fix 3: Use structured error responses

```go
type ErrorResponse struct {
    Error   string `json:"error"`
    Code    int    `json:"code"`
    Details string `json:"details,omitempty"`
}

func respondError(w http.ResponseWriter, code int, msg string) {
    w.Header().Set("Content-Type", "application/json")
    w.WriteHeader(code)
    json.NewEncoder(w).Encode(ErrorResponse{Error: msg, Code: code})
}
```

## Examples

```go
package main

import (
    "encoding/json"
    "log"
    "net/http"
    "runtime/debug"
)

func main() {
    http.HandleFunc("/api/data", recoveryMiddleware(func(w http.ResponseWriter, r *http.Request) {
        data := map[string]string{"status": "ok"}
        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(data)
    }))

    log.Fatal(http.ListenAndServe(":8080", nil))
}

func recoveryMiddleware(next http.HandlerFunc) http.HandlerFunc {
    return func(w http.ResponseWriter, r *http.Request) {
        defer func() {
            if err := recover(); err != nil {
                log.Printf("panic: %v\n%s", err, debug.Stack())
                http.Error(w, "internal server error", 500)
            }
        }()
        next(w, r)
    }
}
```

## Related Errors

- [panic]({{< relref "/languages/go/invalid-memory-address" >}}) — nil pointer panic in handler
- [broken-pipe]({{< relref "/languages/go/broken-pipe" >}}) — client disconnects during error response
- [goroutine-stack-overflow]({{< relref "/languages/go/goroutine-stack-overflow" >}}) — infinite recursion causes 500
