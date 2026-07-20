---
title: "[Solution] npm publish Version Already Exists"
description: "Resolve version already exists errors in npm publish by incrementing version numbers, using prerelease tags, or publishing under a new scope."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm publish Version Already Exists

This guide helps you diagnose and resolve npm publish Version Already Exists errors encountered when running npm commands.

## Common Causes

- The version in package.json matches an already-published version
- package.json version was not updated before the publish command
- Another maintainer published the same version concurrently

## How to Fix

### Increment Version Before Publish

```bash
npm version patch --no-git-tag-version && npm publish
```

### Check All Published Versions

```bash
npm view <package> versions --json
```

### Use Prerelease Version

```bash
npm version prerelease --preid=alpha --no-git-tag-version
```

## Examples

```bash
# Forgot to bump version
npm publish
# Fix: Bump version first
npm version patch --no-git-tag-version
npm publish

# Need specific version
npm publish
# Check existing versions
npm view my-pkg versions --json

```

## Related Errors

- [E409 Conflict]({{< relref "/tools/npm/publish-e409-conflict-version-exists" >}}) -- version conflict
- [Version Invalid]({{< relref "/tools/npm/version-invalid" >}}) -- version format
