---
title: "[Solution] Netlify CLI Version Mismatch Error"
description: "Fix Netlify CLI version mismatch errors when local CLI and build environment differ."
tools: ["netlify"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Netlify CLI Version Mismatch Error

Netlify CLI reports version mismatch between local and remote build environments.

```
Warning: CLI version mismatch. Local: v12.0.0, Netlify Build: v10.0.0
```

## Common Causes

- Outdated CLI installation
- Global vs local CLI version conflict
- Build environment using different CLI version
- Node version causing version detection issues
- Cached CLI version

## How to Fix

### Update Netlify CLI

```bash
# Update globally
npm install -g netlify-cli@latest

# Update locally in project
npm install netlify-cli@latest --save-dev
```

### Use Local CLI Version

```bash
# In package.json scripts
{
  "scripts": {
    "netlify:dev": "npx netlify dev",
    "netlify:deploy": "npx netlify deploy --prod"
  }
}
```

### Check CLI Version

```bash
# Check installed version
netlify --version

# Check latest available
npm view netlify-cli version
```

### Pin CLI Version

```json
// package.json
{
  "devDependencies": {
    "netlify-cli": "12.0.0"
  }
}
```

### Clear Cache

```bash
# Clear npm cache
npm cache clean --force

# Reinstall
rm -rf node_modules
npm install
```

## Examples

```bash
# Verify CLI works
netlify status
netlify --version

# Deploy with local CLI
npx netlify deploy --prod --dir=dist
```
