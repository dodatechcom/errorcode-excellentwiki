---
title: "[Solution] npm install ERR_MODULE_NOT_FOUND Module Not Found"
description: "Fix ERR_MODULE_NOT_FOUND errors in npm install by checking module paths, reinstalling dependencies, and verifying package resolution."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ERR_MODULE_NOT_FOUND Module Not Found

This guide helps you diagnose and resolve npm install ERR_MODULE_NOT_FOUND Module Not Found errors encountered when running npm commands.

## Common Causes

- Module was removed or never installed in node_modules
- Import path is incorrect or missing file extension for ESM
- Hoisting issues in monorepo cause module to be inaccessible

## How to Fix

### Reinstall All Dependencies

```bash
rm -rf node_modules && npm install
```

### Check Module Resolution

```bash
node -e 'require.resolve("<module>")'
```

### Verify Package is in package.json

```bash
cat package.json | grep <module>
```

## Examples

```bash
# Module missing from node_modules
npm install
# Fix: Full reinstall
rm -rf node_modules package-lock.json
npm install

# ESM import missing extension
import x from './utils'
# Fix: Add file extension
import x from './utils.js'

```

## Related Errors

- [Module Not Found]({{< relref "/tools/npm/module-not-found" >}}) -- missing module
- [No Such File]({{< relref "/tools/npm/enoent-no-such-file" >}}) -- file not found
