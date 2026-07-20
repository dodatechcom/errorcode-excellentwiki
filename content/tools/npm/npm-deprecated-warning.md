---
title: "[Solution] npm Deprecated Package Warning"
description: "Fix npm deprecated package warnings. Handle deprecated dependency warnings."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

npm displays deprecated warnings when a package you depend on has been marked as deprecated by its author. While not always breaking, deprecated packages may have security issues or lack maintenance.

## Common Causes

- Using a package that has been superseded by a newer alternative
- Package author has abandoned the package
- Package has known security vulnerabilities
- Package functionality has been absorbed into another package

## How to Fix

### Check Which Packages Are Deprecated

```bash
npm ls --depth=0
npm audit
```

### Find Alternative Packages

```bash
npm search <alternative-package>
```

### Update to Replacement Package

```bash
npm uninstall <deprecated-package>
npm install <new-package>
```

### Suppress Warnings (temporary)

```bash
npm install --no-fund --no-audit
```

### Check npm Deprecation Notices

```bash
npm info <package-name> deprecated
```

## Examples

```bash
# Example 1: Deprecated package
npm install request
# npm WARN deprecated request@2.88.2: request has been deprecated
# Fix: use node-fetch or axios instead

# Example 2: Check deprecation
npm info request deprecated
# 'request has been deprecated, see https://github.com/request/request/issues/3142'
```

## Related Errors

- [npm Audit]({{< relref "/tools/npm/npm-audit" >}}) -- security vulnerabilities found
- [npm Peer]({{< relref "/tools/npm/npm-peer" >}}) -- ERESOLVE unable to resolve
