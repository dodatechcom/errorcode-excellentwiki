---
title: "[Solution] GitHub Actions Cache Hit Miss Logic Error"
description: "Fix GitHub Actions cache hit/miss logic errors in workflow."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Cache hit/miss logic errors occur when the workflow does not handle cache states correctly:

```
Warning: cache-hit was expected but not found
```

## Common Causes

- Workflow expects cache hit but key does not match.
- Conditional steps based on cache-hit use incorrect syntax.

## How to Fix

**Properly handle cache-hit output:**

```yaml
- uses: actions/cache@v4
  id: cache-deps
  with:
    path: node_modules
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}

- run: npm ci
  if: steps.cache-deps.outputs.cache-hit != 'true'

- run: npm run build
```

## Examples

```yaml
steps:
  - uses: actions/cache@v4
    id: cache
    with:
      path: ~/.cache/go-build
      key: ${{ runner.os }}-go-${{ hashFiles('**/go.sum') }}

  - run: go build ./...
```
