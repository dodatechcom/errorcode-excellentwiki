---
title: "[Solution] Terraform Missing Required Flag"
description: "Fix Terraform missing required flag errors when a mandatory flag is not provided."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Missing required flag errors occur when a command requires a flag that's not provided:

```
Error: Required flag not provided

The "-var" flag is required when using "-var-file".
```

## Common Causes

- Forgot to include required flag.
- Script doesn't pass all required flags.

## How to Fix

**Add the required flag:**

```bash
terraform apply -var="environment=production"
```

**Use variable files:**

```bash
terraform apply -var-file="production.tfvars"
```

**Check flag requirements:**

```bash
terraform plan -help
```

## Examples

```bash
terraform plan -var="env=prod" -out=tfplan
terraform apply -auto-approve -var-file="prod.tfvars"
terraform import aws_instance.web i-12345678
```
