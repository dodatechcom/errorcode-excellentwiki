---
title: "[Solution] npm access Grant Failed"
description: "Fix npm access grant failures by verifying team names, checking package ownership, and ensuring the grantee has an npm account."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm access Grant Failed

This guide helps you diagnose and resolve npm access Grant Failed errors encountered when running npm commands.

## Common Causes

- Team or user does not exist on npm
- Package is not owned by your account
- Grant permission level is invalid

## How to Fix

### Check Team Exists

```bash
npm team ls <org>
```

### Grant Access Correctly

```bash
npm access grant read-write <package> <team>
```

### Verify Package Ownership

```bash
npm owner ls <package>
```

## Examples

```bash
# Team not found for grant
npm access grant read-write my-pkg myorg:devs
# Fix: Verify team exists
npm team ls myorg

# Invalid permission level
npm access grant admin my-pkg user1
# Fix: Use valid level
npm access grant read-write my-pkg user1

```

## Related Errors

- [Revoke Failed]({{< relref "/tools/npm/access-revoke-failed" >}}) -- revoke error
- [Public Failed]({{< relref "/tools/npm/access-public-failed" >}}) -- public access error
