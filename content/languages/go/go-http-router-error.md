---
title: "[Solution] Go http-router Error — How to Fix"
description: "Fix Go http-router errors. Handle route configuration, middleware patterns, and API usage."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go http-router Error

Fix Go http-router errors. Handle route configuration, middleware patterns, and API usage.

## Why It Happens

- http-router does not support method-based routing natively
- Route parameters are not extracted correctly from the URL
- Middleware functions do not have access to route parameters
- http-router configuration conflicts with Go HTTP server

## Common Error Messages

```
router: route already exists
```
```
router: invalid route pattern
```
```
router: method not allowed
```
```
router: path parameter required
```

## How to Fix It

### Solution 1: Use http-router correctly

```go
router := httprouter.New()
router.GET("/user/:id", func(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
    id := ps.ByName("id")
    fmt.Fprintf(w, "User %s", id)
})
```

### Solution 2: Add middleware to http-router

```go
func WithMiddleware(h httprouter.Handle) httprouter.Handle {
    return func(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
        log.Printf("Request: %s %s", r.Method, r.URL.Path)
        h(w, r, ps)
    }
}
router.GET("/api/:path", WithMiddleware(handler))
```

### Solution 3: Handle method not allowed

```go
router.HandleMethodNotAllowed = true
router.MethodNotAllowed = http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
    http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
})
```

### Solution 4: Use with standard library

```go
router := httprouter.New()
log.Fatal(http.ListenAndServe(":8080", router))
```

## Common Scenarios

- http-router does not support middleware natively
- Route parameters are not accessible in standard http.Handler
- Method not allowed is not returned for valid routes with wrong methods

## Prevent It

- Wrap handlers with middleware functions
- Use ps.ByName() to extract route parameters
- Enable HandleMethodNotAllowed for proper 405 responses
