---
title: "GitHub Actions YAML Parse Error"
description: "GitHub Actions workflow fails due to YAML parsing error."
tools: ["github-actions"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# GitHub Actions — YAML Parse Error

This error occurs when GitHub Actions cannot parse the workflow YAML file. Invalid YAML syntax prevents the workflow from being loaded and executed.

## Common Causes

- Incorrect indentation (YAML is indentation-sensitive)
- Missing colons after keys
- Invalid characters in YAML values
- Unclosed strings or brackets
- Tab characters instead of spaces

## How to Fix

### Validate YAML Syntax

```bash
actionlint .github/workflows/ci.yml
```

### Fix Indentation

```yaml
# Wrong - inconsistent indentation
jobs:
  build
    runs-on: ubuntu-latest

# Correct - consistent 2-space indentation
jobs:
  build:
    runs-on: ubuntu-latest
```

### Quote Special Characters

```yaml
# Wrong
env:
  VERSION: 1.0.0  # YAML interprets as number

# Correct
env:
  VERSION: "1.0.0"
```

### Fix Expression Syntax

```yaml
# Wrong - missing ${{ }}
if: success()
run: echo Hello

# Correct
if: ${{ success() }}
run: echo "Hello ${{ github.actor }}"
```

### Validate with Python

```bash
python -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))"
```

### Check for Tab Characters

```bash
grep -P '\t' .github/workflows/ci.yml
```

## Examples

```yaml
# Error: missing colon
jobs:
  build
    runs-on: ubuntu-latest

# Error: unclosed bracket
steps:
  - uses: actions/checkout@v4
    with:
      node-version: ['20'
```

## Related Errors

- [GitHub Actions Permission Error]({{< relref "/tools/github-actions/github-actions-permission-error" >}}) — permission issues
- [GitHub Actions Secret Error]({{< relref "/tools/github-actions/github-actions-secret-error" >}}) — secret not found
- [GitHub Actions Env Error]({{< relref "/tools/github-actions/github-actions-env-error" >}}) — environment variable issues
