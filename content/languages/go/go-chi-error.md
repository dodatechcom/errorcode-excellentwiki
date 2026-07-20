---
title: "[Solution] Chi Route Not Found Fix"
description: "Fix Chi router route not found errors. Handle route patterns, middleware groups, and URL parameters."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Chi Route Not Found

The Chi router returns 404 or panics when routes are not registered correctly, URL parameter patterns are mismatched, or sub-router mounting strips path prefixes unexpectedly. Chi uses a radix tree router where overlapping patterns cause conflicts.

## Common Causes

```go
// Cause 1: Route registered after first request
go func() {
    time.Sleep(100 * time.Millisecond)
    r.Get("/late", handler) // Chi not safe for concurrent route changes
}()

// Cause 2: Subrouter mount path stripping
sub := chi.NewRouter()
sub.Get("/", listItems)
r.Mount("/items", sub) // sub does not see /items prefix

// Cause 3: Using wrong HTTP method
r.Post("/users", createUser)
http.Get("/users") // 405

// Cause 4: Missing trailing slash
r.Get("/users", listUsers)
// GET /users/ redirects to /users
```

## How to Fix

### Fix 1: Set up all routes before starting server

```go
import "github.com/go-chi/chi/v5"

func main() {
    r := chi.NewRouter()
    r.Use(middleware.Logger)

    r.Get("/users", listUsers)
    r.Post("/users", createUser)
    r.Get("/users/{id}", getUser)

    http.ListenAndServe(":3000", r)
}
```

### Fix 2: Use chi.URLParam

```go
func getUser(w http.ResponseWriter, r *http.Request) {
    id := chi.URLParam(r, "id")
    fmt.Fprintf(w, "User: %s", id)
}
```

### Fix 3: Use RouteGroup for sub-routers

```go
func apiRoutes() chi.Router {
    r := chi.NewRouter()
    r.Route("/users", func(r chi.Router) {
        r.Get("/", listUsers)
        r.Post("/", createUser)
        r.Get("/{id}", getUser)
    })
    return r
}
```

## Examples

```go
package main

import (
    "fmt"
    "net/http"

    "github.com/go-chi/chi/v5"
    "github.com/go-chi/chi/v5/middleware"
)

func main() {
    r := chi.NewRouter()
    r.Use(middleware.Logger)
    r.Use(middleware.Recoverer)

    r.Route("/articles", func(r chi.Router) {
        r.Get("/", listArticles)
        r.Post("/", createArticle)
        r.Get("/{articleID}", getArticle)
    })

    http.ListenAndServe(":3000", r)
}

func listArticles(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "listing articles")
}

func getArticle(w http.ResponseWriter, r *http.Request) {
    id := chi.URLParam(r, "articleID")
    fmt.Fprintf(w, "article %s\n", id)
}
```

## Related Errors

- [http-status-404]({{< relref "/languages/go/http-status-404" >}}) — generic 404
- [go-mux-error]({{< relref "/languages/go/go-mux-error" >}}) — gorilla/mux route mismatch
- [broken-pipe]({{< relref "/languages/go/broken-pipe" >}}) — client disconnects
