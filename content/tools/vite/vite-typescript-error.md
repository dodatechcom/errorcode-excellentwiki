---
title: "Vite TypeScript Type Checking Error"
description: "Vite encounters TypeScript type errors during development or build."
tools: ["vite"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["vite", "typescript", "type", "error", "checking"]
weight: 5
---

# Vite TypeScript — Type Checking Error

This error occurs when Vite encounters TypeScript type errors. While Vite uses esbuild for transpilation (which skips type checking), build errors or IDE errors reveal type issues.

## Common Causes

- TypeScript type errors in source files
- Missing type definitions
- Incorrect generic type parameters
- Strict mode violations

## How to Fix

### Run Type Checker

```bash
npx tsc --noEmit
```

### Add TypeScript Config

```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "jsx": "react-jsx",
    "noEmit": true
  }
}
```

### Fix Common Type Errors

```typescript
// Wrong
function add(a: number, b: string): number {
  return a + b;
}

// Correct
function add(a: number, b: number): number {
  return a + b;
}
```

### Install Missing Types

```bash
npm install -D @types/react @types/node
```

### Configure Type Check in Build

```json
// package.json
{
  "scripts": {
    "typecheck": "tsc --noEmit",
    "build": "npm run typecheck && vite build"
  }
}
```

### Use Satisfies for Better Inference

```typescript
const config = {
  port: 3000,
  host: 'localhost',
} satisfies import('vite').ServerOptions;
```

## Examples

```text
src/App.tsx:15:5 - error TS2322:
  Type 'string' is not assignable to type 'number'.

  15     const count: number = "0";
```

## Related Errors

- [Vite Build Error]({{< relref "/tools/vite/vite-build-error" >}}) — general build failure
- [Vite Config Error]({{< relref "/tools/vite/vite-config-error" >}}) — configuration error
- [Vite React Error]({{< relref "/tools/vite/vite-react-error" >}}) — React JSX errors
