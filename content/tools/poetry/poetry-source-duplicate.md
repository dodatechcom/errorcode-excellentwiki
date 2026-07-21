---
title: "[Solution] Poetry Source Duplicate -- Fix Duplicate Package Sources"
description: "Fix Poetry source duplicate errors when multiple package sources are configured for the same name. Remove or rename duplicate sources."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means you have defined multiple sources with the same name in `pyproject.toml`. Poetry cannot determine which source to use.

## Common Causes

- Copy-pasted source blocks without changing the name
- Merge conflicts left duplicate sources
- Multiple `[[tool.poetry.source]]` entries with identical names

## How to Fix

### 1. Check Current Sources

```bash
poetry source --list
```

### 2. Edit pyproject.toml

Remove the duplicate entry:

```toml
[[tool.poetry.source]]
name = "private"
url = "https://pypi.internal.com/simple/"

# Remove the second [[tool.poetry.source]] with the same name
```

### 3. Disable One Source

```bash
poetry source disable private
```

### 4. Validate Configuration

```bash
poetry check
```

## Examples

```bash
$ poetry check
ValueError: Source "private" is defined multiple times in pyproject.toml

# Fix pyproject.toml by removing the duplicate [[tool.poetry.source]] block.
$ poetry check
All checks passed!
```
