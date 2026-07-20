---
title: "[Solution] Terraform Working Directory Error"
description: "Fix Terraform working directory errors when terraform is run in the wrong directory."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Working directory errors occur when Terraform can't find configuration:

```
Error: No configuration files found

No .tf files are present in the current working directory.
```

## Common Causes

- Not in the correct directory.
- Configuration files in a subdirectory.

## How to Fix

**Navigate to the correct directory:**

```bash
cd /path/to/terraform/config
terraform plan
```

**Use the `-chdir` flag:**

```bash
terraform -chdir=/path/to/config plan
```

**Check current directory:**

```bash
pwd
ls *.tf
```

## Examples

```bash
ls -la *.tf
terraform -chdir=./environments/prod plan
```
