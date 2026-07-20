---
title: "[Solution] npm install git dependency error"
description: "Fix npm 'git dependency' error. Resolve failures when installing packages from Git repositories."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install git dependency error

npm ERR! git clone <url>: remote: Repository not found

This error occurs when npm cannot clone a Git repository specified as a dependency.

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
