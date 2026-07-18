---
title: "[Solution] pip Legacy Dependency Resolution Error — Fix Backwards Incompatible Behavior"
description: "Fix pip backwards incompatible dependency resolution errors. Upgrade to the new resolver or use legacy behavior flags to resolve installation conflicts."
tools: ["pip"]
error-types: ["dependency-error"]
severities: ["warning"]
weight: 5
---

This error means pip's dependency resolver detects a conflict it cannot resolve automatically. The resolver behavior changed significantly between pip 20.2 and 20.3, breaking workflows that relied on the old backtracking behavior.

## What This Error Means

pip's current resolver performs deep dependency resolution and fails when it finds irreconcilable version conflicts:

```
ERROR: pip's dependency resolution failed. The following dependencies are conflicting:
  package-a==2.0 depends on package-b>=3.0
  package-c==1.0 depends on package-b<2.0
```

Or with the legacy resolver warning:

```
WARNING: pip's legacy resolver is deprecated. Migrate to the new resolver.
```

## Why It Happens

- Two packages require incompatible versions of the same dependency
- A transitive dependency pins a version range that conflicts with a direct requirement
- Your requirements.txt has version constraints that contradict each other
- An older package has not been updated to support newer dependency versions
- You are using flags like `--use-deprecated legacy-resolver` on a modern pip

## How to Fix It

### Identify the Conflicting Dependencies

```bash
pip install <package> 2>&1 | grep "conflicting"
pip check  # check for installed conflicts
```

### Upgrade All Packages Together

Let pip find a consistent resolution:

```bash
pip install --upgrade <package> <conflicting-package>
```

### Use --upgrade-strategy

```bash
pip install --upgrade-strategy eager <package>
```

### Install with the Legacy Resolver (Temporary)

```bash
pip install --use-deprecated legacy-resolver <package>
```

### Use pip-tools to Resolve Conflicts

```bash
pip install pip-tools
pip-compile requirements.in
pip install -r requirements.txt
```

### Relax Version Constraints

```yaml
# requirements.in (no pinning)
requests
flask

# Let pip-tools resolve versions
```

### Isolate in a Separate Environment

```bash
python -m venv isolated_env
source isolated_env/bin/activate
pip install <conflicting-package>
```

## Common Mistakes

- Using the legacy resolver as a permanent workaround instead of fixing conflicts
- Pinning every dependency with exact versions, leaving no room for resolution
- Not running `pip check` after installation to verify consistency
- Ignoring `DeprecationWarning` messages about the legacy resolver

## Related Pages

- [pip Dependency Conflict]({{< relref "/tools/pip/pip-dependency-conflict" >}}) -- dependency conflicts
- [pip Install Error]({{< relref "/tools/pip/pip-install-error" >}}) -- install failures
- [pip Version Error]({{< relref "/tools/pip/pip-version-error" >}}) -- pip version issues
