---
title: "[Solution] Terraform Invalid Flag"
description: "Fix Terraform invalid flag errors when an unrecognized flag is used."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Invalid flag errors occur when an unrecognized flag is passed:

```
Error: Invalid flag

"-option" is not a valid flag. Did you mean "-out"?
```

## Common Causes

- Typo in flag name.
- Flag from wrong Terraform version.

## How to Fix

**Check available flags:**

```bash
terraform plan -help
```

**Use correct flag syntax:**

```bash
# Correct
terraform plan -out=tfplan

# Wrong
terraform plan -output=tfplan
```

## Examples

```bash
terraform plan -out=tfplan
terraform apply -auto-approve
terraform destroy -target=aws_instance.web
```
