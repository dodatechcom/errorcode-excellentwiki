---
title: "[Solution] npm access Public Failed"
description: "Fix npm access public failures by verifying package ownership, checking scope settings, and ensuring proper authentication for visibility changes."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm access Public Failed

This guide helps you diagnose and resolve npm access Public Failed errors encountered when running npm commands.

## Common Causes

- You are not the package owner or maintainer
- Package is scoped and requires org-level visibility change
- npm access command syntax is incorrect

## How to Fix

### Verify Package Ownership

```bash
npm owner ls <package>
```

### Make Package Public

```bash
npm access public <package>
```

### Check Scope Settings

```bash
npm access ls-packages <scope>
```

## Examples

```bash
# Not package owner
npm access public my-pkg
# Fix: Ensure ownership
npm owner ls my-pkg

# Scoped package visibility
npm access public @scope/pkg
# Fix: Set scope visibility
npm access public @scope/pkg

```

## Related Errors

- [Restricted Failed]({{< relref "/tools/npm/access-restricted-failed" >}}) -- restricted error
- [Grant Failed]({{< relref "/tools/npm/access-grant-failed" >}}) -- grant error
