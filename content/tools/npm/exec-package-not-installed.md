---
title: "[Solution] npm exec Package Not Installed"
description: "Handle npm exec package not installed errors by pre-installing the package, using npx with cache, and verifying package availability."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm exec Package Not Installed

This guide helps you diagnose and resolve npm exec Package Not Installed errors encountered when running npm commands.

## Common Causes

- Package is not available locally or in npx cache
- Registry cannot be reached to download the package
- Package name is incorrect or misspelled

## How to Fix

### Install Package Locally

```bash
npm install <package>
```

### Force npx to Download

```bash
npx --yes <package>
```

### Check Package Exists

```bash
npm view <package>
```

## Examples

```bash
# npx cannot find package
npx my-tool
# Fix: Install first
npm install my-tool
# Or force download
npx --yes my-tool

# Wrong package name
npx wrong-name
# Fix: Search and install correct name
npm search tool-name

```

## Related Errors

- [Command Not Found]({{< relref "/tools/npm/exec-command-not-found" >}}) -- command error
- [E404 Not Found]({{< relref "/tools/npm/e404-not-found" >}}) -- package not found
