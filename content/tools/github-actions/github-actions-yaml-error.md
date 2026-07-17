---
title: "GitHub Actions YAML Syntax Error"
description: "GitHub Actions workflow file has invalid YAML syntax."
tools: ["github-actions"]
error-types: ["build-error"]
severities: ["error"]
tags: ["github-actions", "yaml", "syntax", "workflow", "ci"]
weight: 5
---

# GitHub Actions YAML Syntax Error

A GitHub Actions YAML syntax error occurs when the workflow file has invalid YAML formatting. GitHub Actions requires strict YAML syntax with correct indentation and valid expressions.

## Common Causes

- Incorrect indentation (YAML is indentation-sensitive)
- Missing colons or quotes around strings
- Invalid `${{ }}` expression syntax
- YAML special characters not quoted

## How to Fix

### Validate YAML Syntax

```bash
actionlint .github/workflows/ci.yml
```

### Check Indentation

```yaml
# Correct indentation
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          node-version: '20'
```

### Quote Special Characters

```yaml
# Correct
env:
  VERSION: "1.0.0"  # Quote if starts with special char
  URL: "https://example.com"
```

### Fix Expression Syntax

```yaml
# Correct
if: ${{ success() }}
run: echo "Hello ${{ github.actor }}"

# Wrong
if: success()  # Missing ${{ }}
```

### Use YAML Validator

```bash
python -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))"
```

## Examples

```yaml
# Error: invalid YAML
jobs:
  build
    runs-on: ubuntu-latest
# Missing colon after 'build'

# Fix:
jobs:
  build:
    runs-on: ubuntu-latest
```

## Related Errors

- [Permission Error]({{< relref "/tools/github-actions/github-actions-permission-error" >}}) — permission issues
- [Secret Error]({{< relref "/tools/github-actions/github-actions-secret-error" >}}) — secret not found
