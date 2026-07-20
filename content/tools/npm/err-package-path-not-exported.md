---
title: "[Solution] npm install ERR_PACKAGE_PATH_NOT_EXPORTED"
description: "Resolve ERR_PACKAGE_PATH_NOT_EXPORTED errors in npm install by fixing package exports configuration and using correct import paths."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ERR_PACKAGE_PATH_NOT_EXPORTED

This guide helps you diagnose and resolve npm install ERR_PACKAGE_PATH_NOT_EXPORTED errors encountered when running npm commands.

## Common Causes

- Package exports field in package.json does not include the requested path
- Import path references a file not listed in the package exports map
- Version mismatch between installed package and expected exports

## How to Fix

### Check Package Exports

```bash
node -e 'console.log(require("<package>/package.json").exports)'
```

### Use the Correct Import Path

```bash
node -e 'console.log(require.resolve("<package>"))'
```

### Upgrade to Latest Package Version

```bash
npm update <package>
```

## Examples

```bash
# Deep import not exported
import x from 'pkg/deep/path'
# Fix: Check available exports
node -e 'console.log(JSON.stringify(require("pkg/package.json").exports, null, 2))'

# Missing subpath export
require('pkg/subpath')
# Fix: Update package
npm update pkg

```

## Related Errors

- [ESM Require Error]({{< relref "/tools/npm/err-require-esm-esm-require-error" >}}) -- ESM compatibility
- [Module Not Found]({{< relref "/tools/npm/module-not-found" >}}) -- missing module
