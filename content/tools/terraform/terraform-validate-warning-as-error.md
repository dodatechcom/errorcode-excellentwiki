---
title: "[Solution] Terraform Validate Warning As Error"
description: "Fix Terraform validate warning as error when warnings are treated as errors in CI/CD."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Validate warning as error occurs when CI/CD fails on warnings:

```
Warning: Value for undeclared variable

Variable "unused_var" is not declared. It will be ignored.

Error: warnings treated as errors
```

## Common Causes

- CI/CD configured to fail on warnings.
- Warnings from legacy configurations.

## How to Fix

**Fix the warnings:**

```bash
# Remove unused variables from variables.tf
# Or add them to usage
```

**Configure CI/CD to allow warnings:**

```yaml
# GitHub Actions
- name: Terraform Validate
  run: terraform validate
  continue-on-error: true
```

**Use `-json` for structured output:**

```bash
terraform validate -json | jq '.diagnostics[] | select(.severity == "warning")'
```

## Examples

```bash
# Ignore warnings in CI
terraform validate 2>&1 | grep -v "Warning:"

# Or use -no-color for machine parsing
terraform validate -no-color 2>&1 | tee validate-output.txt
```
