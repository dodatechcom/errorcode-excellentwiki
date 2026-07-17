---
title: "[Solution] npm Peer Dependency Error — ERESOLVE unable to resolve"
description: "Fix npm peer dependency resolution errors. Resolve ERESOLVE conflicts."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["peer", "dependency", "eresolve", "resolution", "npm"]
weight: 5
---

An ERESOLVE error occurs when npm cannot automatically resolve peer dependency conflicts. Two packages require incompatible versions of the same dependency.

## Common Causes

- Packages require different major versions of a shared dependency
- Outdated lock file with stale dependency tree
- npm v7+ enforces strict peer dependency resolution
- Circular or conflicting dependency requirements

## How to Fix

### Use Legacy Peer Dependencies

```bash
npm install --legacy-peer-deps
```

### Force Installation

```bash
npm install --force
```

### Use npm Overrides

```json
{
  "overrides": {
    "package-a": {
      "shared-dep": "^2.0.0"
    }
  }
}
```

### Delete node_modules and Reinstall

```bash
rm -rf node_modules package-lock.json
npm install --legacy-peer-deps
```

### Pin Specific Package Version

```bash
npm install shared-dep@2.0.0
```

## Examples

```bash
# Example 1: React version conflict
npm install react-datepicker
# ERESOLVE unable to resolve dependency tree
# Fix: npm install react-datepicker --legacy-peer-deps

# Example 2: Clear and reinstall
rm -rf node_modules package-lock.json
npm install --legacy-peer-deps
```

## Related Errors

- [npm Audit]({{< relref "/tools/npm/npm-audit" >}}) — security vulnerabilities found
- [npm Version Error]({{< relref "/tools/npm/npm-version" >}}) — version conflict error
