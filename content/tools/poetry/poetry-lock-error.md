---
title: "[Solution] Poetry Lock Error — Fix Lock File and pyproject.toml Inconsistency"
description: "Fix Poetry lock errors when poetry.lock and pyproject.toml are out of sync or corrupted. Regenerate lock files without losing pinned dependency versions."
tools: ["poetry"]
error-types: ["lock-error"]
severities: ["error"]
weight: 5
---

This error means `poetry.lock` does not match the current state of `pyproject.toml`. Poetry detects a mismatch and refuses to install until the lock file is updated or regenerated.

## What This Error Means

Poetry maintains `poetry.lock` as a record of every exact version and hash for your dependency tree. When you change `pyproject.toml` without running `poetry lock`, or when `poetry.lock` is edited manually, Poetry raises:

```
PoetryException

poetry.lock was not consistent with pyproject.toml
Run `poetry lock [--no-update]` to fix it.
```

## Why It Happens

- You edited `pyproject.toml` (added, removed, or changed a dependency) without running `poetry lock`
- `poetry.lock` was modified manually or by a merge conflict
- A teammate committed a `poetry.lock` generated with a different Poetry version
- The lock file was truncated by a failed write (disk full, interrupted process)
- You checked out a branch with a different `pyproject.toml` but did not update the lock

## How to Fix It

### Regenerate the Lock File

```bash
poetry lock
```

This re-resolves every dependency and writes a fresh `poetry.lock`.

### Regenerate Without Updating Versions

```bash
poetry lock --no-update
```

This keeps existing pinned versions and only updates the metadata to match `pyproject.toml`.

### Validate Lock File Integrity

```bash
poetry check
```

This confirms `pyproject.toml` is valid syntax. For the lock file specifically:

```bash
poetry lock --check
```

### Fix Merge Conflicts in poetry.lock

Never try to manually merge `poetry.lock`. Instead:

```bash
# Accept the incoming lock file
git checkout --theirs poetry.lock

# Or regenerate from scratch
poetry lock
```

### Regenerate After Changing Python Version Constraint

If you changed the Python version in `pyproject.toml`:

```bash
poetry lock
poetry env use python3.11
poetry install
```

### Pin Poetry Version in Your Project

Prevent version mismatches across team members:

```toml
[tool.poetry]
requires-poetry = ">=1.7.0,<2.0.0"
```

## Common Mistakes

- Committing `pyproject.toml` changes without running `poetry lock`
- Trying to merge `poetry.lock` manually in git
- Ignoring the `--no-update` flag when you want to preserve current versions
- Using different Poetry versions across team members without pinning

## Related Pages

- [Poetry Dependency Conflict]({{< relref "/tools/poetry/poetry-dependency-conflict" >}}) -- solver failures
- [Poetry Install Error]({{< relref "/tools/poetry/poetry-install-error" >}}) -- install failures
- [Poetry Package Not Found]({{< relref "/tools/poetry/poetry-package-not-found" >}}) -- missing packages
