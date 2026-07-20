---
title: "[Solution] npm run-script Script Not Found"
description: "Fix npm run-script script not found errors by checking scripts in package.json, verifying script name spelling, and using correct run syntax."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm run-script Script Not Found

This guide helps you diagnose and resolve npm run-script Script Not Found errors encountered when running npm commands.

## Common Causes

- Script name is misspelled in the npm run command
- Script is not defined in package.json scripts field
- Package has been updated and script name has changed

## How to Fix

### Check Available Scripts

```bash
npm run
```

### Verify Script Name in package.json

```bash
node -e 'console.log(Object.keys(require("./package.json").scripts))'
```

### Run Script with Correct Name

```bash
npm run <script-name>
```

## Examples

```bash
# Script name typo
npm run devlop
# Fix: Check available scripts
npm run
# Use correct name: npm run develop

# Script not in package.json
npm run test
# Fix: Check scripts field
node -e 'console.log(require("./package.json").scripts)'

```

## Related Errors

- [Exit Code Non-Zero]({{< relref "/tools/npm/exit-code-non-zero" >}}) -- script failed
- [Module Not Found]({{< relref "/tools/npm/module-not-found" >}}) -- missing module
