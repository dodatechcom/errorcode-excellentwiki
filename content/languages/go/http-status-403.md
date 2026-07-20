---
title: "[Solution] HTTP 403 Forbidden Fix"
description: "Fix Go HTTP 403 forbidden errors. Handle authorization failures, access control, and permission issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# HTTP 403 Forbidden

A Go HTTP server returns 403 Forbidden when the client is authenticated but does not have permission to access the requested resource. This is different from 401 Unauthorized — the client has valid credentials but the server explicitly denies access.

## Common Causes

```go
// Cause 1: Auth middleware checks permissions but denies
func adminOnly(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        role := getUserRole(r)
        if role != "admin" {
            http.Error(w, "forbidden", http.StatusForbidden)
            return
        }
        next.ServeHTTP(w, r)
    })
}

// Cause 2: CORS preflight blocked
// Browser sends OPTIONS request, server does not handle it

// Cause 3: File permissions on served directory
// os.Open returns permission denied for restricted files

// Cause 4: Rate limiting returns 403
// Client exceeded rate limit

// Cause 5: CSRF token validation fails
// Token missing or expired
```

## How to Fix

### Fix 1: Implement role-based access control

```go
func requireRole(roles []string, next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        userRole := getUserRole(r)
        allowed := false
        for _, role := range roles {
            if userRole == role {
                allowed = true
                break
            }
        }
        if !allowed {
            http.Error(w, `{"error":"forbidden"}`, http.StatusForbidden)
            return
        }
        next.ServeHTTP(w, r)
    })
}

// Usage
http.Handle("/admin", requireRole([]string{"admin"}, adminHandler))
```

### Fix 2: Add CORS handling

```go
func corsMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        w.Header().Set("Access-Control-Allow-Origin", "*")
        w.Header().Set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
        w.Header().Set("Access-Control-Allow-Headers", "Content-Type, Authorization")

        if r.Method == http.MethodOptions {
            w.WriteHeader(http.StatusOK)
            return
        }
        next.ServeHTTP(w, r)
    })
}
```

### Fix 3: Serve files with proper permissions

```go
func fileServer(w http.ResponseWriter, r *http.Request) {
    path := filepath.Join("./public", filepath.Clean(r.URL.Path))
    info, err := os.Stat(path)
    if os.IsNotExist(err) || info.IsDir() {
        http.NotFound(w, r)
        return
    }
    http.ServeFile(w, r, path)
}
```

## Examples

```go
package main

import (
    "fmt"
    "net/http"
)

func main() {
    mux := http.NewServeMux()
    mux.Handle("/admin", requireRole([]string{"admin"}, adminHandler))
    mux.Handle("/api/data", requireRole([]string{"user", "admin"}, dataHandler))
    http.ListenAndServe(":8080", mux)
}

func adminHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "Admin dashboard")
}

func dataHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "Protected data")
}
```

## Related Errors

- [http-status-401]({{< relref "/languages/go/http-status-401" >}}) — authentication required but not provided
- [go-vault-error]({{< relref "/languages/go/go-vault-error" >}}) — Vault permission denied
- [grpc-permission]({{< relref "/languages/go/grpc-permission" >}}) — gRPC permission denied
