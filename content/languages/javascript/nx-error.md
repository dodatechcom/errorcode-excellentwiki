---
title: "[Solution] JavaScript Nx Monorepo Error — How to Fix"
description: "Fix JavaScript Nx monorepo project graph errors, dependency resolution failures, cache conflicts, and executor configuration issues."
languages: ["javascript"]
error-types: ["runtime"]
severities: ["error"]
comments: true
weight: 811
---

# JavaScript Nx Monorepo Error

An `NxError`, `TypeError`, or `ProjectGraphError` occurs when Nx's project graph cannot be computed, dependencies between projects are misconfigured, the computation cache becomes corrupted, or executors are incorrectly defined.

## Why It Happens

Nx errors arise from circular dependencies between projects, missing `project.json` configuration, incorrect `target` configurations in executors, stale or corrupted `.nx/cache` directories, and TypeScript path alias resolution failures.

## Common Error Messages

- `Error: Cannot create project graph - circular dependency detected`
- `Error: Nx detected a project with no targets`
- `Error: Cannot find executor '@nx/xxx:build'`
- `Error: Nx cache has been corrupted`
- `Error: Could not resolve dependency 'xxx' from project 'yyy'`

## How to Fix It

### Fix 1: Resolve circular dependencies

```json
// ❌ Wrong - project-a imports from project-b, project-b imports from project-a
// ✅ Correct - extract shared library
{
  "shared": {
    "sourceRoot": "libs/shared/src",
    "targets": { "build": { "executor": "@nx/js:tsc" } }
  }
}
```

### Fix 2: Configure project targets

```json
// project.json
{
  "name": "api",
  "sourceRoot": "apps/api/src",
  "projectType": "application",
  "targets": {
    "build": {
      "executor": "@nx/webpack:webpack",
      "options": {
        "outputPath": "dist/apps/api",
        "main": "apps/api/src/main.ts",
        "tsConfig": "apps/api/tsconfig.app.json"
      }
    },
    "serve": {
      "executor": "@nx/js:node",
      "options": {
        "buildTarget": "api:build"
      }
    }
  }
}
```

### Fix 3: Clear corrupted cache

```bash
# ❌ Run build failing due to stale cache
# ✅ Clear Nx cache
npx nx reset

# Or manually
rm -rf .nx/cache

# Disable cache for debugging
# npx nx build my-app --skip-nx-cache
```

### Fix 4: Set up dependencies between projects

```json
// ❌ Wrong - implicit dependency that Nx can't find
// apps/api/project.json
{
  "name": "api",
  "implicitDependencies": ["shared-lib"],
  "targets": {
    "build": {
      "executor": "@nx/js:tsc",
      "options": {}
    }
  }
}
```

```typescript
// ✅ Correct - explicit import so Nx detects dependency
// apps/api/src/main.ts
import { helper } from '@myorg/shared-lib'
```

## Examples

Full project configuration:

```json
{
  "name": "my-app",
  "root": "apps/my-app",
  "sourceRoot": "apps/my-app/src",
  "projectType": "application",
  "tags": ["scope:frontend", "type:app"],
  "implicitDependencies": [],
  "targets": {
    "build": {
      "executor": "@nx/vite:build",
      "options": { "outputPath": "dist/apps/my-app" }
    },
    "test": {
      "executor": "@nx/vitest:test",
      "options": { "passWithNoTests": true }
    }
  }
}
```

## Related Errors

- [JavaScript Turborepo Error](/languages/javascript/js-turborepo-error)
- [JavaScript Webpack Error](/languages/javascript/js-webpack-error)
- [JavaScript TypeScript Error](/languages/javascript/js-ts-node-error)
