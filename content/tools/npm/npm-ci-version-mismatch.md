---
title: "[Solution] npm ci version mismatch error"
description: "Fix npm 'ci version mismatch' error. Resolve npm CI failures when package-lock.json does not match package.json."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm ci version mismatch error

npm ERR! cipm: CI can't install: package-lock.json and package.json don't match

This error occurs when the package-lock.json is out of sync with package.json.

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
