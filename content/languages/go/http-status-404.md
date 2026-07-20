---
title: "[Solution] HTTP 404 Page Not Found Fix"
description: "Fix Go HTTP 404 not found errors. Handle missing routes, URL patterns, and middleware configuration."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# HTTP 404 Page Not Found

A Go HTTP server returns 404 when no registered handler matches the request path. In `net/http`, this happens when `http.DefaultServeMux` or a custom mux has no matching route. With routers like `gorilla/mux` or `chi`, 404 occurs when routes are misconfigured or trailing slashes cause mismatches.

## Common Causes

```go
// Cause 1: Handler not registered for the path
http.HandleFunc("/users", listUsers)
// GET /users/123 returns 404 — no pattern for /users/{id}

// Cause 2: Trailing slash mismatch
http.HandleFunc("/users", handler)
// GET /users/ returns 301 redirect to /users

// Cause 3: ServeMux trailing slash requirement
mux := http.NewServeMux()
mux.HandleFunc("/api/", apiHandler) // matches /api/anything
// GET /api returns 404 — must be /api/ with trailing slash

// Cause 4: Wrong HTTP method
http.HandleFunc("/users", func(w http.ResponseWriter, r *http.Request) {
    if r.Method != http.MethodGet {
        http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
    }
})
// POST /users returns 405

// Cause 5: Routes registered after server starts
go registerRoutes()
http.ListenAndServe(":8080", nil) // race condition
```

## How to Fix

### Fix 1: Use a proper router with path parameters

```go
import (
    "fmt"
    "net/http"

    "github.com/gorilla/mux"
)

func main() {
    r := mux.NewRouter()
    r.HandleFunc("/users", listUsers).Methods("GET")
    r.HandleFunc("/users/{id}", getUser).Methods("GET")
    r.HandleFunc("/users", createUser).Methods("POST")

    r.NotFoundHandler = http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        http.Error(w, "page not found", http.StatusNotFound)
    })

    http.ListenAndServe(":8080", r)
}

func getUser(w http.ResponseWriter, r *http.Request) {
    vars := mux.Vars(r)
    fmt.Fprintf(w, "User %s", vars["id"])
}
```

### Fix 2: Register all routes before starting the server

```go
func main() {
    r := http.NewServeMux()
    registerRoutes(r)

    fmt.Println("Server starting on :8080")
    log.Fatal(http.ListenAndServe(":8080", r))
}

func registerRoutes(mux *http.ServeMux) {
    mux.HandleFunc("/", home)
    mux.HandleFunc("/about", about)
}
```

### Fix 3: Add custom 404 handler

```go
mux := http.NewServeMux()
mux.HandleFunc("/users", listUsers)

http.ListenAndServe(":8080", mux)
```

## Examples

```go
package main

import (
    "fmt"
    "log"
    "net/http"
    "strings"
)

func main() {
    mux := http.NewServeMux()
    mux.HandleFunc("/", homeHandler)
    mux.HandleFunc("/users", usersHandler)
    mux.HandleFunc("/users/", userHandler)

    log.Fatal(http.ListenAndServe(":8080", mux))
}

func homeHandler(w http.ResponseWriter, r *http.Request) {
    if r.URL.Path != "/" {
        http.NotFound(w, r)
        return
    }
    fmt.Fprintln(w, "Home page")
}

func usersHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "User list")
}

func userHandler(w http.ResponseWriter, r *http.Request) {
    id := strings.TrimPrefix(r.URL.Path, "/users/")
    if id == "" {
        http.NotFound(w, r)
        return
    }
    fmt.Fprintf(w, "User: %s\n", id)
}
```

## Related Errors

- [go-mux-error]({{< relref "/languages/go/go-mux-error" >}}) — gorilla/mux route mismatch
- [go-chi-error]({{< relref "/languages/go/go-chi-error" >}}) — Chi router path conflicts
- [http-status-405]({{< relref "/languages/go/http-status-404" >}}) — method not allowed on valid path
