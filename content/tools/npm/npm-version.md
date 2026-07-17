---
title: "[Solution] npm Version Conflict Error"
description: "Fix npm version conflict errors. Resolve dependency version resolution issues."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["version", "conflict", "dependency", "resolution", "npm"]
weight: 5
---

A npm version conflict error occurs when dependencies require incompatible versions of the same package. npm cannot find a version range that satisfies all requirements.

## Common Causes

- Two packages require different major versions of the same dependency
- Overly restrictive version ranges in package.json
- Using caret (^) or tilde (~) ranges that conflict
- Locked dependencies preventing resolution

## How to Fix

### Check Dependency Tree

```bash
npm ls <package-name>
```

### Use Overrides to Force Version

```json
{
  "overrides": {
    "conflicting-package": "^2.0.0"
  }
}
```

### Update Conflicting Packages

```bash
npm update <package-name>
```

### Check npm Outdated

```bash
npm outdated
```

### Pin Exact Versions

```bash
npm install package@1.2.3 --save-exact
```

## Examples

```bash
# Example 1: Check conflict
npm ls lodash
# my-app@1.0.0
# ├── package-a@1.0.0
# │   └── lodash@4.17.20
# └── package-b@2.0.0
#     └── lodash@3.10.1
# Fix: use overrides to force lodash@4

# Example 2: Outdated packages
npm outdated
# Fix: npm update to resolve conflicts
```

## Related Errors

- [npm Peer]({{< relref "/tools/npm/npm-peer" >}}) — ERESOLVE unable to resolve
- [npm Run Script Error]({{< relref "/tools/npm/npm-run-script-error" >}}) — script error
