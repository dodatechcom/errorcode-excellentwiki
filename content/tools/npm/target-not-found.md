---
title: "[Solution] npm link Target Not Found"
description: "Resolve npm link target not found errors by verifying the source package path, ensuring package.json exists, and checking the link target directory."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm link Target Not Found

This guide helps you diagnose and resolve npm link Target Not Found errors encountered when running npm commands.

## Common Causes

- The directory specified for linking does not contain a package.json
- Symlink target path does not exist or was moved
- Relative path to link target is incorrect

## How to Fix

### Verify package.json Exists

```bash
ls package.json
```

### Use Absolute Path for Link

```bash
npm link /absolute/path/to/package
```

### Check Target Directory

```bash
ls -la <target-path>
```

## Examples

```bash
# No package.json in target
npm link ../my-lib
# Fix: Ensure target has package.json
cd ../my-lib && ls package.json

# Moved or deleted target
npm link my-linked-pkg
# Fix: Verify path is correct
ls -la $(npm config get prefix)/lib/node_modules/my-linked-pkg

```

## Related Errors

- [Module Not Linked]({{< relref "/tools/npm/module-not-linked" >}}) -- link error
- [Module Not Found]({{< relref "/tools/npm/module-not-found" >}}) -- missing module
