---
title: "[Solution] pip No Matching Distribution Found — Fix Version Resolution Errors"
description: "Fix pip no matching distribution found errors when a package version is unavailable for your Python version, platform, or operating system combination."
tools: ["pip"]
error-types: ["version-error"]
severities: ["error"]
weight: 5
---

This error means pip searched all configured indexes for a version of a package matching your requirements and system constraints, but found nothing that satisfies every condition simultaneously.

## What This Error Means

pip resolves packages by checking available versions against your Python version, operating system, and architecture. When every candidate version is filtered out, you get:

```
ERROR: No matching distribution found for <package>
```

This can mean the package exists on PyPI but not for your Python version, OS, or CPU architecture.

## Why It Happens

- The requested version does not exist (typo in the version string)
- The package dropped support for your Python version (e.g., Python 3.7)
- You are on a platform without a pre-built wheel (e.g., armv7l Linux) and no sdist is available
- The package was removed or yanked from PyPI
- You are using a private index that does not mirror the package
- You are searching a platform-specific index (e.g., only musllinux wheels)

## How to Fix It

### Verify the Version Exists

```bash
pip index versions <package>
```

This lists all published versions. Check if your requested version is in the list.

### Relax the Version Constraint

```
# Bad
package==99.99.99

# Good
package>=2.0,<3.0
```

### Check Your Python Version

```bash
python3 --version
```

If the package requires Python 3.9+ and you are on 3.7, upgrade Python or use `pyenv`:

```bash
pyenv install 3.11
pyenv local 3.11
```

### Check Platform Availability

```bash
pip install <package> --only-binary=:all: --dry-run
```

If the dry run fails, the package has no binary wheel for your platform. Install build tools and let pip build from source:

```bash
pip install <package> --no-binary=:all:
```

### Use the Correct Index URL

```bash
pip install <package> -i https://pypi.org/simple/
```

## Common Mistakes

- Using `==` with a version that was never published (check with `pip index versions`)
- Forgetting that alpha or pre-release versions require `--pre`
- Searching a platform-specific index that does not host your OS
- Copying install commands from tutorials targeting a different Python version

## Related Pages

- [pip Dependency Conflict]({{< relref "/tools/pip/pip-dependency-conflict" >}}) -- conflicting requirements
- [pip Connection Error]({{< relref "/tools/pip/pip-connection-error" >}}) -- network failures during install
- [pip SSL Error]({{< relref "/tools/pip/pip-ssl-error" >}}) -- SSL certificate issues
