---
title: "[Solution] npm ls Extraneous Package"
description: "Resolve npm ls extraneous package warnings by removing packages not listed in package.json and cleaning up unused dependencies."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm ls Extraneous Package

This guide helps you diagnose and resolve npm ls Extraneous Package errors encountered when running npm commands.

## Common Causes

- Package was installed directly without saving to package.json
- package.json was edited to remove a dependency but node_modules was not cleaned
- Manual npm install without --save flag left orphaned packages

## How to Fix

### List Extraneous Packages

```bash
npm ls --parseable | grep extraneous
```

### Remove Extraneous Packages

```bash
npm prune
```

### Clean Install from Scratch

```bash
rm -rf node_modules && npm install
```

## Examples

```bash
# Orphaned packages in node_modules
npm ls
# Fix: Prune extraneous packages
npm prune

# Manual install not saved
npm ls
# Fix: Add to package.json or remove
npm install <package> --save

```

## Related Errors

- [Cycle Detected]({{< relref "/tools/npm/cycle-detected" >}}) -- circular dependency
- [Missing Dependency Tree]({{< relref "/tools/npm/missing-dependency-tree" >}}) -- broken tree
