---
title: "[Solution] npm Audit Vulnerabilities — vulnerabilities found"
description: "Fix npm audit vulnerabilities. Understand and resolve security vulnerabilities in dependencies."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["audit", "vulnerabilities", "security", "dependencies", "npm"]
weight: 5
---

# npm Audit Vulnerabilities — vulnerabilities found

`npm audit` reports security vulnerabilities in your project's dependencies. These range from low to critical severity and may affect your application.

## Common Causes

- Outdated dependencies with known vulnerabilities
- Transitive dependencies with security issues
- Using deprecated or unmaintained packages
- Dependency tree includes vulnerable versions

## How to Fix

### Run Audit

```bash
npm audit
```

### Automatically Fix Vulnerabilities

```bash
npm audit fix
```

### Force Fix (may include breaking changes)

```bash
npm audit fix --force
```

### Check for Specific Vulnerability

```bash
npm audit --json | jq '.vulnerabilities'
```

### Update Dependencies Manually

```bash
npm update
```

### Use npm Overrides

```json
{
  "overrides": {
    "vulnerable-package": "^2.0.0"
  }
}
```

## Examples

```bash
# Example 1: Run audit
npm audit
# found 3 vulnerabilities (1 moderate, 2 high)
# Fix: npm audit fix

# Example 2: Force fix breaking changes
npm audit fix --force
# fix auditorily breaking change in lodash
# Fix: test application thoroughly after update

# Example 3: Check specific package
npm audit --json | jq '.vulnerabilities.lodash'
```

## Related Errors

- [Peer Dependency]({{< relref "/tools/npm/peer-dep" >}}) — peer dependency conflict
- [Registry Error]({{< relref "/tools/npm/registry-error" >}}) — registry connection issues
