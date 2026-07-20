---
title: "[Solution] npm access ls-collaborators error"
description: "Fix npm 'access ls-collaborators' error. Resolve permission errors when listing package collaborators."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm access ls-collaborators error

npm ERR! 403 Forbidden - You do not have permission to list collaborators

This error occurs when you do not have read access to the package's collaborator list.

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
