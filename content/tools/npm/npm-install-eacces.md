---
title: "[Solution] npm install EACCES permission denied"
description: "Fix npm 'EACCES permission denied' error. Resolve permission issues when installing npm packages globally or locally."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install EACCES permission denied

EACCES: permission denied, access '/usr/local/lib/node_modules'

This error occurs when npm does not have write permissions to the installation directory. Global installs typically require root or proper user permissions.

## How to Fix

### Check npm Version

```bash
npm --version
node --version
```

### Clear npm Cache

```bash
npm cache clean --force
```

### Check Registry Status

```bash
npm ping
npm config get registry
```

### Verify Permissions

```bash
ls -la $(npm root -g)
whoami
```

## Related Errors

- [Module Not Found]({{< relref "/tools/npm/module-not-found" >}}) -- missing module
- [ERESOLVE]({{< relref "/tools/npm/peer-deps" >}}) -- dependency conflict
