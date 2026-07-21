---
title: "Embedded static file missing"
description: "Go embed static files are not found at runtime because the embed directive path does not match the actual directory structure"
frameworks: ['gin']
error-types: ['runtime-error']
severities: ["error"]
weight: 5
---

This error occurs when go embed static files are not found at runtime because the embed directive path does not match the actual directory structure.

## Common Causes

- Missing or misconfigured middleware in the Gin engine setup
- Incorrect route definitions or parameter binding configuration
- Environment-specific configuration not loaded for the deployment
- Go version incompatibility with Gin framework features
- Network or filesystem permissions blocking required resources
- Improper error handling in the request lifecycle chain

## How to Fix

1. Verify your Gin engine configuration:

```go
package main

import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()
    // Ensure middleware is registered correctly
    r.GET("/health", func(c *gin.Context) {
        c.JSON(200, gin.H{"status": "ok"})
    })
    r.Run(":8080")
}
```

2. Check middleware registration order:

```go
func setupRouter() *gin.Engine {
    r := gin.New()
    r.Use(gin.Logger())
    r.Use(gin.Recovery())
    // Add custom middleware after defaults
    r.Use(corsMiddleware())
    return r
}
```

3. Validate request binding:

```go
type LoginRequest struct {
    Username string `json:"username" binding:"required"`
    Password string `json:"password" binding:"required"`
}

func loginHandler(c *gin.Context) {
    var req LoginRequest
    if err := c.ShouldBindJSON(&req); err != nil {
        c.JSON(400, gin.H{"error": err.Error()})
        return
    }
    // Process login
}
```

## Examples

```go
// Common mistake: not returning after sending an error response
func handler(c *gin.Context) {
    if err := validate(c); err != nil {
        c.JSON(400, gin.H{"error": err.Error()})
        // Missing return here causes double write
    }
    c.JSON(200, gin.H{"result": "ok"})
}
```

```text
[ERROR] gin-gonic/gin superfluous response.WriteHeader call
```

## Prevention

1. Always return after sending an error response in handlers
2. Use gin.Recovery middleware to handle unexpected panics gracefully
3. Write integration tests that exercise the full middleware chain
4. Pin Go and Gin versions in go.mod to avoid surprise upgrades
