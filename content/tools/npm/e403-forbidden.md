---
title: "[Solution] npm install E403 Forbidden"
description: "Resolve E403 forbidden errors in npm install by checking package access permissions, registry policies, and IP-based restrictions."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install E403 Forbidden

This guide helps you diagnose and resolve npm install E403 Forbidden errors encountered when running npm commands.

## Common Causes

- Your account does not have permission to access the package
- Registry is blocking requests from your IP address or region
- Package has been marked as private or restricted

## How to Fix

### Check Package Access

```bash
npm access ls-packages
```

### Verify Registry Settings

```bash
npm config get registry
```

### Contact Package Owner for Access

```bash
npm owner ls <package-name>
```

## Examples

```bash
# Access denied to private package
npm install @company/internal-lib
# Fix: Request access
npm owner ls @company/internal-lib

# IP blocked by registry
npm install some-package
# Fix: Use VPN or switch registry
npm config set registry https://registry.npmmirror.com

```

## Related Errors

- [E401 Unauthorized]({{< relref "/tools/npm/e401-unauthorized" >}}) -- authentication error
- [Scope Not Allowed]({{< relref "/tools/npm/scope-not-allowed" >}}) -- scope permission denied
