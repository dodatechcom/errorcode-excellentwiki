---
title: "[Solution] Node.js ERR_MISSING_ESM_TRANSPILER — ESM Transpiler Missing Fix"
description: "Fix Node.js ERR_MISSING_ESM_TRANSPILER by configuring a custom loader, using --loader flag, or setting up experimental TypeScript/JSX support."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Node.js ERR_MISSING_ESM_TRANSPILER — ESM Transpiler Missing Fix

The `ERR_MISSING_ESM_TRANSPILER` error occurs when Node.js encounters an ESM file with an extension it cannot natively parse (like `.ts`, `.tsx`, `.jsx`) and no custom loader or transpiler is configured. Node.js natively supports `.js`, `.mjs`, and `.cjs` — any other extension requires explicit configuration.

## Description

Common ERR_MISSING_ESM_TRANSPILER messages include:

- `ERR_MISSING_ESM_TRANSPILER: "loader" is required to use ".ts" file extensions` — TypeScript without a loader.
- `ERR_MISSING_ESM_TRANSPILER: Must use import to load ES Module` — wrong file extension with no transpiler.

## Common Causes

```javascript
// Cause 1: Importing a .ts file without a loader
import { helper } from "./utils.ts";  // ERR_MISSING_ESM_TRANSPILER

// Cause 2: Importing JSX without configuration
import App from "./App.jsx";  // ERR_MISSING_ESM_TRANSPILER in Node.js

// Cause 3: package.json "exports" pointing to .ts files
// { "exports": { ".": "./src/index.ts" } }  — needs transpiler

// Cause 4: Missing TypeScript or SWC configuration
```

## Solutions

### Fix 1: Use the --loader flag with a transpiler

```bash
# For TypeScript with tsx (recommended)
npx tsx src/index.ts

# For TypeScript with ts-node
npx ts-node --esm src/index.ts

# For SWC (faster)
npx tsx --swc src/index.ts

# Custom loader with Node.js 18.18+
node --loader ts-node/esm src/index.ts
```

### Fix 2: Use tsx as a loader for TypeScript files

```bash
# Install tsx globally or as a dev dependency
npm install -D tsx

# Run with tsx directly
npx tsx src/index.ts

# Or add as a script in package.json
```

```json
{
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "start": "tsx src/index.ts"
  }
}
```

### Fix 3: Use the experimental TypeScript strip-types flag (Node.js 22+)

```bash
# Node.js 22.6+ supports --experimental-strip-types
node --experimental-strip-types src/index.ts

# Enable decorators support
node --experimental-strip-types --experimental-decorators src/index.ts
```

### Fix 4: Set up a custom loader for JSX

```javascript
// loader.mjs
import { readFileSync } from "fs";
import { fileURLToPath } from "url";
import { transform } from "esbuild";

const jsxExtensions = [".jsx", ".tsx"];

export async function resolve(specifier, context, nextResolve) {
  return nextResolve(specifier, context);
}

export async function load(url, context, nextLoad) {
  const ext = new URL(url).pathname;

  if (jsxExtensions.some((e) => ext.endsWith(e))) {
    const filePath = fileURLToPath(url);
    const source = readFileSync(filePath, "utf-8");
    const result = await transform(source, {
      loader: ext.endsWith(".tsx") ? "tsx" : "jsx",
      format: "esm",
    });
    return {
      format: "module",
      shortCircuit: true,
      source: result.code,
    };
  }

  return nextLoad(url, context);
}
```

```bash
node --import ./loader.mjs src/index.jsx
```

### Fix 5: Use a bundler for production

```bash
# Use esbuild to bundle TypeScript for production
npx esbuild src/index.ts --bundle --platform=node --outfile=dist/index.js

# Run the bundled output with plain Node.js
node dist/index.js
```

## Examples

```bash
# Before: ERR_MISSING_ESM_TRANSPILER
node src/index.ts

# After: with tsx
npx tsx src/index.ts

# After: with Node.js 22+ strip types
node --experimental-strip-types src/index.ts

# After: with esbuild bundling
npx esbuild src/index.ts --bundle --platform=node --outfile=dist/app.js
node dist/app.js
```

## Related Errors

- [ERR_REQUIRE_ESM]({{< relref "/languages/javascript/err_require_esm" >}}) — cannot require an ES module.
- [ERR_MODULE_NOT_FOUND]({{< relref "/languages/javascript/err_module_not_found" >}}) — ESM import resolution failed.
- [ERR_UNKNOWN_FILE_EXTENSION]({{< relref "/languages/javascript/err_unknown_file_extension" >}}) — Node.js does not know the extension.
- [SyntaxError]({{< relref "/languages/javascript/syntaxerror" >}}) — transpiled code has syntax errors.
