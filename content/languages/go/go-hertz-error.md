---
title: "[Solution] Hertz HTTP Error Fix"
description: "Fix Hertz HTTP framework errors. Handle request processing, routing, and middleware issues."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Hertz HTTP Error

The Hertz framework (by CloudWeGo) fails during route registration, request binding, or middleware execution when routes conflict, `context.Request` is used incorrectly, or custom middleware does not call `ctx.Next()`. Hertz is built on `netpoll`, not `net/http`.

## Common Causes

```go
// Cause 1: Duplicate route registration
h.GET("/users", listUsers)
h.GET("/users", listUsers) // panic

// Cause 2: Binding to wrong type or missing tags
type Req struct {
    Name string `json:"name" query:"name"` // ambiguous
}

// Cause 3: Writing after handler returns
go func() {
    c.JSON(200, map[string]string{"msg": "late"}) // crash
}()

// Cause 4: Not calling ctx.Next() in middleware
func myMiddleware(ctx context.Context, c *app.RequestContext) {
    // forgot c.Next(ctx)
}

// Cause 5: Using net/http handler signature with Hertz
func badHandler(w http.ResponseWriter, r *http.Request) {} // wrong
```

## How to Fix

### Fix 1: Set up routes before h.Run()

```go
import (
    "context"

    "github.com/cloudwego/hertz/pkg/app"
    "github.com/cloudwego/hertz/pkg/app/server"
)

func main() {
    h := server.Default()

    h.GET("/users", listUsers)
    h.POST("/users", createUser)

    h.Spin()
}

func listUsers(ctx context.Context, c *app.RequestContext) {
    c.JSON(200, []string{"alice", "bob"})
}
```

### Fix 2: Use proper middleware pattern

```go
func AuthMiddleware() app.HandlerFunc {
    return func(ctx context.Context, c *app.RequestContext) {
        token := c.GetHeader("Authorization")
        if token == "" {
            c.AbortWithStatusJSON(401, map[string]string{"error": "unauthorized"})
            return
        }
        c.Next(ctx)
    }
}
```

## Examples

```go
package main

import (
    "context"

    "github.com/cloudwego/hertz/pkg/app"
    "github.com/cloudwego/hertz/pkg/app/server"
    "github.com/cloudwego/hertz/pkg/common/consts"
)

func main() {
    h := server.Default()

    h.GET("/", func(ctx context.Context, c *app.RequestContext) {
        c.String(consts.StatusOK, "Hello Hertz!")
    })

    h.Spin()
}
```

## Related Errors

- [broken-pipe]({{< relref "/languages/go/broken-pipe" >}}) — netpoll connection closed
- [context-deadline-exceeded]({{< relref "/languages/go/context-deadline" >}}) — handler times out
- [http-status-404]({{< relref "/languages/go/http-status-404" >}}) — unmatched route
