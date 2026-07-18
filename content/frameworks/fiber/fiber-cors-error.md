---
title: "[Solution] Fiber CORS Error — How to Fix"
description: "Fix Fiber CORS errors. Resolve cross-origin request blocked, missing headers, and preflight issues."
frameworks: ["fiber"]
error-types: ["security-error"]
severities: ["error"]
weight: 5
comments: true
---

A Fiber CORS error occurs when the browser blocks cross-origin requests due to missing or incorrect CORS headers.

## Why It Happens

CORS errors happen because the server doesn't send proper Access-Control-Allow-Origin headers or doesn't handle preflight OPTIONS requests.

## Common Error Messages

```
CORS error: No Access-Control-Allow-Origin
```

```
Blocked by CORS policy
```

```
Response to preflight request doesn't pass
```

```
Origin is not allowed
```

## How to Fix It

### 1. Enable CORS Middleware

Use fiber-contrib/cors.

```go
import "github.com/gofiber/fiber/v2/middleware/cors"

app.Use(cors.New(cors.Config{
    AllowOrigins: "*",
    AllowMethods: "GET,POST,PUT,DELETE",
    AllowHeaders: "Origin,Content-Type,Authorization",
}))
```

### 2. Configure CORS Properly

Set specific origins for production.

```go
app.Use(cors.New(cors.Config{
    AllowOrigins: "https://myapp.com",
    AllowMethods: "GET,POST,PUT,DELETE",
    AllowHeaders: "Content-Type,Authorization",
    AllowCredentials: true,
}))
```

### 3. Handle Preflight Requests

Handle OPTIONS requests.

```go
app.Options("/*", func(c *fiber.Ctx) error {
    c.Set("Access-Control-Allow-Origin", "*")
    c.Set("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE")
    return c.SendStatus(204)
})
```

### 4. Set Exposed Headers

Expose custom headers.

```go
app.Use(cors.New(cors.Config{
    ExposeHeaders: "Content-Length,X-Request-Id",
}))
```

## Common Scenarios

**Scenario 1: Browser console shows CORS error.**
Check Access-Control-Allow-Origin header.

**Scenario 2: Preflight request fails.**
Ensure OPTIONS requests are handled.

## Prevent It

1. **Always configure CORS explicitly.**


2. **Use allowlists for production origins.**


3. **Handle preflight OPTIONS requests.**


