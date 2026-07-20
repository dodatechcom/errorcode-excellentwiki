---
title: "[Solution] npm org Ls Failed"
description: "Resolve npm org list failures by verifying org membership, checking authentication, and ensuring the organization name is correct."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm org Ls Failed

This guide helps you diagnose and resolve npm org Ls Failed errors encountered when running npm commands.

## Common Causes

- You are not a member of the specified organization
- Authentication token has expired or is invalid
- Organization name does not exist on npm

## How to Fix

### Re-login to npm

```bash
npm login
```

### List Organizations

```bash
npm org ls <org>
```

### Check Available Orgs

```bash
npm org ls
```

## Examples

```bash
# Auth expired
npm org ls myorg
# Fix: Re-authenticate
npm login

# Not org member
npm org ls myorg
# Fix: Verify membership
npm profile get

```

## Related Errors

- [Set Failed]({{< relref "/tools/npm/org-set-failed" >}}) -- set org error
- [Rm Failed]({{< relref "/tools/npm/org-rm-failed" >}}) -- remove org error
