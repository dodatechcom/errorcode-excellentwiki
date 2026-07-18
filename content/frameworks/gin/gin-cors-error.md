---
title: "[Solution] Gin CORS Error — How to Fix"
description: "Fix Gin CORS errors. Resolve cross-origin request blocked, missing headers, and preflight issues."
frameworks: ["gin"]
error-types: ["security-error"]
severities: ["error"]
weight: 5
comments: true
---

A Gin CORS error occurs when the browser blocks cross-origin requests due to missing or incorrect CORS headers.

## Why It Happens

CORS errors happen because the server doesn't send proper Access-Control-Allow-Origin headers, doesn't handle preflight OPTIONS requests, or has restrictive CORS configuration.

## Common Error Messages

```
CORS error: No 'Access-Control-Allow-Origin'
```

```
Blocked by CORS policy
```

```
Response to preflight request doesn't pass
```

```
Origin is not allowed by Access-Control-Allow-Origin
```

## How to Fix It

### 1. Enable CORS Middleware

Use gin-contrib/cors for proper CORS handling.

```go
import "github.com/gin-contrib/cors"

r := gin.Default()
r.Use(cors.New(cors.Config{
    AllowOrigins:     []string{"*"},
    AllowMethods:     []string{"GET", "POST", "PUT", "DELETE"},
    AllowHeaders:     []string{"Origin", "Content-Type", "Authorization"},
    AllowCredentials: true,
}))
```

### 2. Handle Preflight Requests

Handle OPTIONS requests manually.

```go
r.OPTIONS("/api/*path", func(c *gin.Context) {
    c.Header("Access-Control-Allow-Origin", "*")
    c.Header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
    c.Header("Access-Control-Allow-Headers", "Content-Type, Authorization")
    c.Status(204)
})
```

### 3. Restrict Origins

Don't use * in production.

```go
r.Use(cors.New(cors.Config{
    AllowOrigins:     []string{"https://myapp.com"},
    AllowMethods:     []string{"GET", "POST"},
    AllowHeaders:     []string{"Content-Type", "Authorization"},
    AllowCredentials: true,
}))
```

### 4. Add Exposed Headers

Expose custom headers to the browser.

```go
r.Use(cors.New(cors.Config{
    ExposeHeaders:    []string{"Content-Length", "X-Request-Id"},
    AllowCredentials: true,
}))
```

## Common Scenarios

**Scenario 1: Browser console shows CORS error.**
Check Access-Control-Allow-Origin header.

**Scenario 2: Preflight request fails.**
Ensure OPTIONS requests are handled.

**Scenario 3: Credentials not sent with CORS.**
Set AllowCredentials to true.

## Prevent It

1. **Always configure CORS explicitly.**


2. **Use allowlists for production origins.**


3. **Handle preflight OPTIONS requests.**


