---
title: "[Solution] HTTP 503 Service Unavailable in Go Fix"
description: "Fix HTTP 503 Service Unavailable errors in Go. Handle overloaded services, maintenance modes, and graceful degradation."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# HTTP 503: Service Unavailable in Go

This error occurs when a Go service returns 503 because it's temporarily unable to handle the request due to overload, maintenance, or dependency failure.

## What This Error Means

Common error messages:

- `503 Service Unavailable`
- `connection refused` (server not accepting connections)
- `server is at capacity`
- `Retry-After: 30`

A 503 indicates the service is temporarily unavailable but should be available later. Clients can retry after a delay indicated by the `Retry-After` header.

## Common Causes

```go
// Cause 1: Server overloaded (too many concurrent requests)
// No connection limiter, goroutine count exceeds capacity

// Cause 2: Dependency down (database, Redis, etc.)
// Health check fails, service returns 503

// Cause 3: Deployment in progress
// Server shutting down during rolling update

// Cause 4: Circuit breaker open
// Too many upstream failures, circuit opened

// Cause 5: Rate limiting active
// Server throttling requests
```

## How to Fix

### Fix 1: Add connection limiting with semaphore

```go
var sem = make(chan struct{}, 100) // max 100 concurrent requests

func handler(w http.ResponseWriter, r *http.Request) {
    select {
    case sem <- struct{}{}:
        defer func() { <-sem }()
    default:
        w.Header().Set("Retry-After", "5")
        http.Error(w, "Service Unavailable", 503)
        return
    }

    // Process request
    processRequest(w, r)
}
```

### Fix 2: Implement health checks

```go
var isHealthy int32

func healthHandler(w http.ResponseWriter, r *http.Request) {
    if atomic.LoadInt32(&isHealthy) == 0 {
        w.Header().Set("Retry-After", "30")
        http.Error(w, "Service Unavailable", 503)
        return
    }
    w.WriteHeader(http.StatusOK)
    json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
}

func setHealthy(healthy bool) {
    if healthy {
        atomic.StoreInt32(&isHealthy, 1)
    } else {
        atomic.StoreInt32(&isHealthy, 0)
    }
}
```

### Fix 3: Add graceful shutdown

```go
func main() {
    srv := &http.Server{Addr: ":8080"}

    go func() {
        if err := srv.ListenAndServe(); err != http.ErrServerClosed {
            log.Fatalf("Server error: %v", err)
        }
    }()

    quit := make(chan os.Signal, 1)
    signal.Notify(quit, syscall.SIGTERM, syscall.SIGINT)
    <-quit

    log.Println("Shutting down server...")

    // Wait for in-flight requests to complete
    ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()

    if err := srv.Shutdown(ctx); err != nil {
        log.Printf("Shutdown error: %v", err)
    }
}
```

### Fix 4: Implement circuit breaker

```go
type CircuitBreaker struct {
    failures  int
    threshold int
    open      bool
    mu        sync.Mutex
}

func (cb *CircuitBreaker) Allow() bool {
    cb.mu.Lock()
    defer cb.mu.Unlock()
    return !cb.open
}

func (cb *CircuitBreaker) RecordFailure() {
    cb.mu.Lock()
    defer cb.mu.Unlock()
    cb.failures++
    if cb.failures >= cb.threshold {
        cb.open = true
        go func() {
            time.Sleep(30 * time.Second)
            cb.mu.Lock()
            cb.open = false
            cb.failures = 0
            cb.mu.Unlock()
        }()
    }
}
```

### Fix 5: Return Retry-After header

```go
func overloadedHandler(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Retry-After", "10")
    http.Error(w, "Service Unavailable", 503)
}
```

## Examples

```
$ curl http://localhost:8080/api/data
HTTP/1.1 503 Service Unavailable
Retry-After: 30
Content-Type: text/plain
Service Unavailable
```

```go
// Fix: check dependencies before accepting requests
func middleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        if err := db.Ping(); err != nil {
            w.Header().Set("Retry-After", "5")
            http.Error(w, "Service Unavailable", 503)
            return
        }
        next.ServeHTTP(w, r)
    })
}
```

## Related Errors

- [http-status-502]({{< relref "/languages/go/go-http-status-502" >}}) — bad gateway
- [go-http-timeout-v2]({{< relref "/languages/go/go-http-timeout-v2" >}}) — context deadline exceeded
- [http-status-429]({{< relref "/languages/go/http-status-429" >}}) — too many requests
