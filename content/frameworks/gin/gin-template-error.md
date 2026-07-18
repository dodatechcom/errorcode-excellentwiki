---
title: "[Solution] Gin Template Error — How to Fix"
description: "Fix Gin template rendering errors. Resolve HTML template loading, execution, and compilation failures."
frameworks: ["gin"]
error-types: ["template-error"]
severities: ["error"]
weight: 5
comments: true
---

A Gin template error occurs when HTML templates cannot be loaded, compiled, or rendered properly.

## Why It Happens

Template errors happen due to missing template files, syntax errors in templates, incorrect variable access, or missing custom functions.

## Common Error Messages

```
template: not defined
```

```
html/template: cannot parse
```

```
function not defined in template
```

```
unexpected EOF in template
```

## How to Fix It

### 1. Load Templates Correctly

Use LoadHTMLGlob or LoadHTMLFiles.

```go
r := gin.Default()
r.LoadHTMLGlob("templates/*")

r.GET("/page", func(c *gin.Context) {
    c.HTML(200, "index.html", gin.H{"title": "Home"})
})
```

### 2. Use Subdirectories

Load templates from subdirectories.

```go
r.LoadHTMLGlob("templates/**/*")
```

### 3. Add Custom Template Functions

Register custom functions before loading.

```go
r.SetFuncMap(template.FuncMap{
    "upper": strings.ToUpper,
    "formatDate": func(t time.Time) string {
        return t.Format("Jan 02, 2006")
    },
})
r.LoadHTMLGlob("templates/*")
```

### 4. Handle Template Errors

Check for errors during rendering.

```go
if err := c.HTML(200, "page.html", data); err != nil {
    log.Printf("template error: %v", err)
}
```

## Common Scenarios

**Scenario 1: Template not found error.**
Check template file path and name.

**Scenario 2: Variable not defined in template.**
Ensure all variables are passed to c.HTML.

## Prevent It

1. **Validate templates during build.**


2. **Use template caching in production.**


3. **Test template rendering.**


