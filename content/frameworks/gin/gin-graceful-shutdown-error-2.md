---
title: "[Solution] Gin Graceful Shutdown Error -- How to Fix"
description: "Fix Gin graceful shutdown errors. Resolve server shutdown, connection draining, and signal handling issues."
frameworks: ["gin"]
error-types: ["server-error"]
severities: ["error"]
weight: 5
comments: true
---

A Gin graceful shutdown error occurs when the server does not shut down properly, causing dropped requests or resource leaks.

## Why It Happens

Graceful shutdown errors happen due to missing signal handling, abrupt server termination, or not waiting for in-flight requests to complete.

## Common Error Messages

```
server: closed
```

```
use of closed network connection
```

```
context canceled
```

```
interrupt
```

## How to Fix It

### 1. Handle OS Signals

Listen for shutdown signals.

```go
func main() {
    srv := &http.Server{Addr: ":8080", Handler: r}
    go func() {
        if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
            log.Fatalf("listen: %s
", err)
        }
    }()
    quit := make(chan os.Signal, 1)
    signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
    <-quit
    log.Println("Shutting down server...")
    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()
    if err := srv.Shutdown(ctx); err != nil {
        log.Fatal("Server forced to shutdown:", err)
    }
    log.Println("Server exiting")
}
```

### 2. Wait for In-Flight Requests

Use context timeout.

```go
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()
if err := srv.Shutdown(ctx); err != nil {
    log.Fatal("Server forced to shutdown:", err)
}
```

### 3. Close Database Connections

Cleanup resources on shutdown.

```go
if err := srv.Shutdown(ctx); err != nil {
    log.Fatal(err)
}
db.Close()
redis.Close()
```

### 4. Use Health Checks During Shutdown

Mark as unhealthy first.

```go
// In main
<-quit
healthStatus = "shutting_down"
srv.Shutdown(ctx)
```

## Common Scenarios

**Scenario 1: Dropped requests during deploy.**
Ensure proper signal handling.

**Scenario 2: Server hangs on shutdown.**
Set context timeout for shutdown.

## Prevent It

1. **Always implement graceful shutdown.**


2. **Set appropriate shutdown timeout.**


3. **Close all resources on shutdown.**


