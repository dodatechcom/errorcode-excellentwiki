---
title: "[Solution] Terraform Variable File Not Found"
description: "Fix Terraform variable file not found errors when the specified tfvars file doesn't exist."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Variable file not found errors occur when a referenced tfvars file is missing:

```
Error: Failed to read file

The file "production.tfvars" cannot be read: no such file or directory.
```

## Common Causes

- Typo in filename.
- Wrong directory path.

## How to Fix

**Check file exists:**

```bash
ls -la *.tfvars
```

**Create the file:**

```bash
cat > production.tfvars << EOF
environment    = "production"
instance_count = 5
instance_type  = "t3.large"
EOF
```

## Examples

```bash
# Auto-loaded files
terraform.tfvars
*.auto.tfvars

# Explicit file
terraform plan -var-file="production.tfvars"
```
