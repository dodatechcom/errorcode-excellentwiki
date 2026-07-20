---
title: "[Solution] npm publish E412 Precondition Failed"
description: "Resolve E412 precondition failed errors in npm publish by refreshing authentication, clearing cache, and retrying the publish operation."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm publish E412 Precondition Failed

This guide helps you diagnose and resolve npm publish E412 Precondition Failed errors encountered when running npm commands.

## Common Causes

- Server-side precondition check failed due to stale authentication
- Package metadata on registry is inconsistent with local version
- Concurrent publish operation modified the package state

## How to Fix

### Re-login to npm

```bash
npm logout && npm login
```

### Clear npm Cache

```bash
npm cache clean --force
```

### Retry Publish After Delay

```bash
sleep 30 && npm publish
```

## Examples

```bash
# Stale auth causing precondition failure
npm publish
# Fix: Re-authenticate
npm logout
npm login
npm publish

# Concurrent publish conflict
npm publish
# Fix: Wait and retry
sleep 60
npm cache clean --force
npm publish

```

## Related Errors

- [E409 Conflict]({{< relref "/tools/npm/publish-e409-conflict-version-exists" >}}) -- version conflict
- [E401 Unauthorized Publish]({{< relref "/tools/npm/publish-e401-unauthorized" >}}) -- auth error
