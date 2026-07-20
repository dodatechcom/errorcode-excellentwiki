---
title: "[Solution] npm Cannot Find Module -- Cannot find module 'X'"
description: "Fix npm 'Cannot find module' error. Resolve missing Node.js module issues."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm Cannot Find Module -- Cannot find module 'X'

This error means Node.js cannot locate the specified module in the `node_modules` directory or along the resolution path. The module is either not installed or the path is incorrect.

## Common Causes

- Package was not installed or install failed silently
- Typo in the module name in your `require()` or `import` statement
- `node_modules` is missing or corrupted
- Module is a dependency that needs to be installed separately

## How to Fix

### Install the Missing Module

```bash
npm install <module-name>
```

### Check for Typos

```javascript
// Wrong
const express = require("expres");

// Correct
const express = require("express");
```

### Reinstall All Dependencies

```bash
rm -rf node_modules package-lock.json
npm install
```

### Install as Dev Dependency (if needed)

```bash
npm install --save-dev <module-name>
```

### Check the Module Exists

```bash
npm ls <module-name>
```

## Examples

```bash
# Example 1: Missing module
node app.js
# Error: Cannot find module 'lodash'
# Fix: npm install lodash

# Example 2: Typo in require
node app.js
# Error: Cannot find module 'expres'
# Fix: correct the name to 'express'

# Example 3: Module installed globally but not locally
npm install -g typescript
node -e "require('typescript')"
# Error: Cannot find module 'typescript'
# Fix: npm install typescript
```

## Related Errors

- [ERESOLVE]({{< relref "/tools/npm/peer-deps" >}}) -- peer dependency resolution failure
- [Image Not Found]({{< relref "/tools/docker/image-not-found" >}}) -- Docker image not found
