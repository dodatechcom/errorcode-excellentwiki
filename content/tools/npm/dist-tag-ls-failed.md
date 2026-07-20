---
title: "[Solution] npm dist-tag Ls Failed"
description: "Handle npm dist-tag ls failures by verifying package name, checking registry connectivity, and ensuring proper authentication."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm dist-tag Ls Failed

This guide helps you diagnose and resolve npm dist-tag Ls Failed errors encountered when running npm commands.

## Common Causes

- Package does not exist on the registry
- Registry is unreachable from your network
- Authentication is required for private packages

## How to Fix

### Verify Package Exists

```bash
npm view <package>
```

### Check Registry Connectivity

```bash
curl -I https://registry.npmjs.org
```

### List Tags

```bash
npm dist-tag ls <package>
```

## Examples

```bash
# Package not found
npm dist-tag ls unknown-pkg
# Fix: Verify package name
npm search unknown-pkg

# Registry unreachable
npm dist-tag ls my-pkg
# Fix: Check connectivity
npm config get registry

```

## Related Errors

- [Add Failed]({{< relref "/tools/npm/dist-tag-add-failed" >}}) -- add tag error
- [Rm Failed]({{< relref "/tools/npm/dist-tag-rm-failed" >}}) -- remove tag error
