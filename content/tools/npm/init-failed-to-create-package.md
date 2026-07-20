---
title: "[Solution] npm init Failed to Create Package"
description: "Fix npm init failures to create package.json by checking directory permissions, resolving write errors, and providing required fields manually."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm init Failed to Create Package

This guide helps you diagnose and resolve npm init Failed to Create Package errors encountered when running npm commands.

## Common Causes

- Current directory does not have write permissions
- package.json already exists and init refuses to overwrite
- Disk is full preventing file creation

## How to Fix

### Check Directory Permissions

```bash
ls -la . | grep $(whoami)
```

### Force Init to Overwrite

```bash
npm init --yes --force
```

### Create package.json Manually

```bash
echo '{"name": "my-pkg", "version": "1.0.0"}' > package.json
```

## Examples

```bash
# Permission denied creating file
npm init
# Fix: Fix directory permissions
chmod 755 .
npm init

# package.json already exists
npm init
# Fix: Use --yes to confirm
npm init --yes

```

## Related Errors

- [Name Validation Failed]({{< relref "/tools/npm/init-name-validation-failed" >}}) -- name error
- [Version Invalid]({{< relref "/tools/npm/version-invalid" >}}) -- version error
