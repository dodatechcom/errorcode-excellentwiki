---
title: "[Solution] npm install unsupported platform error"
description: "Fix npm 'unsupported platform' error. Resolve installation failures due to operating system or architecture incompatibility."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install unsupported platform error

npm WARN notsup Unsupported platform: package@version: wanted {os: "darwin"}, current: {os: "linux"}

This warning indicates the package does not support the current operating system.

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
