---
title: "[Solution] TypeScript Cannot Find Module — Module Resolution and Type Declarations Fix"
description: "Fix TypeScript 'Cannot find module X or its type declarations' errors. Configure module resolution, install @types packages, and set up path aliases."
languages: ["typescript"]
severities: ["error"]
error-types: ["type-error"]
weight: 5
---

# TypeScript: Cannot find module 'X' or its type declarations

This error occurs when TypeScript cannot resolve a module import. It happens when the module doesn't exist, hasn't been installed, is missing type declarations, or when `tsconfig.json` module resolution settings don't match the project structure.

## Common Causes

- **Module not installed** — `node_modules` is missing the package
- **Missing `@types` package** — JavaScript packages need separate type declarations
- **Incorrect `moduleResolution` in tsconfig** — using `"node"` when the package needs `"node16"` or `"bundler"`
- **Path aliases not configured** — importing via aliases without `paths` in tsconfig

## How to Fix

```bash
# Fix 1: Install the missing package
npm install <package-name>

# Fix 2: Install type declarations
npm install --save-dev @types/<package-name>

# Fix 3: Some packages include their own types — no @types needed
npm install express  # express includes types
```

```json
// Fix 4: Configure tsconfig.json for module resolution
{
  "compilerOptions": {
    "moduleResolution": "node",
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

```typescript
// Fix 5: Create a declaration file for untyped modules
// src/types/my-module.d.ts
declare module "my-untyped-module" {
  export function doSomething(): void;
  export default function main(): void;
}

// Now you can import it
import main from "my-untyped-module";  // OK
```

## Examples

```typescript
// Example 1: Missing @types package
// ERROR: Cannot find module 'lodash' or its type declarations
import _ from "lodash";
// FIX: npm install --save-dev @types/lodash

// Example 2: Custom path alias
// tsconfig.json: { "paths": { "@app/*": ["./src/*"] } }
import { helper } from "@app/utils/helper";  // needs paths config

// Example 3: Local module not found
// File: src/utils/math.ts
export function add(a: number, b: number) { return a + b; }

// File: src/index.ts
import { add } from "./utils/math";  // must match exact path and file extension
```

## Common tsconfig.json Fixes

```json
{
  "compilerOptions": {
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "noEmit": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src/**/*"]
}
```

## Related Errors

- [TS2307: Cannot find module]({{< relref "/languages/typescript/ts2307" >}}) — base variant of this error
- [TS2309: Cannot find global type]({{< relref "/languages/typescript/ts2309" >}}) — missing global type declarations
- [TS2688: Cannot find type definition file]({{< relref "/languages/typescript/ts2688" >}}) — broken @types path
