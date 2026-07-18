---
title: "Solved JavaScript ts-node Error — How to Fix"
date: 2026-03-20T17:15:00+00:00
description: "Learn how to resolve JavaScript ts-node TypeScript execution and configuration errors."
categories: ["javascript"]
keywords: ["ts-node error", "typescript node", "ts-node config", "typescript execution", "ts-node register"]
error_types: ["runtime"]
severities: ["error"]
languages: ["javascript"]
weight: 5
comments: true
---

## Why It Happens

ts-node errors occur when TypeScript compilation fails, tsconfig is misconfigured, or module resolution doesn't match the runtime. The tool transpiles TypeScript on-the-fly.

Common causes include:
- Invalid tsconfig.json syntax
- Missing TypeScript dependencies
- Module resolution mismatch
- Strict mode violations
- ESM/CJS configuration issues

## Common Error Messages

```
Error: Cannot find module './app'
```

```
TSError: ⨯ Unable to compile TypeScript
```

```
Error: ts-node requires --esm flag
```

## How to Fix It

### 1. Configure ts-node

Set up ts-node properly.

```javascript
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

```json
// package.json
{
  "scripts": {
    "dev": "ts-node src/index.ts",
    "dev:watch": "ts-node-dev --respawn src/index.ts",
    "build": "tsc",
    "start": "node dist/index.js"
  },
  "ts-node": {
    "transpileOnly": true,
    "compilerOptions": {
      "module": "commonjs"
    }
  }
}
```

### 2. Handle Module Resolution

Fix import issues.

```typescript
// ❌ Wrong - missing extension
import { something } from "./utils";

// ✅ Correct - with tsconfig paths
// tsconfig.json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    }
  }
}

// Import with alias
import { something } from "@/utils/something";
```

### 3. Use ts-node-dev

Watch mode for development.

```bash
# Install
npm install -D ts-node-dev

# Basic usage
npx ts-node-dev --respawn src/index.ts

# With options
npx ts-node-dev --respawn --transpile-only src/index.ts

# With watch
npx ts-node-dev --watch src src/index.ts
```

## Common Scenarios

### Scenario 1: ESM Support

Use ESM with ts-node:

```json
// package.json
{
  "type": "module",
  "scripts": {
    "dev": "node --loader ts-node/esm src/index.ts"
  }
}
```

### Scenario 2: Project References

Use with project references:

```json
// tsconfig.json
{
  "references": [
    { "path": "./packages/core" },
    { "path": "./packages/utils" }
  ]
}
```

## Prevent It

- Use `transpileOnly: true` for faster execution
- Configure `ts-node` in `package.json` for better compatibility
- Use `ts-node-dev` for watch mode in development
- Set `esModuleInterop: true` for default imports
- Use `--esm` flag when using `"type": "module"`