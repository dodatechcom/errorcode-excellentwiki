---
title: "[Solution] GitHub Actions NPM CI Failed"
description: "Fix GitHub Actions npm ci failures during Node.js workflow."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

npm ci failures occur during the dependency installation step:

```
Error: npm ERR! code ERESOLVE
npm ERR! ERESOLVE unable to resolve dependency tree
```

## Common Causes

- Dependency version conflicts in package-lock.json.
- Node.js version incompatible with some dependencies.
- Corrupted or stale package-lock.json.

## How to Fix

**Ensure Node.js version matches:**

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
  - run: npm ci
```

**Fix dependency conflicts:**

```bash
npm install --legacy-peer-deps
```

## Examples

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
  - run: npm ci --prefer-offline
  - run: npm run build
  - run: npm test
```
