---
title: "[Solution] npm org Rm Failed"
description: "Handle npm org rm failures by verifying organization ownership, checking user membership, and preventing removal of the last org owner."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm org Rm Failed

This guide helps you diagnose and resolve npm org Rm Failed errors encountered when running npm commands.

## Common Causes

- User is not a member of the organization
- Cannot remove the last owner of an organization
- You lack owner permissions to remove members

## How to Fix

### Check Org Members

```bash
npm org ls <org>
```

### Verify User Membership

```bash
npm org ls <org> | grep <username>
```

### Remove User from Org

```bash
npm org rm <org> <username>
```

## Examples

```bash
# User not in org
npm org rm myorg user1
# Fix: Check members first
npm org ls myorg

# Cannot remove last owner
npm org rm myorg last-owner
# Fix: Add new owner first
npm org set myorg new-owner team --role=admin

```

## Related Errors

- [Set Failed]({{< relref "/tools/npm/org-set-failed" >}}) -- set org error
- [Ls Failed]({{< relref "/tools/npm/org-ls-failed" >}}) -- list org error
