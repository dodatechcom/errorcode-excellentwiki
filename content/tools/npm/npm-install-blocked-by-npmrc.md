---
title: "[Solution] npm install blocked by .npmrc error"
description: "Fix npm 'blocked by .npmrc' error. Resolve installation failures caused by restrictive npm configuration."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install blocked by .npmrc error

npm ERR! 403 Forbidden - Public registration is not allowed

This error occurs when .npmrc restricts package installations to a specific registry.

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
