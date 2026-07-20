---
title: "[Solution] npm help-search error"
description: "Fix npm 'help-search' error. Resolve failures when searching npm documentation."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm help-search error

npm ERR! No results for <term>

This error occurs when the help search term does not match any documentation.

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
