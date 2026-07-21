---
title: "[Solution] Fiber Health Check Error -- How to Fix"
description: "Fix Fiber health check errors. Resolve readiness and liveness probe failures."
frameworks: ["fiber"]
error-types: ["monitoring-error"]
severities: ["warning"]
weight: 5
comments: true
---

A Fiber health check error occurs when health endpoints fail or return incorrect status.

## Why It Happens

Health check errors happen due to missing health endpoints, incorrect status codes, or missing dependency checks.

## Common Error Messages

```
health check failed
```

```
readiness probe failed
```

```
liveness probe failed
```

```
service unavailable
```

## How to Fix It

### 1. Add Health Endpoints

Create readiness and liveness probes.

```go
app.Get("/healthz", func(c *fiber.Ctx) error {
    return c.JSON(fiber.Map{"status": "ok"})
})

app.Get("/readyz", func(c *fiber.Ctx) error {
    if err := db.Ping(); err != nil {
        return c.Status(503).JSON(fiber.Map{"status": "not ready"})
    }
    return c.JSON(fiber.Map{"status": "ready"})
})
```

### 2. Check Dependencies

Verify database, Redis, etc.

```go
app.Get("/readyz", func(c *fiber.Ctx) error {
    checks := fiber.Map{"db": checkDB(), "redis": checkRedis()}
    for name, ok := range checks {
        if !ok {
            return c.Status(503).JSON(fiber.Map{"status": "not ready", "failed": name})
        }
    }
    return c.JSON(fiber.Map{"status": "ready"})
})
```

### 3. Add Timeout to Health Checks

Don't let health checks hang.

```go
func checkDB() bool {
    ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
    defer cancel()
    return db.PingContext(ctx) == nil
}
```

### 4. Return Proper Status Codes

Use 200 for healthy, 503 for unhealthy.

```go
return c.JSON(fiber.Map{"status": "healthy"})
return c.Status(503).JSON(fiber.Map{"status": "unhealthy"})
```

## Common Scenarios

**Scenario 1: Health check always fails.**
Check dependency availability.

**Scenario 2: Health check slow.**
Add timeouts to checks.

## Prevent It

1. **Implement both liveness and readiness.**


2. **Add dependency checks.**


3. **Set timeouts on health checks.**


