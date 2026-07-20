---
title: "[Solution] npm publish invalid TOTP code"
description: "Fix npm 'invalid TOTP code' error. Resolve npm publish failures due to incorrect one-time passwords."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm publish invalid TOTP code

npm ERR! 401 Unauthorized - Invalid one-time password

This error occurs when the two-factor authentication OTP code is incorrect or expired.

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
