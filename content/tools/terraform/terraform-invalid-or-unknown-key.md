---
title: "[Solution] Terraform Invalid Or Unknown Key"
description: "Fix Terraform invalid or unknown key errors when an unrecognized argument is used."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Unknown key errors occur when an unrecognized argument is present:

```
Error: Invalid or unknown key

on main.tf line 5, in resource "aws_instance" "web":
   5:   ami_name = "my-ami"
```

## Common Causes

- Typo in argument name.
- Argument from wrong provider version.

## How to Fix

**Check available attributes:**

```bash
terraform providers schema -json | jq   '.provider_schemas["registry.terraform.io/hashicorp/aws"].resource_schemas.aws_instance.block.attributes | keys'
```

## Examples

```bash
terraform providers schema -json > schema.json
cat schema.json | jq '.provider_schemas["registry.terraform.io/hashicorp/aws"].resource_schemas.aws_instance.block.attributes | keys'
```
