---
title: "[Solution] npm 404 Not Found — package not found"
description: "Fix npm 404 not found error. Resolve missing package issues in npm."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm 404 Not Found — package not found

This error occurs when npm cannot find a package in the registry. The package may not exist, have been unpublished, or may require a different name.

## Common Causes

- Package name is misspelled
- Package was unpublished or removed from npm
- Package is in a private registry
- Package has been renamed

## How to Fix

### Check Package Name

```bash
npm search <partial-name>
```

### Verify Package Exists

```bash
npm view <package-name>
```

### Check for Typos

```bash
npm search react-daterpicker  # Typo: should be datepicker
```

### Check Private Registry

```bash
npm config get registry
```

### Search npm Registry

```bash
npm search <keyword>
```

### Use npm Info

```bash
npm info <package-name>
```

## Examples

```bash
# Example 1: Typo in package name
npm install react-daterpicker
# 404 Not Found - GET https://registry.npmjs.org/react-daterpicker
# Fix: npm install react-datepicker

# Example 2: Package unpublished
npm install old-unused-package
# 404 Not Found
# Fix: find alternative package

# Example 3: Check package info
npm info react
# name: 'react'
# version: '18.2.0'
```

## Related Errors

- [Registry Error]({{< relref "/tools/npm/registry-error" >}}) — registry connection issues
- [Node Modules Error]({{< relref "/tools/npm/node-modules-error" >}}) — node_modules issues
