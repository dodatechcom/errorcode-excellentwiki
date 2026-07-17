---
title: "[Solution] npm Run Script Error — script execution failed"
description: "Fix npm run script errors. Resolve script execution failures in npm."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["run", "script", "execution", "package.json", "npm"]
weight: 5
---

An npm run script error occurs when a script defined in `package.json` fails during execution. The error can come from the script itself or from missing dependencies.

## Common Causes

- Script command does not exist or has a typo
- Required executable is not installed (not in node_modules/.bin)
- Script depends on another script that failed
- Environment variables not set
- Operating system differences (Windows vs Linux)

## How to Fix

### Check Available Scripts

```bash
npm run
```

### Run Script with Verbose Output

```bash
npm run <script-name> --verbose
```

### Verify Executable Exists

```bash
ls node_modules/.bin/<command>
```

### Install Missing Dependencies

```bash
npm install
```

### Use Cross-Platform Scripts

```bash
npx cross-env NODE_ENV=production npm run build
```

## Examples

```bash
# Example 1: Script not found
npm run build
# npm ERR! Missing script: "build"
# Fix: add "build" script to package.json

# Example 2: Command not found
npm run lint
# sh: eslint: command not found
# Fix: npm install --save-dev eslint
```

## Related Errors

- [npm Npx Error]({{< relref "/tools/npm/npm-npx-error" >}}) — npx command not found
- [npm Workspace Error]({{< relref "/tools/npm/npm-workspace-error" >}}) — workspace link error
