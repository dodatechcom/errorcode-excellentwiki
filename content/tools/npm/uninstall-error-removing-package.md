---
title: "[Solution] npm uninstall Error Removing Package"
description: "Fix npm uninstall errors when removing packages by handling permission issues, cleaning symlinks, and resolving locked file handles."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm uninstall Error Removing Package

This guide helps you diagnose and resolve npm uninstall Error Removing Package errors encountered when running npm commands.

## Common Causes

- Permission denied on node_modules directory or bin links
- Package files are locked by another process
- Broken symlinks in global bin directory causing removal failure

## How to Fix

### Fix Permissions on node_modules

```bash
sudo chown -R $(whoami) node_modules
```

### Force Remove Package

```bash
npm uninstall <package> --force
```

### Manually Remove and Clean Up

```bash
rm -rf node_modules/<package> && npm cache clean --force
```

## Examples

```bash
# Permission error on global uninstall
npm uninstall -g <package>
# Fix: Fix global directory permissions
sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}

# File locked during uninstall
npm uninstall express
# Fix: Close other processes using the files
rm -rf node_modules/express

```

## Related Errors

- [EACCES Permission Denied]({{< relref "/tools/npm/eacces-permission-denied" >}}) -- permission error
- [Module Not Linked]({{< relref "/tools/npm/module-not-linked" >}}) -- symlink error
