---
title: "[Solution] npm dist-tag Add Failed"
description: "Fix npm dist-tag add failures by verifying version exists, checking authentication, and ensuring the tag name is valid for the package."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm dist-tag Add Failed

This guide helps you diagnose and resolve npm dist-tag Add Failed errors encountered when running npm commands.

## Common Causes

- Version does not exist on the registry for this package
- Tag name is reserved (latest) or contains invalid characters
- You lack maintainer permissions on the package

## How to Fix

### Check Published Versions

```bash
npm view <package> versions
```

### Add Dist-tag Correctly

```bash
npm dist-tag add <package>@<version> <tag-name>
```

### Verify Maintainer Status

```bash
npm owner ls <package>
```

## Examples

```bash
# Version does not exist
npm dist-tag add my-pkg@1.0.0 beta
# Fix: Verify version exists
npm view my-pkg versions

# Invalid tag name
npm dist-tag add my-pkg@1.0.0 'latest!'
# Fix: Use valid tag name
npm dist-tag add my-pkg@1.0.0 beta

```

## Related Errors

- [Rm Failed]({{< relref "/tools/npm/dist-tag-rm-failed" >}}) -- remove tag error
- [Ls Failed]({{< relref "/tools/npm/dist-tag-ls-failed" >}}) -- list tags error
