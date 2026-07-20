---
title: "[Solution] GitHub Actions Action Version Not Pinned"
description: "Fix GitHub Actions action version not pinned warnings and security concerns."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Unpinned action versions can lead to unexpected behavior and security risks:

```
Warning: Action 'actions/checkout' is not pinned to a full length commit SHA
```

## Common Causes

- Using branch names or tags instead of commit SHAs.
- Supply chain attack risk with unpinned actions.

## How to Fix

**Pin to a full commit SHA:**

```yaml
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11
  # v4.1.1
```

**Use tags for convenience (less secure):**

```yaml
- uses: actions/checkout@v4
```

## Examples

```yaml
# Most secure - full SHA
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11

# Less secure but convenient
- uses: actions/checkout@v4
```
