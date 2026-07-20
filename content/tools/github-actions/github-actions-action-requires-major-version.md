---
title: "[Solution] GitHub Actions Action Requires Major Version"
description: "Fix GitHub Actions action requires major version warnings."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Major version warnings occur when an action requires a specific major version:

```
Warning: Action requires Node.js 16, which is not supported
```

## Common Causes

- Action uses an outdated Node.js runtime.
- Action version incompatible with runner.

## How to Fix

**Update to a newer version of the action:**

```yaml
- uses: actions/checkout@v4  # v4 uses Node 20
```

## Examples

```yaml
# Outdated - uses Node 16
- uses: actions/checkout@v3

# Current - uses Node 20
- uses: actions/checkout@v4
```
