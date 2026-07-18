---
title: "[Solution] pip No Matching Distribution Error — Fix Package Not Found"
description: "Fix pip no matching distribution found errors when a package name or version does not exist. Verify names, check indexes, and configure custom repositories."
tools: ["pip"]
error-types: ["distribution-error"]
severities: ["error"]
weight: 5
---

This error means pip searched all configured indexes and found no package matching your request. The package name, version, or platform constraints do not match anything available.

## What This Error Means

pip queries PyPI (or your custom index) for a package matching the name and constraint you specified:

```
ERROR: Could not find a version that satisfies the requirement nonexistent-package (from versions: none)
ERROR: No matching distribution found for nonexistent-package
```

Or for platform-specific issues:

```
ERROR: nonexistent-package is not a supported wheel on this platform.
```

## Why It Happens

- The package name is misspelled or uses incorrect casing (pip names are case-sensitive)
- The version constraint filters out all available versions
- The package exists only on a custom index you did not configure
- The package is platform-specific and has no wheel for your OS/architecture
- The package was removed from PyPI (yanked or deleted)
- You are behind a proxy or firewall that blocks access to PyPI

## How to Fix It

### Verify the Package Name on PyPI

```bash
pip search <partial-name>  # if available
# Or visit https://pypi.org/search/?q=<partial-name>
```

### Check Available Versions

```bash
pip index versions <package>
```

Or:

```bash
pip install <package>==  # shows available versions
```

### Remove Version Constraints Temporarily

```bash
pip install <package>  # no version pin
```

### Add a Custom Index

```bash
pip install --index-url https://private-index.example.com/simple <package>
```

Or configure permanently:

```ini
# pip.conf / pip.ini
[global]
index-url = https://private-index.example.com/simple
extra-index-url = https://pypi.org/simple
```

### Use --only-binary or --no-binary

```bash
pip install --only-binary :all: <package>  # wheels only
pip install --no-binary :all: <package>      # source only
```

### Use a Mirror Index

```bash
pip install -i https://mirrors.aliyun.com/pypi/simple/ <package>
```

## Common Mistakes

- Misspelling the package name (e.g., `pillow` vs `Pillow`, `scikit-learn` vs `sklearn`)
- Using an exact version when only newer versions exist on PyPI
- Forgetting to add `--extra-index-url` for packages split across multiple indexes
- Not checking platform support for architecture-specific packages

## Related Pages

- [pip Install Error]({{< relref "/tools/pip/pip-install-error" >}}) -- install failures
- [pip Connection Error]({{< relref "/tools/pip/pip-connection-error" >}}) -- network issues
- [pip SSL Error]({{< relref "/tools/pip/pip-ssl-error" >}}) -- SSL certificate errors
