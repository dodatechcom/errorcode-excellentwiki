---
title: "[Solution] npm install ENOSPC no space left"
description: "Fix npm 'ENOSPC no space left' error. Resolve npm installation failures due to insufficient disk space or inode exhaustion."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ENOSPC no space left

ENOSPC: no space left on device

This error occurs when the filesystem has run out of disk space or inodes during npm operations.

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
