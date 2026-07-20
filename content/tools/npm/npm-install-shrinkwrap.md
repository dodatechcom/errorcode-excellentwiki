---
title: "[Solution] npm install shrinkwrap conflict"
description: "Fix npm 'shrinkwrap conflict' error. Resolve npm-shrinkwrap.json and package-lock.json conflicts."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install shrinkwrap conflict

npm ERR! Found: package@version
npm ERR! node_modules/package
npm ERR! package.json: package@other-version

This error occurs when the shrinkwrap file conflicts with package.json.

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
