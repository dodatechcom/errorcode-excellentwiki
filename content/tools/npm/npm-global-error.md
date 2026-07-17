---
title: "[Solution] npm Global Install Permission Error"
description: "Fix npm global install permission errors. Resolve EACCES permission denied issues."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["global", "permission", "eacces", "install", "npm"]
weight: 5
---

A npm global install permission error occurs when you lack write access to the global node_modules directory. This is common on Linux/macOS systems.

## Common Causes

- Global npm directory requires root permissions
- npm was installed with sudo
- Directory ownership is incorrect
- Using system Node.js installation instead of version manager

## How to Fix

### Change npm Global Directory

```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
```

### Add to Shell Profile

```bash
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

### Use nvm for Node.js

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install --lts
```

### Fix Directory Permissions (not recommended)

```bash
sudo chown -R $(whoami) $(npm config get prefix)/{lib/node_modules,bin,share}
```

## Examples

```bash
# Example 1: Permission denied
npm install -g create-react-app
# EACCES: permission denied, mkdir '/usr/local/lib/node_modules'
# Fix: change npm global directory

# Example 2: Check global prefix
npm config get prefix
# /usr/local
# Fix: change to ~/.npm-global
```

## Related Errors

- [npm Npx Error]({{< relref "/tools/npm/npm-npx-error" >}}) — npx command not found
- [npm Cache Error]({{< relref "/tools/npm/npm-cache-error" >}}) — npm cache error
