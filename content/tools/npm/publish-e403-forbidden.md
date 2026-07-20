---
title: "[Solution] npm publish E403 Forbidden Publish"
description: "Resolve E403 forbidden publish errors in npm by checking package permissions, verifying scope ownership, and confirming team membership."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm publish E403 Forbidden Publish

This guide helps you diagnose and resolve npm publish E403 Forbidden Publish errors encountered when running npm commands.

## Common Causes

- You are not a maintainer or collaborator on the target package
- Package scope is owned by a different organization
- Registry policy blocks publishing from your IP or account

## How to Fix

### Check Package Maintainers

```bash
npm owner ls <package>
```

### Verify Scope Ownership

```bash
npm org ls <scope>
```

### Request Publish Access

```bash
# Contact package owner to add you as maintainer
```

## Examples

```bash
# Not a package maintainer
npm publish
# Fix: Request maintainer access
npm owner ls <package>

# Scope owned by different org
npm publish --scope=@company
# Fix: Verify scope access
npm org ls company

```

## Related Errors

- [Scope Not Allowed]({{< relref "/tools/npm/scope-not-allowed" >}}) -- scope permission
- [E401 Unauthorized Publish]({{< relref "/tools/npm/publish-e401-unauthorized" >}}) -- auth error
