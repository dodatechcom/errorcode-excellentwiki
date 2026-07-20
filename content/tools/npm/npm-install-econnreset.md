---
title: "[Solution] npm install ECONNRESET error"
description: "Fix npm 'ECONNRESET' error. Resolve npm installation failures when the connection is reset by the remote server."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ECONNRESET error

ECONNRESET: connection reset by peer

This error occurs when the TCP connection to the npm registry is interrupted or reset by the server.

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
