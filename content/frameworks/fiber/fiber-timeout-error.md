---
title: "[Solution] Fiber Timeout Error -- How to Fix"
description: "Fix Fiber request timeout errors. Resolve handler timeouts, context cancellation, and slow request issues."
frameworks: ["fiber"]
error-types: ["timeout-error"]
severities: ["error"]
weight: 5
comments: true
---

A Fiber timeout error occurs when a request takes too long to process and exceeds the configured timeout limit.

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
app := fiber.New(fiber.Config{
    ReadTimeout:  15 * time.Second,
    WriteTimeout: 15 * time.Second,
    IdleTimeout:  60 * time.Second,
})
```

### 2. Set Handler Timeouts

Add context deadlines in handlers.

```go
func slowHandler(c *fiber.Ctx) error {
    ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
    defer cancel()
    result, err := db.QueryContext(ctx, "SELECT * FROM users")
    if err != nil {
        if ctx.Err() == context.DeadlineExceeded {
            return c.Status(408).JSON(fiber.Map{"error": "timeout"})
        }
        return c.Status(500).JSON(fiber.Map{"error": err.Error()})
    }
    return c.JSON(result)
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
Set appropriate timeouts.

## Prevent It

1. **Set timeouts at every level.**


2. **Use circuit breakers for external services.**


3. **Monitor request latency.**


