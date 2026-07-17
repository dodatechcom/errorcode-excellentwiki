---
title: "[Solution] Vite Dev Server Error"
description: "Fix Vite dev server errors. Resolve development server startup and connection issues."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Vite Dev Server Error

A dev server error occurs when Vite's development server fails to start or cannot serve modules. The error may be a port conflict, plugin failure, or configuration issue.

## Common Causes

- The configured port is already in use by another process
- A plugin fails during server initialization
- The `server.fs.allow` restriction blocks file access
- Network or firewall issues prevent the server from binding

## How to Fix

### Check if Port is in Use

```bash
lsof -i :5173
ss -tlnp | grep 5173
```

### Use a Different Port

```javascript
// vite.config.js
export default defineConfig({
  server: {
    port: 3000,
  },
});
```

### Allow File System Access

```javascript
export default defineConfig({
  server: {
    fs: {
      allow: ['.', '/usr/local/lib'],
    },
  },
});
```

### Kill Existing Processes on the Port

```bash
kill $(lsof -t -i:5173)
npx vite
```

### Enable Open Browser

```javascript
export default defineConfig({
  server: {
    open: true,
    host: true,  // listen on all addresses
  },
});
```

## Examples

```bash
# Port 5173 already in use
# Error: Port 5173 is already in use
# Fix: kill the existing process or use server.port: 3000

# FS restriction blocks import
# Blocked bare import "..." from index.html
# Fix: add server.fs.allow configuration
```

## Related Errors

- [Config Error]({{< relref "/tools/vite/config-error6" >}}) — invalid configuration
- [HMR Error]({{< relref "/tools/webpack/hmr-error" >}}) — hot module replacement issue
