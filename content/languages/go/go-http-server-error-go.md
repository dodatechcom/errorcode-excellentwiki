---
title: "[Solution] Go HTTP Server Error — How to Fix"
description: "Fix Go net/http server errors. Handle listen failures, handler panics, TLS configuration, request timeouts, and connection limits."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go HTTP Server Error

Fix Go net/http server errors. Handle listen failures, handler panics, TLS configuration, request timeouts, and connection limits.

## Why It Happens

- The server tries to bind to a port already in use by another process
- An HTTP handler panics without recovery middleware crashing the entire server
- ReadTimeout and WriteTimeout are not set causing slow clients to hold connections indefinitely
- TLS certificate files are missing or have incorrect permissions

## Common Error Messages

```
listen tcp :8080: bind: address already in use
```
```
http: panic serving <addr>: <panic>
```
```
http: TLS handshake error: tls: bad certificate
```
```
context deadline exceeded (Client.Timeout exceeded)
```

## How to Fix It

### Solution 1: Configure the server with all necessary timeouts

```go
srv := &http.Server{
    Addr: ":8080", Handler: mux,
    ReadTimeout:  15 * time.Second,
    WriteTimeout: 15 * time.Second,
    IdleTimeout:  60 * time.Second,
    MaxHeaderBytes: 1 << 20,
}
log.Fatal(srv.ListenAndServe())
```

### Solution 2: Add panic recovery middleware

```go
func RecoverMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        defer func() {
            if err := recover(); err != nil {
                log.Printf("panic recovered: %v\n%s", err, debug.Stack())
                http.Error(w, "Internal Server Error", http.StatusInternalServerError)
            }
        }()
        next.ServeHTTP(w, r)
    })
}
```

### Solution 3: Use ListenAndServeTLS for HTTPS

```go
log.Fatal(srv.ListenAndServeTLS("cert.pem", "key.pem"))
```

### Solution 4: Limit concurrent connections

```go
type ConnLimiter struct {
    sem chan struct{}
}
func (l *ConnLimiter) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    select {
    case l.sem <- struct{}{}:
        defer func() { <-l.sem }()
        l.handler.ServeHTTP(w, r)
    default:
        http.Error(w, "Too Many Requests", http.StatusServiceUnavailable)
    }
}
```

## Common Scenarios

- A production server crashes because an unhandled panic kills the process
- Slowloris attacks exhaust connections because ReadTimeout is not configured
- The server fails to start because another process is already on port 8080

## Prevent It

- Always set ReadTimeout, WriteTimeout, and IdleTimeout on http.Server
- Wrap all HTTP handlers with panic recovery middleware
- Use lsof or ss to check port availability before starting
