---
title: "[Solution] npm unlink Not Linked"
description: "Handle npm unlink not linked errors by checking current link status, manually removing symlinks, and cleaning up node_modules references."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm unlink Not Linked

This guide helps you diagnose and resolve npm unlink Not Linked errors encountered when running npm commands.

## Common Causes

- Package was never linked in the current project
- Link was already removed but node_modules reference persists
- Symlink was manually created outside of npm link

## How to Fix

### Check Current Links

```bash
ls -la node_modules/ | grep ^l
```

### Manually Remove Symlink

```bash
rm -rf node_modules/<package>
```

### Clean and Reinstall

```bash
rm -rf node_modules && npm install
```

## Examples

```bash
# Package not found to unlink
npm unlink my-pkg
# Fix: Check if linked
ls -la node_modules/my-pkg
# If not symlink, just uninstall: npm uninstall my-pkg

# Stale link reference
npm unlink my-pkg
# Fix: Manually clean up
rm -rf node_modules/my-pkg
npm install

```

## Related Errors

- [Module Not Linked]({{< relref "/tools/npm/module-not-linked" >}}) -- link error
- [EACCES Permission]({{< relref "/tools/npm/link-eacces-permission" >}}) -- permission error
