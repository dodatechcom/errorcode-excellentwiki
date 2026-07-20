---
title: "[Solution] npm install EEXIST file exists"
description: "Fix npm 'EEXIST file exists' error. Resolve npm installation conflicts when a file already exists at the target path."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install EEXIST file exists

EEXIST: file already exists

This error occurs when npm tries to create a file or symlink that already exists at the target location.

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
