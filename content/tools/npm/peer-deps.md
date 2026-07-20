---
title: "[Solution] npm ERESOLVE -- Unable to Resolve Dependency Tree"
description: "Fix npm ERESOLVE unable to resolve dependency tree error. Resolve peer dependency conflicts with npm."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm ERESOLVE -- Unable to Resolve Dependency Tree

ERESOLVE occurs when npm cannot automatically resolve conflicting peer dependency requirements between packages. This is common when different packages require incompatible versions of the same dependency.

## Common Causes

- Conflicting peer dependency versions between packages
- Outdated lock file not reflecting current dependency tree
- Installing packages that require different major versions of a shared dependency
- Using npm v7+ which enforces strict peer dependency resolution

## How to Fix

### Use the --legacy-peer-deps Flag

```bash
npm install --legacy-peer-deps
```

### Force the Installation

```bash
npm install --force
```

### Use npm Overrides

```json
{
  "overrides": {
    "old-package": {
      "dependency": "^2.0.0"
    }
  }
}
```

### Delete node_modules and Lock File

```bash
rm -rf node_modules package-lock.json
npm install
```

### Use a Specific Package Version

```bash
npm install package-name@specific-version
```

## Examples

```bash
# Example 1: Conflicting React versions
npm install react-datepicker
# ERESOLVE unable to resolve dependency tree
# react-datepicker peer-depends on react@^17, but project uses react@18
# Fix: npm install react-datepicker --legacy-peer-deps

# Example 2: Clear and reinstall
rm -rf node_modules package-lock.json
npm install --legacy-peer-deps
```

## Related Errors

- [Module Not Found]({{< relref "/tools/npm/module-not-found" >}}) -- missing module after install
- [Dependency Failed]({{< relref "/tools/systemd/dependency-failed" >}}) -- service dependency failures
