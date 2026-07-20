---
title: "[Solution] npm install EACCES Permission Denied"
description: "Fix EACCES permission denied errors during npm install by correcting directory ownership and npm configuration settings."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install EACCES Permission Denied

This guide helps you diagnose and resolve npm install EACCES Permission Denied errors encountered when running npm commands.

## Common Causes

- npm global directory owned by root instead of current user
- Project node_modules directory has restrictive permissions
- User lacks write access to the npm cache or global prefix directory

## How to Fix

### Change npm Global Directory Ownership

```bash
sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}
```

### Use npx to Run Packages Locally

```bash
npx create-react-app my-app
```

### Configure npm to Use a Different Directory

```bash
mkdir ~/.npm-global && npm config set prefix '~/.npm-global'
```

## Examples

```bash
# Global install without sudo fails
npm install -g typescript
# Fix: Change npm global directory
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH

# Permission error on node_modules
npm install
# Fix: Fix local directory permissions
sudo chown -R $(whoami) node_modules

```

## Related Errors

- [Module Not Found]({{< relref "/tools/npm/module-not-found" >}}) -- missing module
- [ENOSPC No Space Left]({{< relref "/tools/npm/enospc-no-space-left" >}}) -- disk space exhausted
