---
title: "[Solution] npm exec Permission Error"
description: "Fix npm exec permission errors by adjusting execute permissions, fixing bin directory ownership, and configuring npx to use local installs."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm exec Permission Error

This guide helps you diagnose and resolve npm exec Permission Error errors encountered when running npm commands.

## Common Causes

- Binary in node_modules/.bin lacks execute permission
- npx trying to create files in a protected directory
- Global bin directory has wrong ownership

## How to Fix

### Fix Binary Permissions

```bash
chmod +x node_modules/.bin/<binary>
```

### Fix Global Bin Directory

```bash
sudo chown -R $(whoami) $(npm config get prefix)/bin
```

### Use Local Package Instead

```bash
npm install <package> && npx <command>
```

## Examples

```bash
# Binary not executable
npx my-tool
# Fix: Set execute permission
chmod +x node_modules/.bin/my-tool
npx my-tool

# npx cache permission error
npx my-tool
# Fix: Fix npx cache permissions
chmod -R u+rw ~/.npm/_npx
npx my-tool

```

## Related Errors

- [EACCES Permission Denied]({{< relref "/tools/npm/eacces-permission-denied" >}}) -- permission error
- [Command Not Found]({{< relref "/tools/npm/exec-command-not-found" >}}) -- command error
