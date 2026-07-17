---
title: "[Solution] pip Dependency Conflict — Fix Conflicting Requirements Error"
description: "Fix pip dependency conflict errors when the resolver finds incompatible package versions. Step-by-step guide to resolve conflicting requirements in Python."
tools: ["pip"]
error-types: ["dependency-error"]
severities: ["error"]
weight: 5
---

This error means pip's dependency resolver detected two or more packages that require incompatible versions of a shared dependency. pip refuses to proceed because installing one package would break another.

## What This Error Means

pip's backtracking resolver walks through your requirements and checks every dependency tree. When it finds that package A requires `requests>=2.28` but package B pins `requests==2.27`, it raises a dependency conflict error. The full message usually looks like:

```
ERROR: pip's dependency resolver does not take into account all the packages that are installed.
ERROR: Cannot install -r requirements.txt because these package versions have conflicting dependencies.
```

## Why It Happens

- You pinned a package version that is too old or too new for another dependency
- A transitive dependency was updated to a version that breaks compatibility
- Your `requirements.txt` contains explicit version pins that contradict each other
- You are mixing packages from different sources (PyPI vs git) with mismatched versions
- The resolver backtracks through every combination and still finds no solution

## How to Fix It

### Upgrade pip First

An older pip resolver may produce false conflicts. Upgrade before anything else:

```bash
pip install --upgrade pip
```

### Use `--resolver=backtracking`

Force the modern backtracking resolver:

```bash
pip install -r requirements.txt --resolver=backtracking
```

### Relax Version Pins

Change strict pins to compatible ranges:

```
# Bad
requests==2.27.0

# Good
requests>=2.27,<3.0
```

### Check the Conflict Chain

Use `pip check` to see what is actually broken:

```bash
pip check
```

This outputs the specific packages and versions in conflict, which helps you decide which pin to relax.

### Install with `--force-reinstall`

If the conflict stems from a cached state:

```bash
pip install -r requirements.txt --force-reinstall
```

### Use a Constraint File

Create `constraints.txt` to set upper bounds that satisfy all packages:

```
requests<3.0
urllib3<2.1
```

Then install with:

```bash
pip install -r requirements.txt -c constraints.txt
```

## Common Mistakes

- Pinning exact versions without checking transitive dependencies
- Copying version numbers from a tutorial that uses different Python or OS versions
- Running `pip install package` and then appending to `requirements.txt` without verifying compatibility
- Ignoring `pip check` output after a successful install

## Related Pages

- [pip Install Error]({{< relref "/tools/pip/pip-install-error" >}}) -- environment errors during install
- [pip Version Error]({{< relref "/tools/pip/pip-version-error" >}}) -- no matching distribution found
- [pip Cache Error]({{< relref "/tools/pip/pip-cache-error" >}}) -- cache corruption issues
