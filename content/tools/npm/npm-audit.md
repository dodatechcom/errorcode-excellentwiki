---
title: "[Solution] npm Audit -- vulnerability found"
description: "Fix npm audit vulnerability errors. Resolve security vulnerabilities in dependencies."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

npm audit detects known security vulnerabilities in your project dependencies. It reports vulnerabilities with severity levels and suggests fixes.

## Common Causes

- Outdated packages with known vulnerabilities
- Using deprecated packages with security issues
- Transitive dependencies with vulnerabilities
- Using exact versions that lock to vulnerable ranges

## How to Fix

### Run npm Audit

```bash
npm audit
```

### Fix Vulnerabilities Automatically

```bash
npm audit fix
```

### Force Fix (including breaking changes)

```bash
npm audit fix --force
```

### Ignore Specific Vulnerabilities

```json
{
  "overrides": {
    "vulnerable-package": ">=1.0.0"
  }
}
```

### Check Audit Report

```bash
npm audit --json
```

## Examples

```bash
# Example 1: Audit and fix
npm audit
# 5 vulnerabilities (2 moderate, 3 high)
npm audit fix
# fixed 3 of 5 vulnerabilities

# Example 2: Force fix all
npm audit fix --force
# Fix: 5 vulnerabilities resolved
```

## Related Errors

- [npm Deprecated Warning]({{< relref "/tools/npm/npm-deprecated-warning" >}}) -- deprecated package warning
- [npm Integrity Error]({{< relref "/tools/npm/npm-integrity-error" >}}) -- integrity check failed
