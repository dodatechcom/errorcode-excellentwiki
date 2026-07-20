---
title: "[Solution] Mux Route Mismatch Fix"
description: "Fix Gorilla Mux route mismatch errors. Handle route patterns, variables, and middleware."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Mux Route Mismatch

The `gorilla/mux` router fails to match routes when patterns are misconfigured, method restrictions conflict, path variables are named inconsistently, or subrouter mounting strips path prefixes unexpectedly. Mux uses regex-based routing, so similar patterns can cause ambiguous matches.

## Common Causes

```go
// Cause 1: Route pattern ambiguity
r := mux.NewRouter()
r.HandleFunc("/users/{id:[0-9]+}", getUser)
r.HandleFunc("/users/{name}", getUserByName)
// Mux resolves by order, but ambiguous patterns cause confusion

// Cause 2: Method mismatch
r.HandleFunc("/users", createUser).Methods("POST")
// GET /users — no handler, returns 405

// Cause 3: Subrouter path not stripped
sub := r.PathPrefix("/api").Subrouter()
sub.HandleFunc("/users", listUsers) // matches /api/users
// But /api/users/extra does not match

// Cause 4: Trailing slash handling
r.HandleFunc("/users/", listUsers) // exact match with slash
// GET /users — no match, returns 404

// Cause 5: Route registered after first request
go func() {
    time.Sleep(100 * time.Millisecond)
    r.HandleFunc("/late", lateHandler) // concurrent route registration unsafe
}()
```

## How to Fix

### Fix 1: Use unambiguous route patterns

```go
import (
    "fmt"
    "net/http"

    "github.com/gorilla/mux"
)

func main() {
    r := mux.NewRouter()

    r.HandleFunc("/users", listUsers).Methods("GET")
    r.HandleFunc("/users/{id:[0-9]+}", getUser).Methods("GET")
    r.HandleFunc("/users", createUser).Methods("POST")
    r.HandleFunc("/users/{id:[0-9]+}", updateUser).Methods("PUT")
    r.HandleFunc("/users/{id:[0-9]+}", deleteUser).Methods("DELETE")

    http.ListenAndServe(":8080", r)
}
```

### Fix 2: Use proper subrouter setup

```go
func apiRouter() *mux.Router {
    r := mux.NewRouter()
    api := r.PathPrefix("/api/v1").Subrouter()

    api.HandleFunc("/users", listUsers).Methods("GET")
    api.HandleFunc("/users/{id}", getUser).Methods("GET")

    return r
}
```

### Fix 3: Use router.StrictSlash for trailing slash consistency

```go
r := mux.NewRouter()
r.StrictSlash(true) // /users redirects to /users/ or vice versa
r.HandleFunc("/users/", listUsers)
```

## Examples

```go
package main

import (
    "fmt"
    "net/http"

    "github.com/gorilla/mux"
)

func main() {
    r := mux.NewRouter()

    r.HandleFunc("/users", listUsersHandler).Methods("GET")
    r.HandleFunc("/users/{id:[0-9]+}", getUserHandler).Methods("GET")
    r.HandleFunc("/users/{id:[0-9]+}/posts", getUserPostsHandler).Methods("GET")

    http.ListenAndServe(":8080", r)
}

func listUsersHandler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "User list")
}

func getUserHandler(w http.ResponseWriter, r *http.Request) {
    vars := mux.Vars(r)
    fmt.Fprintf(w, "User %s\n", vars["id"])
}

func getUserPostsHandler(w http.ResponseWriter, r *http.Request) {
    vars := mux.Vars(r)
    fmt.Fprintf(w, "Posts for user %s\n", vars["id"])
}
```

## Related Errors

- [http-status-404]({{< relref "/languages/go/http-status-404" >}}) — no route matches the request
- [go-chi-error]({{< relref "/languages/go/go-chi-error" >}}) — Chi router path conflicts
- [go-fiber-error]({{< relref "/languages/go/go-fiber-error" >}}) — Fiber route registration issues
