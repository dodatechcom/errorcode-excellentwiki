---
title: "Node.js Error: Cannot Find Module 'X'"
description: "Error: Cannot find module 'X' — Fix Node.js module resolution failures."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["nodejs", "cannot-find-module", "module", "require", "import", "node_modules"]
weight: 5
---

The `Cannot find module` error occurs when Node.js fails to locate a module during `require()` or `import` resolution. This differs from `ERR_MODULE_NOT_FOUND` as it typically originates from CommonJS require resolution.

## Description

Common Cannot Find Module messages include:

- `Error: Cannot find module 'express'` — module not installed
- `Error: Cannot find module './utils'` — relative path does not resolve
- `Error: Cannot find module '/absolute/path/to/module'` — absolute path invalid
- `Error: Cannot find module 'my-package/lib/helper'` — subpath not exported

## Common Causes

```javascript
// Cause 1: Module not in node_modules
const lodash = require("lodash"); // not installed

// Cause 2: Typo in module name
const express = require("expresss"); // extra 's'

// Cause 3: Module installed at wrong level (monorepo)
// package in packages/app needs package in packages/lib

// Cause 4: Node version mismatch
// require.resolve differs between Node 16 and Node 18+
```

## Solutions

### Fix 1: Install the missing module

```bash
# Install the missing dependency
npm install express

# Or with yarn
yarn add express

# Verify installation
ls node_modules | grep express
```

### Fix 2: Check module resolution paths

```javascript
// Print the resolution paths Node.js searches
console.log(module.paths);

// Verify where a module resolves to
try {
  const resolved = require.resolve("my-module");
  console.log("Resolved to:", resolved);
} catch (err) {
  console.error("Module not found:", err.message);
}
```

### Fix 3: Fix monorepo resolution

```bash
# In a monorepo, use workspace commands
npm install --workspace=packages/my-app

# Or use lerna
lerna bootstrap

# Or use pnpm workspaces
pnpm install --filter my-app
```

### Fix 4: Set up Node.js module resolution

```javascript
// Use NODE_PATH environment variable
// process.env.NODE_PATH = "/shared/modules";

// Or use module-alias
// package.json: { "_moduleAliases": { "@lib": "./src/lib" } }
require("module-alias/register");
const helper = require("@lib/helper");
```

## Examples

```javascript
// Cannot find module after fresh clone
// Fix: run npm install
// $ npm install

// Cannot find module in Docker container
// Fix: ensure COPY package.json and npm install in Dockerfile
// FROM node:18
// WORKDIR /app
// COPY package*.json ./
// RUN npm ci
// COPY . .
// CMD ["node", "server.js"]
```

## Related Errors

- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/err-cannot-find-module" >}}) — ESM module not found.
- [ERR_REQUIRE_ESM]({{< relref "/languages/javascript/err_require_esm" >}}) — require() on ESM module.
- [ERR_DOPEN_DISABLED]({{< relref "/languages/javascript/err_dlopen_disabled" >}}) — native module loading disabled.
