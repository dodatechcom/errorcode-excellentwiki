---
title: "[Solution] TypeScript TS2307 v2 — Cannot Find Module Fix"
description: "Fix TypeScript TS2307 when module resolution fails. Handle missing types, path aliases, and module format issues."
languages: ["typescript"]
error-types: ["compile-error"]
severities: ["error"]
weight: 5
---

# TS2307 — Cannot Find Module (v2)

This variant of TS2307 covers module resolution failures involving path aliases, relative imports, missing type declarations, and mismatches between ESM and CJS configurations.

## What This Error Means

Common error messages:

- `TS2307: Cannot find module '@utils/helper' or its corresponding type declarations`
- `TS2307: Cannot find module './types' or its corresponding type declarations`
- `TS2307: Cannot find module 'my-lib' because it is not declared in the 'typesVersions' field`
- `TS2307: Cannot find module '@/components/Button'`

TypeScript uses the `moduleResolution` strategy in tsconfig.json to find imported modules. Path aliases, missing type packages, or incorrect resolution strategies cause this error.

## Common Causes

```typescript
// Cause 1: Path alias not configured
import { helper } from '@utils/helper'; // no alias in tsconfig

// Cause 2: Missing @types package
import express from 'express'; // @types/express not installed

// Cause 3: Relative path typo
import { User } from './types/user'; // file is at ./types/users.ts

// Cause 4: Package not installed
import { something } from 'missing-package';

// Cause 5: ESM module resolution with wrong extension
import { helper } from './utils'; // needs './utils.js' for ESM
```

## How to Fix

### Fix 1: Configure paths in tsconfig.json

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@utils/*": ["src/utils/*"],
      "@components/*": ["src/components/*"]
    }
  }
}
```

### Fix 2: Install missing type packages

```bash
npm install --save-dev @types/express @types/node
# or
yarn add -D @types/express
```

### Fix 3: Create type declaration file

```typescript
// src/types/my-lib.d.ts
declare module 'my-lib' {
  export function doSomething(): void;
}
```

### Fix 4: Use moduleResolution that matches your project

```json
{
  "compilerOptions": {
    "moduleResolution": "node"
  }
}
```

For ESM projects:
```json
{
  "compilerOptions": {
    "moduleResolution": "node16"
  }
}
```

### Fix 5: Fix relative path imports

```typescript
// ❌ Wrong path
import { User } from './types/user';

// ✅ Correct path
import { User } from './types/users';

// Or use path aliases
import { User } from '@types/users';
```

## Examples

```
src/main.ts:1:21 - error TS2307: Cannot find module './config' or its corresponding type declarations.

1 import { config } from './config';
                        ~~~~~~~~~~~~~~
```

```json
// Fix: add file extension for node16 resolution
{
  "compilerOptions": {
    "module": "node16",
    "moduleResolution": "node16"
  }
}
// Then use: import { config } from './config.js';
```

## Related Errors

- [TS2307]({{< relref "/languages/typescript/ts2307" >}}) — basic TS2307
- [TS2304]({{< relref "/languages/typescript/ts2304" >}}) — cannot find name
- [TS2306]({{< relref "/languages/typescript/ts2306" >}}) — is not a module
