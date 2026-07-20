---
title: "[Solution] npm star Unstar Failed"
description: "Handle npm unstar failures by verifying login status, checking current star status, and ensuring the package name is correct."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm star Unstar Failed

This guide helps you diagnose and resolve npm star Unstar Failed errors encountered when running npm commands.

## Common Causes

- Package was not previously starred by the user
- Authentication token is invalid or expired
- Package name does not match exactly (case-sensitive)

## How to Fix

### Verify Login Status

```bash
npm whoami
```

### Check if Starred

```bash
npm stars
```

### Unstar the Package

```bash
npm unstar <package>
```

## Examples

```bash
# Not currently starred
npm unstar my-pkg
# Fix: Check your stars first
npm stars

# Auth issue
npm unstar my-pkg
# Fix: Re-login
npm login
npm unstar my-pkg

```

## Related Errors

- [Failed to Star]({{< relref "/tools/npm/star-failed-to-star" >}}) -- star error
- [E401 Unauthorized]({{< relref "/tools/npm/e401-unauthorized" >}}) -- auth error
