---
title: "[Solution] npm ls Unmet Peer Dependency"
description: "Fix npm ls unmet peer dependency warnings by installing required peer packages, updating versions, or configuring peer dep resolution."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm ls Unmet Peer Dependency

This guide helps you diagnose and resolve npm ls Unmet Peer Dependency errors encountered when running npm commands.

## Common Causes

- A required peer dependency was not installed alongside the package
- Peer dependency version range is not satisfied by installed version
- npm version 7+ strict peer dependency checking is enabled

## How to Fix

### Install Missing Peer Dependencies

```bash
npm install <peer-package>@<version>
```

### Check Peer Requirements

```bash
npm view <package> peerDependencies
```

### Allow Legacy Peer Dependencies

```bash
npm config set legacy-peer-deps true
```

## Examples

```bash
# React peer dep not installed
npm install some-react-lib
# Fix: Install peer dependencies
npm install react react-dom@18

# Version conflict with peer deps
npm install plugin
# Fix: Use legacy peer deps resolution
npm config set legacy-peer-deps true

```

## Related Errors

- [Cycle Detected]({{< relref "/tools/npm/cycle-detected" >}}) -- circular dependency
- [ERESOLVE Dependency Conflict]({{< relref "/tools/npm/peer-deps" >}}) -- dependency conflict
