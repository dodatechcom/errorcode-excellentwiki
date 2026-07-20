---
title: "[Solution] npm link EACCES Permission Error"
description: "Fix npm link EACCES permission errors by adjusting global directory ownership, using local linking, and fixing symlink creation permissions."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm link EACCES Permission Error

This guide helps you diagnose and resolve npm link EACCES Permission Error errors encountered when running npm commands.

## Common Causes

- Global node_modules directory is owned by root
- Symlink creation requires elevated privileges
- Target directory has restrictive write permissions

## How to Fix

### Fix Global Directory Ownership

```bash
sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}
```

### Use npm link --local

```bash
npm link --local
```

### Create Symlink Manually

```bash
ln -s $(pwd) $(npm config get prefix)/lib/node_modules/<package>
```

## Examples

```bash
# Global link fails with EACCES
npm link
# Fix: Fix global permissions
sudo chown -R $(whoami) $(npm config get prefix)/lib/node_modules
npm link

# Cannot create bin symlink
npm link
# Fix: Fix bin directory
sudo chown -R $(whoami) $(npm config get prefix)/bin

```

## Related Errors

- [EACCES Permission Denied]({{< relref "/tools/npm/eacces-permission-denied" >}}) -- permission error
- [Module Not Linked]({{< relref "/tools/npm/module-not-linked" >}}) -- link error
