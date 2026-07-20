---
title: "[Solution] npm access Restricted Failed"
description: "Handle npm access restricted failures by verifying package ownership, understanding scope restrictions, and configuring private package visibility."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm access Restricted Failed

This guide helps you diagnose and resolve npm access Restricted Failed errors encountered when running npm commands.

## Common Causes

- Package owner has not granted restricted access permissions
- Organization settings prevent restricting package visibility
- Free npm account cannot create private packages

## How to Fix

### Verify Package Ownership

```bash
npm owner ls <package>
```

### Restrict Package Access

```bash
npm access restricted <package>
```

### Check npm Account Type

```bash
npm profile get
```

## Examples

```bash
# Free account cannot make private
npm access restricted my-pkg
# Fix: Upgrade npm account for private packages

# Not owner of package
npm access restricted my-pkg
# Fix: Get ownership first
npm owner add <username> my-pkg

```

## Related Errors

- [Public Failed]({{< relref "/tools/npm/access-public-failed" >}}) -- public access error
- [Grant Failed]({{< relref "/tools/npm/access-grant-failed" >}}) -- grant error
