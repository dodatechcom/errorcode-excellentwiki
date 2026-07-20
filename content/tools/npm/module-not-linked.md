---
title: "[Solution] npm link Module Not Linked"
description: "Handle npm link module not linked errors by verifying package names, checking global link registry, and recreating broken symlinks."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm link Module Not Linked

This guide helps you diagnose and resolve npm link Module Not Linked errors encountered when running npm commands.

## Common Causes

- Package was not properly linked with npm link before npm unlink
- Global symlink was removed but local reference still exists
- Package name in node_modules does not match the linked package

## How to Fix

### Check Global Links

```bash
npm ls -g --depth=0
```

### Recreate the Link

```bash
npm link <package-name>
```

### Remove Broken Link

```bash
npm unlink <package-name> && npm link <package-name>
```

## Examples

```bash
# Link not found in project
npm link my-pkg
# Fix: Verify global link exists
npm ls -g --depth=0 | grep my-pkg

# Broken symlink in node_modules
npm link my-pkg
# Fix: Remove and recreate
rm -rf node_modules/my-pkg
npm link my-pkg

```

## Related Errors

- [Target Not Found]({{< relref "/tools/npm/target-not-found" >}}) -- target error
- [Not Linked]({{< relref "/tools/npm/not-linked" >}}) -- unlink error
