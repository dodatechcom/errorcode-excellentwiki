---
title: "[Solution] npm install E404 package not found"
description: "Fix npm 'E404 package not found' error. Resolve npm install failures when a package does not exist in the registry."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install E404 package not found

npm ERR! 404 Not Found - GET https://registry.npmjs.org/<package>

This error occurs when the specified package does not exist in the npm registry.

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
