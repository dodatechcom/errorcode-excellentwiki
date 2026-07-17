---
title: "[Solution] Express Static File Serving Error"
description: "Fix Express static file serving errors. Resolve static file access issues."
frameworks: ["express"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

An Express static file serving error occurs when Express cannot serve static files like CSS, JavaScript, or images.

## Common Causes

- Static middleware not configured
- Wrong directory path specified
- Files not in the correct public directory
- Directory structure does not match URL path
- Missing or incorrect file extensions

## How to Fix

### Configure Static Middleware

```javascript
app.use(express.static('public'));
```

### Serve Multiple Directories

```javascript
app.use(express.static('public'));
app.use(express.static('static'));
```

### Set URL Prefix

```javascript
app.use('/static', express.static('public'));
// Access: /static/css/style.css -> public/css/style.css
```

### Check File Permissions

```bash
ls -la public/css/
chmod 644 public/css/style.css
```

### Verify Directory Exists

```bash
ls -la public/
ls -la public/css/
```

## Examples

```javascript
// Example 1: Wrong path
app.use(express.static('public'));
// Files are in 'assets/' directory
// Fix: app.use(express.static('assets'))

// Example 2: URL prefix
app.use('/assets', express.static('public'));
// Access: /assets/css/style.css
// Not: /css/style.css
```

## Related Errors

- [Express Template Error]({{< relref "/frameworks/express/express-template-error" >}}) — template engine error
- [Express 404 Error]({{< relref "/frameworks/express/express-404-error" >}}) — route not found
