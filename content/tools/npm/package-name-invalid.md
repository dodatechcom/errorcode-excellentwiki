---
title: "[Solution] npm publish Package Name Invalid"
description: "Handle invalid package name errors in npm publish by following naming conventions, avoiding reserved words, and validating the name format."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm publish Package Name Invalid

This guide helps you diagnose and resolve npm publish Package Name Invalid errors encountered when running npm commands.

## Common Causes

- Package name contains uppercase letters or special characters
- Package name starts with a dot or underscore
- Package name is too long or contains URL-unsafe characters

## How to Fix

### Validate Package Name

```bash
node -e 'const n = require("./package.json").name; console.log(/^[a-z][a-z0-9._-]*$/.test(n))'
```

### Fix Package Name in package.json

```bash
# Edit package.json name field to use lowercase, valid characters
```

### Check npm Naming Rules

```bash
npm name <proposed-name> --registry https://registry.npmjs.org
```

## Examples

```bash
# Uppercase in package name
npm publish
# Fix: Use lowercase name
# Change "MyPackage" to "my-package" in package.json

# Special characters in name
npm publish
# Fix: Use only valid characters: a-z, 0-9, -, _, .
# Must start with letter

```

## Related Errors

- [Package Name Too Similar]({{< relref "/tools/npm/package-name-too-similar" >}}) -- name similarity
- [Scope Not Allowed]({{< relref "/tools/npm/scope-not-allowed" >}}) -- scope permission
