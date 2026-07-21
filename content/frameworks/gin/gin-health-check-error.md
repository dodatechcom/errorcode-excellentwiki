---
title: "[Solution] Gin Health Check Error -- How to Fix"
description: "Fix Gin health check errors. Resolve readiness and liveness probe failures."
frameworks: ["gin"]
error-types: ["monitoring-error"]
severities: ["warning"]
weight: 5
comments: true
---

A Gin health check error occurs when health endpoints fail or return incorrect status.

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
r.GET("/healthz", func(c *gin.Context) {
    c.JSON(200, gin.H{"status": "ok"})
})

r.GET("/readyz", func(c *gin.Context) {
    if err := db.Ping(); err != nil {
        c.JSON(503, gin.H{"status": "not ready", "error": err.Error()})
        return
    }
    c.JSON(200, gin.H{"status": "ready"})
})
```

### 2. Check Dependencies

Verify database, Redis, etc.

```go
r.GET("/readyz", func(c *gin.Context) {
    checks := map[string]bool{
        "db":      checkDB(),
        "redis":   checkRedis(),
        "rabbitmq": checkRabbitMQ(),
    }
    for name, ok := range checks {
        if !ok {
            c.JSON(503, gin.H{"status": "not ready", "failed": name})
            return
        }
    }
    c.JSON(200, gin.H{"status": "ready"})
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
c.JSON(200, gin.H{"status": "healthy"})  // Healthy
c.JSON(503, gin.H{"status": "unhealthy"}) // Unhealthy
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


