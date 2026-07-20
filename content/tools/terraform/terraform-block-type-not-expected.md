---
title: "[Solution] Terraform Block Type Not Expected"
description: "Fix Terraform block type not expected errors when using an incorrect nested block."
tools: ["terraform"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Block type errors occur when an unexpected nested block is used:

```
Error: Block type "option" is not expected here

Only "tags", "root_block_device", "ebs_block_device" are
expected here.
```

## Common Causes

- Wrong block type name.
- Block is deprecated in current provider version.

## How to Fix

**Check available block types:**

```bash
terraform providers schema -json | jq   '.provider_schemas["registry.terraform.io/hashicorp/aws"].resource_schemas.aws_instance.block.block_types | keys'
```

**Use correct block syntax:**

```hcl
resource "aws_instance" "web" {
  ami = "ami-12345"

  root_block_device {
    volume_size = 50
    volume_type = "gp3"
  }
}
```

## Examples

```bash
terraform providers schema -json | jq   '.provider_schemas["registry.terraform.io/hashicorp/aws"].resource_schemas.aws_instance.block.block_types | keys'
```
