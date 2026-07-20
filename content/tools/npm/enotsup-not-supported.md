---
title: "[Solution] npm install ENOTSUP Not Supported"
description: "Handle ENOTSUP not supported errors in npm install by verifying platform compatibility, updating npm, and checking package requirements."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ENOTSUP Not Supported

This guide helps you diagnose and resolve npm install ENOTSUP Not Supported errors encountered when running npm commands.

## Common Causes

- Package does not support your current operating system or platform
- npm version is too old to support the package installation method
- Package uses native bindings not available on your architecture

## How to Fix

### Check Package Platform Requirements

```bash
npm view <package> os cpu
```

### Update npm to Latest Version

```bash
npm install -g npm@latest
```

### Use Platform-Specific Alternative

```bash
npm search <package>-<platform>
```

## Examples

```bash
# Package only supports Linux
npm install linux-only-pkg
# Fix: Check supported platforms
npm view linux-only-pkg os

# Architecture mismatch
npm install arm-native-pkg
# Fix: Check CPU requirements
npm view arm-native-pkg cpu

```

## Related Errors

- [Engine Mismatch]({{< relref "/tools/npm/ebadengine-engine-mismatch" >}}) -- version incompatibility
- [Build Failed]({{< relref "/tools/npm/build-failed" >}}) -- compilation error
