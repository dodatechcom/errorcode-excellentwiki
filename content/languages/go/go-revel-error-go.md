---
title: "[Solution] Go Revel Error — How to Fix"
description: "Fix Go Revel errors. Handle framework configuration, controller lifecycle, template rendering, and interceptors."
languages: ["go"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Go Revel Error

Fix Go Revel errors. Handle framework configuration, controller lifecycle, template rendering, and interceptors.

## Why It Happens

- Revel controller is not properly configured causing missing dependency injection
- Template rendering fails because of incorrect template path configuration
- Interceptor is not registered causing lifecycle hooks to not execute
- Revel application does not start because of missing configuration

## Common Error Messages

```
revel: controller not found
```
```
revel: template not found
```
```
revel: invalid configuration
```
```
revel: filter chain error
```

## How to Fix It

### Solution 1: Configure Revel properly

```go
// app/controllers/app.go
type App struct {
    *revel.Controller
}
func (c App) Index() revel.Result {
    return c.Render()
}
```

### Solution 2: Use Revel interceptors

```go
revel.OnAppStart(initDB)
revel.InterceptMethod((*App).CheckAuth, revel.BEFORE)
revel.InterceptFunc(myFilter, revel.BEFORE, revel.ControllerType{})
```

### Solution 3: Handle template rendering

```go
func (c App) Index() revel.Result {
    users := []string{"Alice", "Bob"}
    return c.Render(users)
}
// templates/App/Index.html: {{.users}}
```

### Solution 4: Register routes

```go
// conf/routes:
// GET / Index App.Index
// POST /api/users Api.CreateUser
```

## Common Scenarios

- Revel controller cannot access database because of missing dependency injection
- Templates fail to render because of wrong template path
- Interceptors do not execute because they are registered after route setup

## Prevent It

- Use revel.OnAppStart for initialization code
- Register interceptors before the application starts
- Ensure template paths match the controller package structure
