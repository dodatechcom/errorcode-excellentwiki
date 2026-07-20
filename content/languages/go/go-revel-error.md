---
title: "[Solution] Revel Controller Error Fix"
description: "Fix Revel framework controller errors. Handle request handling, template rendering, and filter chain."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Revel Controller Error

The Revel web framework fails when controller methods have wrong signatures, interceptors do not call `c.Next()`, template rendering fails, or session management is misconfigured. Revel uses a convention-based MVC pattern where controller names and template paths must match.

## Common Causes

```go
// Cause 1: Controller method signature wrong
func (c App) BadIndex() {
    // missing return revel.Result — compile error
}

// Cause 2: Interceptor not calling c.Next()
func init() {
    interceptors.Func(func(c *revel.Controller, fc []revel.Filter) {
        // forgot fc[0](c, fc[1:])
    })
}

// Cause 3: Template not found
return c.Render("user.Name", "user.Age")
// looks for App/Index.html but file is in wrong directory

// Cause 4: Session data not persisted
c.Session["user_id"] = "123"
// session store not configured

// Cause 5: Route parameter name mismatch
// routes file: /users/:id  Controller: App.Show(id int)
```

## How to Fix

### Fix 1: Follow Revel controller conventions

```go
package controllers

import "github.com/revel/revel"

type App struct {
    *revel.Controller
}

func (c App) Index() revel.Result {
    return c.Render()
}

func (c App) Show(id int) revel.Result {
    user := getUser(id)
    return c.Render(user)
}
```

### Fix 2: Use interceptors with proper filter chain

```go
func init() {
    revel.Filters = []revel.Filter{
        revel.PanicFilter,
        revel.RouterFilter,
        revel.FilterConfiguringFilter,
        revel.ParamsFilter,
        SessionFilter,
        revel.InterceptorFilter,
        revel.CompressFilter,
        revel.BeforeAfterFilter,
        revel.ActionInvoker,
    }
}
```

## Examples

```go
package controllers

import "github.com/revel/revel"

type Users struct {
    *revel.Controller
}

func (c Users) List() revel.Result {
    users := []string{"Alice", "Bob"}
    return c.Render(users)
}

func (c Users) Create() revel.Result {
    name := c.Params.Get("name")
    revel.TRACE.Printf("Creating user: %s", name)
    return c.Redirect("/users")
}
```

## Related Errors

- [go-fiber-error]({{< relref "/languages/go/go-fiber-error" >}}) — similar web framework issues
- [go-chi-error]({{< relref "/languages/go/go-chi-error" >}}) — route registration problems
- [template-not-found]({{< relref "/languages/go/go-revel-error" >}}) — template rendering fails
