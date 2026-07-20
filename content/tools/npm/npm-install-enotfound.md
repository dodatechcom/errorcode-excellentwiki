---
title: "[Solution] npm install ENOTFOUND error"
description: "Fix npm 'ENOTFOUND' error. Resolve npm DNS resolution failures when the registry hostname cannot be resolved."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ENOTFOUND error

ENOTFOUND: getaddrinfo ENOTFOUND registry.npmjs.org

This error occurs when the DNS lookup for the npm registry fails.

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
