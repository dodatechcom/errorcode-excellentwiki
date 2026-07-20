---
title: "[Solution] npm install ERR_UNSUPPORTED_DIR_IMPORT"
description: "Handle ERR_UNSUPPORTED_DIR_IMPORT errors in npm install by adding package.json to directories, configuring module resolution, and fixing import paths."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ERR_UNSUPPORTED_DIR_IMPORT

This guide helps you diagnose and resolve npm install ERR_UNSUPPORTED_DIR_IMPORT errors encountered when running npm commands.

## Common Causes

- Importing a directory directly instead of a specific file or package
- Missing index.js or package.json in the imported directory
- TypeScript or bundler configuration does not resolve directory imports

## How to Fix

### Add index.js to Directory

```bash
touch <directory>/index.js
```

### Import Specific File Instead

```bash
import x from '<directory>/file.js'
```

### Configure Module Resolution

```bash
# Add paths config to tsconfig.json or webpack config
```

## Examples

```bash
# Direct directory import fails
import x from './utils'
# Fix: Import specific file or add index.js
import x from './utils/index.js'

# TypeScript directory import
import x from '../shared'
# Fix: Add index.ts to shared directory
touch shared/index.ts

```

## Related Errors

- [Module Not Found]({{< relref "/tools/npm/module-not-found" >}}) -- missing module
- [ESM Require Error]({{< relref "/tools/npm/err-require-esm-esm-require-error" >}}) -- ESM compatibility
