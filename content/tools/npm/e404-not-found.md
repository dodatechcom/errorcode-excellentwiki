---
title: "[Solution] npm install E404 Not Found"
description: "Handle E404 not found errors in npm install by verifying package names, checking typos, and confirming registry availability."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install E404 Not Found

This guide helps you diagnose and resolve npm install E404 Not Found errors encountered when running npm commands.

## Common Causes

- Package name is misspelled or does not exist on the registry
- Package has been unpublished or removed from npm
- Scoped package requires access to a private registry

## How to Fix

### Search for the Correct Package Name

```bash
npm search <partial-name>
```

### Verify Package Exists on npm

```bash
npm view <package-name>
```

### Check for Scoping Issues

```bash
npm config get @scope:registry
```

## Examples

```bash
# Typo in package name
npm install reactt
# Fix: Search for correct name
npm search react
npm install react

# Unpublished private package
npm install @private/pkg
# Fix: Verify scope registry
cat .npmrc

```

## Related Errors

- [Module Not Found]({{< relref "/tools/npm/module-not-found" >}}) -- missing module
- [E401 Unauthorized]({{< relref "/tools/npm/e401-unauthorized" >}}) -- authentication error
