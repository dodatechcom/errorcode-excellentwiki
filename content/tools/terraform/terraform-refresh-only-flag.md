---
title: "[Solution] Terraform Refresh Only Flag"
description: "Fix Terraform refresh only flag errors when using -refresh-only mode incorrectly."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Refresh only mode errors occur when the flag is misused:

```
Error: -refresh-only is not supported with this command

The -refresh-only flag can only be used with "terraform plan".
```

## Common Causes

- Used `-refresh-only` with wrong command.
- Used with `apply` instead of `plan`.

## How to Fix

**Use with plan only:**

```bash
terraform plan -refresh-only
```

**Review changes:**

```bash
terraform plan -refresh-only -detailed-exitcode
```

**Apply the refresh:**

```bash
terraform apply -refresh-only
```

## Examples

```bash
# Detect drift
terraform plan -refresh-only

# Apply drift detection
terraform apply -refresh-only

# Check exit code
terraform plan -refresh-only -detailed-exitcode
```
