---
title: "[Solution] npm install self-signed certificate error"
description: "Fix npm 'self-signed certificate' error. Resolve SSL certificate verification failures when using custom registries."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install self-signed certificate error

npm ERR! code ERR_TLS_CERT_ALTNAME_INVALID

This error occurs when the SSL certificate of the npm registry is self-signed or invalid.

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
