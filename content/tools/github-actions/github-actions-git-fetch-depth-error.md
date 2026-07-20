---
title: "[Solution] GitHub Actions Git Fetch Depth Error"
description: "Fix GitHub Actions git fetch depth errors when commit history is insufficient."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Fetch depth errors occur when the shallow clone does not include enough commit history:

```
Error: detached HEAD; you are on branch 'main' but your commit
does not have enough history
```

## Common Causes

- Default `fetch-depth: 1` only fetches the latest commit.
- Steps that need `git log` or diff comparison require more depth.

## How to Fix

**Increase fetch depth:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 10
```

**Fetch full history:**

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
```

## Examples

```yaml
steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
      fetch-tags: true
```
