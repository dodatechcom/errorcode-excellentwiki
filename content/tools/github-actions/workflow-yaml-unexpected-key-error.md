---
title: "[Solution] Workflow YAML Unexpected Key Error"
description: "Fix GitHub Actions workflow YAML unexpected key errors in workflow files."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Unexpected key errors occur when the workflow YAML contains keys that GitHub Actions does not recognize:

```
Error: .github/workflows/build.yml: Unexpected key 'bulid'
```

## Common Causes

- Typo in YAML key names (e.g., `bulid` instead of `build`).
- Indentation issues causing keys to be at the wrong level.
- Copy-pasting from documentation with incorrect keys.
- Using keys from an older or newer GitHub Actions version.

## How to Fix

**Use a YAML linter to catch typos:**

```bash
yamllint .github/workflows/build.yml
```

**Validate the workflow:**

```bash
actionlint .github/workflows/build.yml
```

**Correct YAML structure:**

```yaml
name: Build
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```

## Examples

```yaml
# Wrong - misspelled key
name: Build
on: push
jods:
  build:
    runs-on: ubuntu-latest

# Correct
name: Build
on: push
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```
