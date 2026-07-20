---
title: "[Solution] npm publish E409 Conflict Version Exists"
description: "Fix E409 conflict errors in npm publish when a version already exists by bumping version, using prerelease tags, or unpublishing safely."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm publish E409 Conflict Version Exists

This guide helps you diagnose and resolve npm publish E409 Conflict Version Exists errors encountered when running npm commands.

## Common Causes

- The specified version number has already been published to the registry
- package.json version was not incremented before publishing
- Previous publish attempt partially succeeded, creating the version

## How to Fix

### Bump Package Version

```bash
npm version patch && npm publish
```

### Use Prerelease Version

```bash
npm version prerelease --preid=beta && npm publish
```

### Check Existing Versions

```bash
npm view <package> versions
```

## Examples

```bash
# Version already published
npm publish
# Fix: Bump version first
npm version patch
npm publish

# Need to publish same version
npm publish
# Fix: Use unpublish (within 72 hours)
npm unpublish <package>@<version>

```

## Related Errors

- [Version Already Exists]({{< relref "/tools/npm/version-already-exists" >}}) -- version conflict
- [Package Name Invalid]({{< relref "/tools/npm/package-name-invalid" >}}) -- name validation
