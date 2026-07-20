---
title: "[Solution] npm install legacy peer deps error"
description: "Fix npm 'legacy peer deps' error. Resolve peer dependency conflicts using legacy resolution."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install legacy peer deps error

npm ERR! Could not resolve dependency:
npm ERR! peer dep missing

This error occurs when peer dependencies cannot be resolved automatically.

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
