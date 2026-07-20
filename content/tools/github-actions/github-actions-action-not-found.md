---
title: "[Solution] GitHub Actions Action Not Found"
description: "Fix GitHub Actions action not found errors when using marketplace actions."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Action not found errors occur when a referenced action does not exist:

```
Error: Can't find action 'actions/chekout@v4'
```

## Common Causes

- Action reference is misspelled.
- Action was removed or renamed.
- Private action requires authentication.

## How to Fix

**Verify the action exists:**

```yaml
- uses: actions/checkout@v4
```

**Use a local action:**

```yaml
- uses: ./.github/actions/my-action
```

## Examples

```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 0
```
