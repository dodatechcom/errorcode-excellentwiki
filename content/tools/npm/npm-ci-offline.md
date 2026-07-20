---
title: "[Solution] npm ci offline error"
description: "Fix npm 'ci offline' error. Resolve npm CI failures when packages are not cached."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm ci offline error

npm ERR! code EOFFLINE: Can not install in offline mode, no cache

This error occurs when running npm ci with --offline but packages are not cached.

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
