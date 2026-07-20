---
title: "[Solution] npm team Ls Failed"
description: "Resolve npm team list failures by verifying org membership, checking authentication, and ensuring the organization name is correct."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm team Ls Failed

This guide helps you diagnose and resolve npm team Ls Failed errors encountered when running npm commands.

## Common Causes

- You are not a member of the specified organization
- Authentication token has expired or is invalid
- Organization does not exist on npm

## How to Fix

### Verify Org Membership

```bash
npm org ls <org>
```

### Re-login to npm

```bash
npm login
```

### Check Available Teams

```bash
npm team ls <org>
```

## Examples

```bash
# Not org member
npm team ls myorg
# Fix: Verify you belong to the org
npm org ls myorg

# Auth expired
npm team ls myorg
# Fix: Re-authenticate
npm login
npm team ls myorg

```

## Related Errors

- [Create Failed]({{< relref "/tools/npm/team-create-failed" >}}) -- team creation error
- [Add User Failed]({{< relref "/tools/npm/team-add-user-failed" >}}) -- add user error
