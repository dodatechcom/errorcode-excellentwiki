---
title: "[Solution] npm hook Ls Failed"
description: "Resolve npm hook list failures by verifying authentication, checking npm account permissions, and ensuring registry connectivity."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm hook Ls Failed

This guide helps you diagnose and resolve npm hook Ls Failed errors encountered when running npm commands.

## Common Causes

- Not authenticated or auth token is expired
- Account does not have any webhooks configured
- Registry API endpoint is temporarily unavailable

## How to Fix

### Re-login to npm

```bash
npm login
```

### List Hooks

```bash
npm hook ls
```

### Check Registry Status

```bash
curl https://status.npmjs.org
```

## Examples

```bash
# Auth expired
npm hook ls
# Fix: Re-login
npm login
npm hook ls

# Empty hooks list is not an error
npm hook ls
# Fix: Create hooks if needed
npm hook create package https://server.com/hook --secret s

```

## Related Errors

- [Create Failed]({{< relref "/tools/npm/hook-create-failed" >}}) -- create hook error
- [Update Failed]({{< relref "/tools/npm/hook-update-failed" >}}) -- update hook error
