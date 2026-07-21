---
title: "[Solution] Pip Extras Require Error"
description: "Fix pip extras_require errors. Install optional dependencies with correct extras syntax."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

## What This Error Means

The `pip` command encountered an extras_require error. This occurs when pip cannot find or install the specified extras for a package.

A typical error:

```
ERROR: No matching distribution found for <package>[<extra>]
```

## Why It Happens

This error occurs when:

- **Extra name wrong**: The extra name does not exist in the package's setup.
- **Package version old**: Older versions did not define the requested extra.
- **Missing brackets**: Incorrect syntax for specifying extras.
- **Extra not installed**: The extra requires additional system dependencies.

## How to Fix It

**Step 1: Check available extras**

```bash
pip index versions <package>
pip install <package> --dry-run
```

**Step 2: Install with correct syntax**

```bash
pip install "<package>[<extra>]"
pip install "<package>[<extra1>,<extra2>]"
```

**Step 3: Install all extras**

```bash
pip install "<package>[all]"
```

**Step 4: Check package documentation**

```bash
pip show <package>
```

## Common Mistakes

- **Missing quotes**: Always quote the package name with brackets in bash.
- **Wrong extra name**: Check package documentation for available extras.
- **Case sensitivity**: Extra names are case-sensitive.

## Related Pages

- [Pip Package Not Found](/tools/pip/pip-package-not-found/) — Package resolution issues
- [Pip Version Conflict](/tools/pip/pip-version-conflict/) — Dependency version conflicts
