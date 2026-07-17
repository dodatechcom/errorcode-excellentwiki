---
title: "[Solution] Node.js ERR_UNKNOWN_FILE_EXTENSION — Unknown File Extension Fix"
description: "Fix Node.js ERR_UNKNOWN_FILE_EXTENSION by using tsx, configuring --loader, setting package.json type field, or renaming files."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_UNKNOWN_FILE_EXTENSION — Unknown File Extension Fix

The `ERR_UNKNOWN_FILE_EXTENSION` error occurs when Node.js encounters a file extension it does not natively recognize for ESM or CJS loading. This is most common when trying to run `.ts`, `.tsx`, `.jsx`, or `.mts` files directly without a transpiler or custom loader.

## Description

Common ERR_UNKNOWN_FILE_EXTENSION messages include:

- `ERR_UNKNOWN_FILE_EXTENSION: Unknown file extension ".ts"` — TypeScript file without a loader.
- `ERR_UNKNOWN_FILE_EXTENSION: Unknown file extension ".tsx"` — TSX file without configuration.
- `ERR_UNKNOWN_FILE_EXTENSION: Unknown file extension ".mjs"` — occurs in rare cases with incorrect package.json config.

## Common Causes

```bash
# Cause 1: Running TypeScript directly
node src/index.ts
# ERR_UNKNOWN_FILE_EXTENSION: Unknown file extension ".ts"

# Cause 2: Running JSX without a loader
node src/App.jsx
# ERR_UNKNOWN_FILE_EXTENSION: Unknown file extension ".jsx"

# Cause 3: package.json "type": "module" with .mts files without loader
node src/utils.mts
# ERR_UNKNOWN_FILE_EXTENSION: Unknown file extension ".mts"

# Cause 4: tsconfig.json targets a non-standard extension
```

## Solutions

### Fix 1: Use tsx to run TypeScript files

```bash
# Install tsx
npm install -D tsx

# Run directly with tsx
npx tsx src/index.ts

# Or add to package.json scripts
```

```json
{
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "start": "tsx src/index.ts",
    "build": "tsc && node dist/index.js"
  }
}
```

### Fix 2: Use Node.js 22+ --experimental-strip-types

```bash
# Node.js 22.6+ can strip TypeScript types natively
node --experimental-strip-types src/index.ts

# With decorator support
node --experimental-strip-types --experimental-decorators src/index.ts
```

### Fix 3: Use ts-node with --esm flag

```bash
# Install ts-node
npm install -D ts-node

# Run with ESM support
npx ts-node --esm src/index.ts

# Or configure in tsconfig.json
```

```json
{
  "ts-node": {
    "esm": true,
    "transpileOnly": true
  }
}
```

### Fix 4: Bundle TypeScript before running with Node.js

```bash
# Bundle with esbuild
npx esbuild src/index.ts --bundle --platform=node --outfile=dist/index.js

# Run the bundled output
node dist/index.js
```

```javascript
// Or bundle with swc for faster builds
npx swc src --out-dir dist --config-file .swcrc
node dist/index.js
```

### Fix 5: Rename .ts files to .js and use JSDoc types

```bash
# If you want to avoid transpilation entirely
mv src/index.ts src/index.js
# Add type annotations via JSDoc comments instead
```

```javascript
/**
 * @param {string} name
 * @returns {string}
 */
function greet(name) {
  return `Hello, ${name}`;
}
```

## Examples

```bash
# Step-by-step fix for a TypeScript project

# 1. Install dependencies
npm install -D typescript tsx

# 2. Create tsconfig.json
# { "compilerOptions": { "target": "ES2022", "module": "NodeNext" } }

# 3. Run with tsx (development)
npx tsx src/index.ts

# 4. Build for production
npx tsc

# 5. Run compiled output
node dist/index.js
```

## Related Errors

- [ERR_MISSING_ESM_TRANSPILER]({{< relref "/languages/javascript/err_missing_esm_transpiler" >}}) — no transpiler configured for ESM.
- [ERR_REQUIRE_ESM]({{< relref "/languages/javascript/err_require_esm" >}}) — cannot require an ES module.
- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/err_module_not_found" >}}) — ESM import resolution failed.
- [SyntaxError]({{< relref "/languages/javascript/syntaxerror" >}}) — transpiled code has syntax errors.
