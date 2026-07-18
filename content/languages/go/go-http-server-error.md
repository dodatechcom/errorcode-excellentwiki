---
title: "[Solution] Go HTTP Server Error — How to Fix"
description: "Fix Go HTTP server errors. Handle server configuration, middleware, graceful shutdown, and timeouts."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go HTTP Server Error

Fix Go HTTP server errors. Handle server configuration, middleware, graceful shutdown, and timeouts.

## Why It Happens

- HTTP server does not shut down gracefully causing dropped requests
- Server timeouts are not configured causing hanging connections
- Middleware does not properly forward requests to next handler
- Server does not start because port is already in use

## Common Error Messages

```
http: server closed before response completed
```
```
http: TLS handshake error
```
```
http: address already in use
```
```
http: timeout
```

## How to Fix It

### Solution 1: Configure HTTP server properly

```go
server := &http.Server{
    Addr:         ":8080",
    Handler:      mux,
    ReadTimeout:  15 * time.Second,
    WriteTimeout: 15 * time.Second,
    IdleTimeout:  60 * time.Second,
}
```

### Solution 2: Graceful shutdown

```go
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()
if err := server.Shutdown(ctx); err != nil {
    log.Fatal(err)
}
```

### Solution 3: Handle TLS

```go
server := &http.Server{
    Addr:    ":443",
    Handler: mux,
}
if err := server.ListenAndServeTLS("cert.pem", "key.pem"); err != nil {
    log.Fatal(err)
}
```

### Solution 4: Use middleware correctly

```go
func logging(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        log.Printf("%s %s", r.Method, r.URL.Path)
        next.ServeHTTP(w, r)
    })
}
```

## Common Scenarios

- Server does not shut down because context timeout is too short
- Connections hang because timeouts are not set
- Middleware breaks the handler chain because next is not called

## Prevent It

- Always set Read, Write, and Idle timeouts
- Call server.Shutdown with a context that has a reasonable timeout
- ['Ensure middleware calls next.ServeHTTP', '```go\nfunc middleware(next http.Handler) http.Handler {\n    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {\n        // Do something before\n        next.ServeHTTP(w, r)\n        // Do something after\n    })\n}\n```']
