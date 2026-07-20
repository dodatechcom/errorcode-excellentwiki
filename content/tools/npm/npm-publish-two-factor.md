---
title: "[Solution] npm publish two-factor authentication error"
description: "Fix npm 'two-factor authentication' error. Resolve npm publish failures requiring OTP codes."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm publish two-factor authentication error

npm ERR! 403 Forbidden - PUT ... - requires a one-time password

This error occurs when publishing to a package that requires two-factor authentication.

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
