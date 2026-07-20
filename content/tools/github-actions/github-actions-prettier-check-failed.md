---
title: "[Solution] GitHub Actions Prettier Check Failed"
description: "Fix GitHub Actions Prettier formatting check failures."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Prettier check failures occur when code formatting does not match standards:

```
Error: [warn] src/index.ts
Code style issues found in the above file(s). Forgot to run Prettier?
```

## Common Causes

- Code committed without running Prettier.
- Prettier version differs between local and CI.

## How to Fix

**Run Prettier check in CI:**

```yaml
steps:
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: 'npm'
  - run: npm ci
  - run: npx prettier --check .
```

## Examples

```yaml
steps:
  - run: npx prettier --check "src/**/*.{ts,tsx,js,jsx,json,css,md}"
```
