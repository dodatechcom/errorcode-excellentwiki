---
title: "[Solution] npm ls Missing Dependency Tree"
description: "Fix npm ls missing dependency tree errors by reinstalling dependencies, verifying package-lock.json, and resolving broken node_modules."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm ls Missing Dependency Tree

This guide helps you diagnose and resolve npm ls Missing Dependency Tree errors encountered when running npm commands.

## Common Causes

- package-lock.json is missing or corrupted
- node_modules structure is incomplete or broken
- Dependency tree was manually modified outside of npm

## How to Fix

### Regenerate package-lock.json

```bash
rm package-lock.json && npm install
```

### Full Clean Reinstall

```bash
rm -rf node_modules package-lock.json && npm install
```

### Check for Workspace Issues

```bash
npm ls --workspaces
```

## Examples

```bash
# Missing package-lock.json
npm ls
# Fix: Regenerate lock file
rm -rf node_modules package-lock.json
npm install

# Broken node_modules
npm ls
# Fix: Full clean reinstall
rm -rf node_modules package-lock.json
npm cache clean --force
npm install

```

## Related Errors

- [Cycle Detected]({{< relref "/tools/npm/cycle-detected" >}}) -- circular dependency
- [Unmet Peer Dependency]({{< relref "/tools/npm/unmet-peer-dependency" >}}) -- missing peer dep
