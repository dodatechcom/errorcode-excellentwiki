---
title: "[Solution] Fiber Graceful Shutdown Error -- How to Fix"
description: "Fix Fiber graceful shutdown errors. Resolve server shutdown, connection draining, and signal handling issues."
frameworks: ["fiber"]
error-types: ["server-error"]
severities: ["error"]
weight: 5
comments: true
---

A Fiber graceful shutdown error occurs when the server does not shut down properly, causing dropped requests or resource leaks.

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
app := fiber.New()
go func() {
    if err := app.Listen(":8080"); err != nil {
        log.Printf("listen error: %v", err)
    }
}()

quit := make(chan os.Signal, 1)
signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
<-quit
if err := app.Shutdown(); err != nil {
    log.Fatal(err)
}
```

### 2. Wait for In-Flight Requests

Use Shutdown with timeout.

```go
ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
defer cancel()
if err := app.ShutdownWithContext(ctx); err != nil {
    log.Fatal(err)
}
```

### 3. Close Database Connections

Cleanup resources on shutdown.

```go
if err := app.Shutdown(); err != nil {
    log.Fatal(err)
}
db.Close()
redis.Close()
```

### 4. Use Health Checks During Shutdown

Mark as unhealthy first.

```go
<-quit
healthStatus = "shutting_down"
app.Shutdown()
```

## Common Scenarios

**Scenario 1: Dropped requests during deploy.**
Ensure proper signal handling.

**Scenario 2: Server hangs on shutdown.**
Set context timeout.

## Prevent It

1. **Always implement graceful shutdown.**


2. **Set appropriate shutdown timeout.**


3. **Close all resources on shutdown.**


