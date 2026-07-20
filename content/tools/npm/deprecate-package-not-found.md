---
title: "[Solution] npm deprecate Package Not Found"
description: "Resolve npm deprecate package not found errors by verifying package ownership, checking exact package name, and confirming registry availability."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm deprecate Package Not Found

This guide helps you diagnose and resolve npm deprecate Package Not Found errors encountered when running npm commands.

## Common Causes

- Package does not exist on the registry
- Package name is misspelled or uses wrong scope
- You are not the package owner or maintainer

## How to Fix

### Verify Package Exists

```bash
npm view <package>
```

### Check Maintainer Status

```bash
npm owner ls <package>
```

### Deprecate with Correct Syntax

```bash
npm deprecate <package>@<range> '<message>'
```

## Examples

```bash
# Misspelled package name
npm deprecate old-pkg@'*' 'Use new-pkg'
# Fix: Verify correct name
npm search old-pkg

# Not package maintainer
npm deprecate my-pkg@'<2' 'Deprecated'
# Fix: Get maintainer access
npm owner add <you> my-pkg

```

## Related Errors

- [Message Too Long]({{< relref "/tools/npm/deprecate-message-too-long" >}}) -- message error
- [E401 Unauthorized]({{< relref "/tools/npm/e401-unauthorized" >}}) -- auth error
