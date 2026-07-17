---
title: "[Solution] npm Peer Dependency Conflict"
description: "Fix npm peer dependency conflict errors. Resolve incompatible peer dependency versions."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm Peer Dependency Conflict — ERESOLVE unable to resolve

Peer dependency conflicts occur when two packages require incompatible versions of the same dependency. npm cannot automatically resolve these conflicts.

## Common Causes

- Packages require different major versions of shared dependency
- Outdated lock file with stale dependency tree
- Using npm v7+ which enforces strict peer dependency resolution
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

### Check Peer Dependencies

```bash
npm ls peer-deps
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

# Example 3: Check what's conflicting
npm ls peer-deps
# Fix: update conflicting packages
```

## Related Errors

- [Audit Vulnerabilities]({{< relref "/tools/npm/audit-vulnerabilities" >}}) — security vulnerabilities found
- [Lifecycle Error]({{< relref "/tools/npm/lifecycle-error" >}}) — lifecycle script error
