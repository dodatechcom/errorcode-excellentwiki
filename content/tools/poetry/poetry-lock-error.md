---
title: "[Solution] Poetry Lock File Conflict Error — How to Fix"
description: "Fix Poetry lock file conflicts when poetry.lock is corrupted or inconsistent. Regenerate lock files, resolve merge conflicts, and restore dependency pins."
tools: ["poetry"]
error-types: ["lock-error"]
severities: ["error"]
weight: 5
comments: true
---

This error means `poetry.lock` is inconsistent with `pyproject.toml` or has become corrupted. Poetry detects a mismatch between the lock file and your declared dependencies and refuses to install until the conflict is resolved.

## Why It Happens

- You edited `pyproject.toml` (added, removed, or changed a dependency) without running `poetry lock`
- `poetry.lock` was modified manually or corrupted by a failed write operation
- A git merge conflict left the lock file in an inconsistent state
- A teammate committed a `poetry.lock` generated with a different Poetry version
- The lock file was truncated because the disk ran out of space during generation
- You checked out a branch with a different `pyproject.toml` but did not update the lock

## Common Error Messages

```
PoetryException

poetry.lock was not consistent with pyproject.toml
Run `poetry lock [--no-update]` to fix it.
```

```
LockError: Poetry lock file is not consistent with pyproject.toml.
Run `poetry lock` to update it.
```

```
Invalid pyproject.toml: poetry.lock and pyproject.toml do not match.
Please run `poetry lock` to regenerate the lock file.
```

```
RuntimeError: poetry.lock file was found to be invalid.
The lock file may have been corrupted.
```

## How to Fix It

### 1. Regenerate the Lock File

```bash
poetry lock
```

This re-resolves every dependency and writes a fresh `poetry.lock` from your current `pyproject.toml`.

### 2. Regenerate Without Updating Versions

```bash
poetry lock --no-update
```

This keeps existing pinned versions and only updates the lock file metadata to match `pyproject.toml`. Use this when you want to preserve current dependency versions.

### 3. Fix Merge Conflicts

Never try to manually merge `poetry.lock`. Instead:

```bash
# Accept the incoming lock file and regenerate
git checkout --theirs poetry.lock
poetry lock

# Or regenerate from scratch
poetry lock
```

For a cleaner workflow, add this to `.gitattributes`:

```
poetry.lock merge=ours
```

This automatically resolves lock file conflicts by preferring the current branch's version.

### 4. Validate Lock File Integrity

```bash
poetry check
poetry lock --check
```

`poetry check` validates `pyproject.toml` syntax. `poetry lock --check` confirms the lock file is consistent without modifying anything.

### 5. Delete and Regenerate the Lock File

```bash
rm poetry.lock
poetry lock
```

Use this when the lock file is too corrupted for `--no-update` to fix.

### 6. Pin Poetry Version in Your Project

Prevent version mismatches across team members:

```toml
[tool.poetry]
requires-poetry = ">=1.7.0,<2.0.0"
```

### 7. Regenerate After Changing Python Version

```bash
poetry lock
poetry env use python3.11
poetry install
```

## Common Scenarios

**Git merge produces lock file conflicts.** The fastest resolution is to accept one side and regenerate:

```bash
git checkout --ours poetry.lock  # keep your version
poetry lock                      # regenerate
```

**Lock file is corrupted after a power outage.** Delete and regenerate:

```bash
rm poetry.lock
poetry lock
```

**Different Poetry versions produce different lock files.** Pin the Poetry version in `pyproject.toml` and use `requires-poetry` to enforce it across your team.

## Prevent It

1. Always run `poetry lock` after modifying `pyproject.toml` before committing
2. Never manually edit `poetry.lock` — let Poetry manage it exclusively
3. Pin `requires-poetry` in `pyproject.toml` so all team members use the same Poetry version
