---
title: "[Solution] npm install ERR_REQUIRE_ESM ESM Require Error"
description: "Fix ERR_REQUIRE_ESM errors when requiring ES modules in CommonJS by updating Node.js, using dynamic import, or configuring package type."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ERR_REQUIRE_ESM ESM Require Error

This guide helps you diagnose and resolve npm install ERR_REQUIRE_ESM ESM Require Error errors encountered when running npm commands.

## Common Causes

- Package uses ES module syntax but is required from CommonJS code
- Node.js version does not support ESM require interop
- package.json missing type field for ESM-only packages

## How to Fix

### Use Dynamic Import Instead

```bash
const pkg = await import('<package>')
```

### Update Node.js to Latest LTS

```bash
nvm install --lts && nvm use --lts
```

### Add type Module to package.json

```bash
echo '"type": "module"' >> package.json
```

## Examples

```bash
# CommonJS requiring ESM package
const pkg = require('esm-package')
# Fix: Use dynamic import
const pkg = await import('esm-package')

# Node.js too old for ESM
npm install modern-esm-pkg
# Fix: Update Node.js
nvm install 18
nvm use 18

```

## Related Errors

- [Module Not Found]({{< relref "/tools/npm/module-not-found" >}}) -- missing module
- [Engine Mismatch]({{< relref "/tools/npm/ebadengine-engine-mismatch" >}}) -- version incompatibility
