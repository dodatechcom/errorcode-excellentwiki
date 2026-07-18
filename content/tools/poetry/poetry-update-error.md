---
title: "[Solution] Poetry Update Causes Resolution Failure Error — How to Fix"
description: "Fix Poetry update resolution failures when poetry update cannot find compatible versions. Resolve dependency conflicts and solver timeouts in Poetry."
tools: ["poetry"]
error-types: ["update-error"]
severities: ["error"]
weight: 5
comments: true
---

This error means `poetry update` could not resolve a valid set of dependency versions. The solver reached a conflict it cannot work around, timed out, or found that updating one package breaks compatibility with others.

## Why It Happens

- A package update requires a newer version of a shared dependency that conflicts with another package's constraints
- The solver is exploring too many version combinations and times out
- A package you are updating has dropped support for your Python version
- Two packages have mutually exclusive version constraints that no solver can satisfy
- The PyPI mirror or private repository does not have the latest version of a dependency
- A dependency's metadata on PyPI is malformed, causing the solver to fail

## Common Error Messages

```
SolverProblemError

Because package-a (>=2.0) depends on package-b (>=3.0,<4.0)
and package-c (>=1.0) depends on package-b (>=2.0,<3.0),
package-a (>=2.0) cannot be installed.
```

```
TimeoutError

Solver timed out after 300 seconds.
```

```
PackageNotFound

Unable to find information for package-d on PyPI.
```

```
VersionSolverCouldNotFindSolution

Solver could not find a solution for the requested dependencies.
```

## How to Fix It

### 1. Update Specific Packages Only

```bash
poetry update package-name
```

Updating one package at a time narrows the solver's search space.

### 2. Update with Verbose Output

```bash
poetry update -vvv
```

This shows the solver's decision process and reveals which constraint is causing the conflict.

### 3. Use `--dry-run` to Preview Changes

```bash
poetry update --dry-run
```

This shows what would be updated without making changes, helping you identify problematic updates.

### 4. Pin Compatible Versions

```bash
poetry add package-a@^2.0 package-b@^3.0
poetry lock
```

Pin versions that are known to work together.

### 5. Upgrade the Solver

```bash
poetry self update
```

Newer Poetry versions have improved solver performance and bug fixes.

### 6. Clear the Cache

```bash
poetry cache clear --all pypi
poetry update
```

Stale cache entries can cause the solver to work with outdated package metadata.

### 7. Use `poetry add` Instead

```bash
poetry add package-name@latest
```

`poetry add` resolves and installs in one step, which sometimes succeeds where `poetry update` fails.

## Common Scenarios

**Updating one package breaks everything.** A transitive dependency changed its constraints. Use `poetry show --tree` to see the full dependency tree and find the conflicting constraint.

**Solver times out on large projects.** Increase the solver timeout or update Poetry:

```bash
POETRY_SOLVER_TIMEOUT=600 poetry update
```

**New version of a package dropped Python 3.8 support.** Pin to the last version that supports your Python:

```bash
poetry add package-name@^1.9
```

## Prevent It

1. Update packages incrementally (one at a time) rather than all at once to isolate conflicts
2. Run `poetry update --dry-run` before actual updates to preview changes
3. Use `poetry show --tree` regularly to understand your dependency tree and spot potential conflicts early
