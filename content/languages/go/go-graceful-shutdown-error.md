---
title: "[Solution] Go Graceful Shutdown Error — How to Fix"
description: "Fix Go graceful shutdown errors. Handle signal catching, HTTP server shutdown, database cleanup, and deadline management."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Graceful Shutdown Error

Fix Go graceful shutdown errors. Handle signal catching, HTTP server shutdown, database cleanup, and deadline management.

## Why It Happens

- The process receives SIGTERM but no signal handler is registered causing immediate termination
- HTTP server Shutdown is called without a timeout context causing it to hang forever
- Database connections and open files are not cleaned up during shutdown causing resource leaks
- The shutdown deadline is too short and in-flight requests are forcefully terminated

## Common Error Messages

```
signal: terminated
```
```
http: Server closed
```
```
context canceled during shutdown
```
```
shutdown deadline exceeded, forcing exit
```

## How to Fix It

### Solution 1: Implement proper signal handling with context

```go
func main() {
    ctx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
    defer stop()
    srv := &http.Server{Addr: ":8080", Handler: mux}
    go func() {
        if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
            log.Fatalf("listen error: %v", err)
        }
    }()
    <-ctx.Done()
    shutdownCtx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
    defer cancel()
    srv.Shutdown(shutdownCtx)
}
```

### Solution 2: Clean up all resources during shutdown

```go
func (a *App) Shutdown(ctx context.Context) error {
    var errs []error
    if err := a.server.Shutdown(ctx); err != nil { errs = append(errs, err) }
    if err := a.db.Close(); err != nil { errs = append(errs, err) }
    if err := a.redis.Close(); err != nil { errs = append(errs, err) }
    return errors.Join(errs...)
}
```

### Solution 3: Use phased shutdown with increasing urgency

```go
func gracefulShutdown(srv *http.Server, cleanup func()) {
    stopCtx, _ := context.WithTimeout(context.Background(), 10*time.Second)
    srv.Shutdown(stopCtx)
    waitCtx, _ := context.WithTimeout(context.Background(), 20*time.Second)
    select {
    case <-done:
    case <-waitCtx.Done():
    }
    cleanup()
}
```

### Solution 4: Handle health checks during shutdown

```go
func runService(ctx context.Context) error {
    srv := NewServer()
    health := NewHealthChecker(srv)
    health.MarkReady()
    go func() {
        <-ctx.Done()
        health.MarkNotReady()
        time.Sleep(5 * time.Second)
        srv.Shutdown(context.Background())
    }()
    return srv.ListenAndServe()
}
```

## Common Scenarios

- A Kubernetes pod is terminated but the Go process exits immediately dropping in-flight requests
- A long-running HTTP handler blocks shutdown because the context deadline is too short
- A microservice shuts down HTTP but does not close database connections causing connection pool exhaustion

## Prevent It

- Always register signal handlers using signal.NotifyContext for SIGTERM and SIGINT
- Set a shutdown timeout context of 30+ seconds to allow in-flight requests to complete
- Implement a cleanup function that closes all resources in reverse order of initialization
