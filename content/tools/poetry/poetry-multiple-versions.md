---
title: "[Solution] Poetry Multiple Versions Error - Fix Multiple Versions Found"
description: "Fix Poetry error when multiple versions of the same package are found during resolution. Resolve version conflicts and duplicate dependencies."
tools: ["poetry"]
error-types: ["multiple-versions"]
severities: ["error"]
weight: 5
---

This error means Poetry found multiple versions of the same package that it cannot reconcile. The dependency resolver encountered two or more sources providing different versions of a package simultaneously.

## What This Error Means

When Poetry's resolver finds multiple candidates for a package and cannot determine which to use, you see:

```
SolverProblemError: Because <package> (X.Y.Z) and <package> (A.B.C) are incompatible...
# or
VersionSolverException: Unable to find a version that satisfies the constraint
```

This typically means your project or its dependencies require the same package at two incompatible version ranges, and the solver cannot narrow it to a single version.

## Why It Happens

- Two dependencies require different versions of the same transitive package
- A dependency is listed both as a direct and transitive dependency with different version constraints
- You specified a version in `pyproject.toml` that conflicts with what a dependency requires
- The lock file was generated on a system with different dependency resolution
- A package was recently updated and its new version conflicts with an older pin
- You have both a regular and optional dependency requiring different versions

## How to Fix It

### Check the dependency tree

```bash
poetry show <package>
poetry show --tree
```

This reveals which dependencies are pulling in conflicting versions.

### Pin a specific version in pyproject.toml

```toml
[tool.poetry.dependencies]
package-name = ">=1.0,<2.0"
```

Constraining the version range helps the solver find a single compatible version.

### Update all dependencies

```bash
poetry update
```

This re-resolves the full dependency tree and often finds a compatible set.

### Remove and regenerate the lock file

```bash
rm poetry.lock
poetry lock
poetry install
```

A fresh lock file resolves all conflicts from scratch.

### Use dependency groups for conflicting needs

```toml
[tool.poetry.group.dev.dependencies]
package-name = ">=2.0"

[tool.poetry.group.test.dependencies]
package-name = ">=1.5"
```

Grouping can help identify which dependencies drive the conflict.

### Override a specific transitive dependency

```toml
[tool.poetry.dependencies]
package-name = {version = ">=1.0", allow-prereleases = true}
```

Allowing prereleases or widening the range can resolve tight constraints.

## Common Mistakes

- Not running `poetry show --tree` to understand where conflicting versions come from
- Using `poetry add` without checking existing constraints
- Locking to exact versions that become outdated as dependencies update
- Ignoring lock file changes when merging branches
- Not testing dependency resolution in a clean environment

## Related Pages

- [Poetry Dependency Conflict]({{< relref "/tools/poetry/poetry-dependency-conflict" >}}) -- general dependency conflicts
- [Poetry Lock Error]({{< relref "/tools/poetry/poetry-lock-error" >}}) -- lock file problems
- [Poetry Package Not Found]({{< relref "/tools/poetry/poetry-package-not-found" >}}) -- missing packages
