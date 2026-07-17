---
title: "[Solution] npm Workspace Error — workspace link error"
description: "Fix npm workspace link errors. Resolve workspace dependency linking issues."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["workspace", "link", "monorepo", "symlink", "npm"]
weight: 5
---

An npm workspace error occurs when packages in a monorepo cannot properly link to each other. This causes missing dependencies or incorrect resolution.

## Common Causes

- Workspace packages not properly defined in root package.json
- Circular dependencies between workspace packages
- Version mismatches between workspace packages
- Symlinks broken after node_modules reinstall
- npm version does not support workspaces

## How to Fix

### Check Workspace Configuration

```json
{
  "workspaces": ["packages/*"]
}
```

### Install All Workspaces

```bash
npm install
```

### Run Script in Specific Workspace

```bash
npm run build -w <workspace-name>
```

### Verify Symlinks

```bash
ls -la node_modules/<workspace-package>
```

### Fix Broken Symlinks

```bash
rm -rf node_modules
npm install
```

## Examples

```bash
# Example 1: Workspace not found
npm run build -w my-package
# npm ERR! No workspaces found
# Fix: add workspaces config to root package.json

# Example 2: Circular dependency
npm install
# npm ERR! code ERESOLVE
# Fix: remove circular dependency between packages
```

## Related Errors

- [npm Run Script Error]({{< relref "/tools/npm/npm-run-script-error" >}}) — script execution failed
- [npm Peer]({{< relref "/tools/npm/npm-peer" >}}) — ERESOLVE unable to resolve
