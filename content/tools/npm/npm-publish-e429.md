---
title: "[Solution] npm publish E429 rate limited"
description: "Fix npm 'E429 rate limited' error. Resolve npm publish rate limiting issues."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm publish E429 rate limited

npm ERR! 429 Too Many Requests

This error occurs when you have exceeded the npm registry rate limit for publishing packages.

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
