---
title: "[Solution] npm config proxy error"
description: "Fix npm 'proxy' configuration error. Resolve npm connectivity issues through HTTP/HTTPS proxies."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm config proxy error

npm ERR! code ECONNREFUSED

This error can occur when the configured proxy server refuses the connection.

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
