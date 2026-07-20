---
title: "[Solution] npm publish E404 Package Not Found"
description: "Handle E404 package not found errors during npm publish by verifying package name, checking scope configuration, and confirming registry settings."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm publish E404 Package Not Found

This guide helps you diagnose and resolve npm publish E404 Package Not Found errors encountered when running npm commands.

## Common Causes

- Package name contains invalid characters or format
- Scope is not configured to point to the correct registry
- Package has not been previously published and requires initial setup

## How to Fix

### Verify Package Name Format

```bash
npm view <package-name>
```

### Check Scope Registry Config

```bash
npm config get @scope:registry
```

### Validate package.json Name Field

```bash
node -e 'console.log(require("./package.json").name)'
```

## Examples

```bash
# Scope pointing to wrong registry
npm publish --scope=@company
# Fix: Configure scope registry
npm config set @company:registry https://registry.npmjs.org

# Invalid package name
npm publish
# Fix: Check name format - must be lowercase with valid characters

```

## Related Errors

- [E401 Unauthorized Publish]({{< relref "/tools/npm/publish-e401-unauthorized" >}}) -- auth error
- [Version Already Exists]({{< relref "/tools/npm/version-already-exists" >}}) -- version conflict
