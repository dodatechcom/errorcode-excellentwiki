---
title: "[Solution] npm install strict-ssl error"
description: "Fix npm 'strict-ssl' error. Resolve npm SSL verification failures behind corporate proxies."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install strict-ssl error

npm ERR! code ECONNRESET
npm ERR! errno ECONNRESET

This error can occur when strict-ssl verification fails behind a corporate proxy.

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
