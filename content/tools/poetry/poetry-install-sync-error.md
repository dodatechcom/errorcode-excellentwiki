---
title: "[Solution] Poetry Install Sync Error -- Fix --sync Removing Too Many Packages"
description: "Fix Poetry install sync error when --sync removes packages you expected to keep. Review dependency groups and sync behavior."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means `poetry install --sync` removed packages that were installed but are not in the lock file. More packages were removed than expected.

## Common Causes

- The lock file does not include all dependency groups
- A package was installed with pip instead of Poetry
- Optional dependency groups were not included in sync

## How to Fix

### 1. Include All Groups in Sync

```bash
poetry install --sync --with dev,test
```

### 2. Check What Would Be Removed

```bash
poetry install --dry-run
```

### 3. Review Installed Packages

```bash
poetry show --no-header | wc -l
```

### 4. Reinstall Everything

```bash
poetry install --sync --with dev,test --remove-untracked
```

## Examples

```bash
$ poetry install --sync
Package operations: 5 installs, 12 removals

# Too many removals -- include dev group:
$ poetry install --sync --with dev
Package operations: 5 installs, 2 removals
```
