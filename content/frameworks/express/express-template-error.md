---
title: "[Solution] Express Template Engine Error"
description: "Fix Express template engine errors. Resolve template rendering issues."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["template", "engine", "ejs", "pug", "handlebars", "express"]
weight: 5
---

An Express template engine error occurs when Express cannot render templates. This can be caused by missing engine configuration, syntax errors, or missing template files.

## Common Causes

- Template engine not registered with Express
- Template file does not exist
- Syntax error in template file
- Missing or undefined variables passed to template
- Views directory misconfigured

## How to Fix

### Set View Engine

```javascript
app.set('view engine', 'ejs');
app.set('views', './views');
```

### Render Template

```javascript
app.get('/', (req, res) => {
  res.render('index', { title: 'Home', user: req.user });
});
```

### Handle Template Errors

```javascript
app.get('/', (req, res, next) => {
  res.render('index', { title: 'Home' }, (err, html) => {
    if (err) return next(err);
    res.send(html);
  });
});
```

### Install Engine Package

```bash
npm install ejs
# or
npm install pug
# or
npm install handlebars
```

## Examples

```javascript
// Example 1: Engine not set
app.get('/', (req, res) => {
  res.render('index'); // Error: No default engine
});
// Fix: app.set('view engine', 'ejs')

// Example 2: Undefined variable
// Template: <%= user.name %>
res.render('page', {}); // user is undefined
// Fix: res.render('page', { user: { name: 'Guest' } })
```

## Related Errors

- [Express Static Error]({{< relref "/frameworks/express/express-static-error" >}}) — static file serving error
- [Express Middleware Error]({{< relref "/frameworks/express/express-middleware-error" >}}) — middleware error
