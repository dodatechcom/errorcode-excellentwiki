---
title: "[Solution] npm ERR! EACCES: permission denied Error Fix"
description: "Fix npm ERR! EACCES: permission denied when running npm install. Resolve permission issues with node_modules and global packages."
languages: ["javascript"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["npm", "eacces", "permission-denied", "node-modules", "install"]
weight: 5
---

# npm ERR! EACCES — permission denied

This error occurs when npm lacks the necessary file system permissions to read, write, or create files. It typically happens when `node_modules` was created by a different user (e.g., root) or when global packages require elevated permissions.

## What This Error Means

Common error messages:

- `npm ERR! code EACCES npm ERR! syscall open`
- `npm ERR! Error: EACCES: permission denied, open '/usr/lib/node_modules/...'`
- `npm ERR! code EACCES npm ERR! syscall access`

The `EACCES` code means "Error ACCESS denied" — the operating system denied the requested file operation.

## Common Causes

```bash
# Cause 1: node_modules created with sudo, now running without
sudo npm install  # creates root-owned node_modules
npm install       # EACCES - can't write to root-owned directory

# Cause 2: Global npm packages installed with wrong permissions
sudo npm install -g typescript
npm install -g eslint  # EACCES

# Cause 3: /usr/lib or /usr/local owned by root
ls -la /usr/lib/node_modules/
# drwxr-xr-x root root ...

# Cause 4: Package tries to create files in protected directory
npm install native-module  # tries to write to /usr/lib
```

## How to Fix

### Fix 1: Fix npm directory permissions

```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### Fix 2: Fix node_modules ownership

```bash
# Remove and reinstall
rm -rf node_modules
npm install

# Or fix ownership (if you know previous owner)
sudo chown -R $(whoami) ~/.npm
sudo chown -R $(whoami) node_modules
```

### Fix 3: Use npx instead of global install

```bash
# Instead of global install
npx typescript --version

# Or for one-off commands
npx eslint src/
```

### Fix 4: Configure npm to use a different directory

```bash
# Use local directory for npm cache
npm config set cache ~/.npm-cache --global

# Create npm directory in home
mkdir -p ~/.npm
npm config set cache ~/.npm
```

## Examples

```bash
# This triggers EACCES
sudo npm install express
npm install body-parser
# npm ERR! code EACCES
# npm ERR! Error: EACCES: permission denied, mkdir '/usr/lib/node_modules/express'

# Fix: reinstall without sudo
rm -rf node_modules
npm install
# Works correctly
```

## Related Errors

- [ENOSPC]({{< relref "/languages/javascript/enospc" >}}) — disk full
- [ENOENT npm]({{< relref "/languages/javascript/enoent-npm" >}}) — package.json missing
- [Permission Model Denied]({{< relref "/languages/javascript/node-permission-error" >}}) — Node.js permission model
