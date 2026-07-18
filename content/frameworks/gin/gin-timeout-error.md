---
title: "[Solution] Gin Timeout Error — How to Fix"
description: "Fix Gin request timeout errors. Resolve handler timeouts, context cancellation, and slow request issues."
frameworks: ["gin"]
error-types: ["timeout-error"]
severities: ["error"]
weight: 5
comments: true
---

A Gin timeout error occurs when a request takes too long to process and exceeds the configured timeout limit.

## Why It Happens

Timeout errors happen due to slow database queries, external API calls, missing context deadlines, or resource exhaustion.

## Common Error Messages

```
context deadline exceeded
```

```
i/o timeout
```

```
request timeout
```

```
client disconnected
```

## How to Fix It

### 1. Set Server Timeouts

Configure read/write timeouts.

```go
srv := &http.Server{
    Addr:         ":8080",
    Handler:      r,
    ReadTimeout:  15 * time.Second,
    WriteTimeout: 15 * time.Second,
    IdleTimeout:  60 * time.Second,
}
srv.ListenAndServe()
```

### 2. Set Handler Timeouts

Add context deadlines in handlers.

```go
func slowHandler(c *gin.Context) {
    ctx, cancel := context.WithTimeout(c.Request.Context(), 10*time.Second)
    defer cancel()
    result, err := db.QueryContext(ctx, "SELECT * FROM users")
    if err != nil {
        if ctx.Err() == context.DeadlineExceeded {
            c.JSON(408, gin.H{"error": "timeout"})
            return
        }
        c.JSON(500, gin.H{"error": err.Error()})
        return
    }
    c.JSON(200, result)
}
```

### 3. Use Timeouts with External Calls

Set timeouts for API calls.

```go
client := &http.Client{Timeout: 5 * time.Second}
req, _ := http.NewRequest("GET", "https://api.example.com", nil)
resp, err := client.Do(req)
```

### 4. Implement Circuit Breaker

Prevent cascading timeouts.

```go
type CircuitBreaker struct {
    failures int
    state    string
    mu       sync.Mutex
}
```

## Common Scenarios

**Scenario 1: Requests timing out.**
Check for slow queries or external calls.

**Scenario 2: Server crashes under load.**
Set appropriate timeouts and limits.

## Prevent It

1. **Set timeouts at every level.**


2. **Use circuit breakers for external services.**


3. **Monitor request latency.**


