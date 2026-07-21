---
title: "[Solution] Poetry Config Unknown Key -- Fix Invalid Configuration Key"
description: "Fix Poetry config unknown key errors when poetry.toml or pyproject.toml contains unrecognized configuration keys. Remove or correct invalid keys."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry found a configuration key it does not recognize. Poetry may have changed its config schema between versions.

## Common Causes

- Using a key from an older Poetry version
- Typo in the configuration key name
- Mixing Poetry 1.x and 2.x configuration syntax
- Copy-pasting config from an external source with wrong keys

## How to Fix

### 1. Check Current Configuration

```bash
poetry config --list
```

### 2. View Valid Keys

```bash
poetry config virtualenvs.in-project
```

### 3. Edit poetry.toml Manually

```bash
cat poetry.toml
# Remove unknown keys
```

### 4. Reset Configuration

```bash
rm poetry.toml
poetry config virtualenvs.in-project true
```

## Examples

```bash
$ poetry install
ConfigurationError: Unknown configuration key: virtualenvs.creates

$ poetry config --list
# Check valid keys

# Fix poetry.toml:
[virtualenvs]
in-project = true
# Removed: creates = true
```
