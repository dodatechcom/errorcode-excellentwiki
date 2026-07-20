---
title: "[Solution] npm publish E412 precondition failed"
description: "Fix npm 'E412 precondition failed' error. Resolve npm publish failures due to unmet preconditions."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm publish E412 precondition failed

npm ERR! 412 Precondition Failed

This error occurs when npm publish fails due to unmet preconditions like two-factor authentication requirements.

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
