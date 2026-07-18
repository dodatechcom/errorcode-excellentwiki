---
title: "[Solution] Gin Graceful Shutdown Error — How to Fix"
description: "Fix Gin graceful shutdown errors. Resolve server shutdown and connection draining issues."
frameworks: ["gin"]
error-types: ["server-error"]
severities: ["error"]
weight: 5
comments: true
---

A Gin graceful shutdown error occurs when the server does not shut down properly, causing dropped requests.

## Why It Happens

Graceful shutdown errors happen due to missing signal handling or abrupt server termination.

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
    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
    defer cancel()
    srv.Shutdown(ctx)
}
```

### 2. Wait for In-Flight Requests

Use context timeout.

```go
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()
srv.Shutdown(ctx)
```

### 3. Close Resources

Cleanup on shutdown.

```go
srv.Shutdown(ctx)
db.Close()
redis.Close()
```

### 4. Mark Unhealthy

Stop accepting traffic first.

```go
<-quit
healthStatus = "shutting_down"
srv.Shutdown(ctx)
```

## Common Scenarios

**Scenario 1: Dropped requests during deploy.**


**Scenario 2: Server hangs on shutdown.**


## Prevent It

1. **Always implement graceful shutdown.**


2. **Set shutdown timeout.**


3. **Close all resources.**


