---
title: "[Solution] VS Code Linter configuration error"
description: "Fix VS Code linting errors. Resolve issues with linter configuration, rules, and diagnostics in the editor."
date: 2026-07-17T10:00:00+08:00
draft: false
tool: "vscode"
tags: ["vscode", "ide", "linting", "eslint", "diagnostics"]
severity: "error"
---

# Linter configuration error

## Error Message

```
Linter configuration error: ESLint failed to load configuration from '.eslintrc.js'. Error: Cannot find module '@typescript-eslint/parser'.
```

## Common Causes

- Linter configuration file references missing dependencies
- ESLint or linter extension version is incompatible with project config
- Node modules not installed in the workspace root
- Linter plugin or parser package is not installed

## Solutions

### Solution 1: Install Missing Linter Dependencies

Install the missing ESLint parser and plugin packages that the configuration file requires.

```
npm install --save-dev eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
```

### Solution 2: Validate Linter Configuration

Run the linter from the command line to check for configuration errors before relying on the editor.

```
npx eslint --print-config src/index.js
```

### Solution 3: Enable Linter Auto-Fix

Configure the linter to automatically fix issues on save for common formatting and style problems.

```
{"editor.codeActionsOnSave": {"source.fixAll.eslint": "explicit", "source.fixAll.tslint": "explicit"}}
```

## Prevention Tips

- Keep ESLint and its plugins updated to compatible versions
- Use .eslintrc.json instead of .eslintrc.js for simpler configuration
- Check the Output panel under ESLint channel for detailed error logs

## Related Errors

- [Format document failed]({{< relref "/tools/vscode/format-error" >}})
- [TypeScript language service error]({{< relref "/tools/vscode/typescript-error" >}})
- [Python extension error]({{< relref "/tools/vscode/python-error" >}})
